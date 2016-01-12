"""
Db module.
"""

from tinydb import TinyDB, where
from tinydb.storages import MemoryStorage

class Table(object):
    def __init__(self, db, name):
        self._table = db.table(name)
    def find(self):
        raise NotImplementedError()

class Db(object):
    def __init__(self, filename=None):
        if filename is None:
            self._db = TinyDB(storage=MemoryStorage)
        else:
            self._db = TinyDB(filename)
        pass
    def __dir__(self):
        _db = super(Db,self).__getattribute__('_db')
        return super(Db,self).__dir__() + list(_db.tables())
    def __getattribute__(self, attr):
        _db = super(Db,self).__getattribute__('_db')
        if attr in _db.tables():
            return Table(_db, attr)
        else:
            return super(Db,self).__getattribute__(attr)