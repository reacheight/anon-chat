from vedis import Vedis


class Database:
    def __init__(self, file_name):
        self.file_name = file_name

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def add(self, key, value):
        with Vedis(self.file_name) as database:
            database[key] = value

    def delete(self, key):
        with Vedis(self.file_name) as database:
            del database[key]

    def get(self, key, default_value=None):
        with Vedis(self.file_name) as database:
            try:
                return database[key].decode('utf-8')
            except KeyError:
                if default_value is not None:
                    return default_value
                else:
                    raise
