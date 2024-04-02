#!/usr/bin/python3
"""Basic dictionary"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
	"""BasicCache class"""

	def __init__(self):
		"""Initialize the class using the parent class __init__ method"""
		BaseCaching.__init__(self)

	def put(self, key, item):
		"""Add an item in the cache"""
		if key is None or item is None:
			return
		self.cache_data[key] = item

	def get(self, key):
		"""Get an item by key"""
		if key is None or key not in self.cache_data:
			return None
		return self.cache_data[key]
