#!/usr/bin/env python3
import time
from shared_struct import Struct

s = Struct.from_key(102)
try:
	while True:
		print(s) # prints '{hour}:{minute}: {msg}'
		time.sleep(0.1)
except KeyboardInterrupt:
	print()
