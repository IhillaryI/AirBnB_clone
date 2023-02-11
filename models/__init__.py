#!/usr/bin/python3
"""
Model creates unique FileStorage instances
"""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
