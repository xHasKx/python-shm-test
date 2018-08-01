#!/usr/bin/env python3
import time
import random
import string
import pstruct

ps = pstruct.shm_begin(102)
print(ps)

for i in range(10):
	ps.contents.set(random.randint(0, 23), random.randint(0, 59), "".join(random.choice(string.ascii_letters + string.digits) for _ in range(32)))
	time.sleep(1)

pstruct.shm_done(ps)
