from abc import ABC, abstractmethod


class DataStore(ABC):

  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(DataStore, cls).__new__(cls)
    return cls.instance

  @abstractmethod
  def get(object, key):
    pass

  @abstractmethod
  def set(object, key, value):
    pass

  @abstractmethod
  def delete(object, key):
    pass

  @abstractmethod
  def list(object, prefix):
    pass
