#!/usr/bin/env python3
import time
import random
import string
from shared_struct import Struct

s = Struct.from_key(102)

try:
	while True:
		s.hour = random.randint(0, 23)
		s.minute = random.randint(0, 59)
		s.msg = ("".join(random.choice(string.ascii_letters + string.digits) for _ in range(32))).encode("utf-8")
		print(s)
		time.sleep(0.1)
except KeyboardInterrupt:
	print()
