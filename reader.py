#!/usr/bin/env python3
import time
import pstruct

ps = pstruct.shm_begin(102)
print(ps)

time.sleep(0.1)
for i in range(10):
	print(ps.contents)
	time.sleep(1)

pstruct.shm_done(ps)
