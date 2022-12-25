from ..settings import data_store


def get_athletes():
  return data_store.list('athlete')


def get_athlete(key):
  return data_store.get(key)


def set_athlete(key):
  data_store.set(key)


def delete_athlete(key):
  data_store.delete(key)
