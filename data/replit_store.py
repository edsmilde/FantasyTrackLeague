from replit import db

from data.store import DataStore


def get_key(object, key):
  return object + '_' + key


class ReplitDataStore(DataStore):

  def get(object, key):
    return db[get_key(object, key)]

  def set(object, key, value):
    db[get_key(object, key)] = value

  def delete(object, key):
    del db[get_key(object, key)]

  def list(object, prefix):
    return db.prefix(get_key(object, prefix))
