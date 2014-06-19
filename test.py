import os.path
import sys
import lib.py3utils as py3utils
import lib.py3anidb as py3anidb

target_metadata = py3anidb.anidbmodel.Base.metadata
print(target_metadata)
