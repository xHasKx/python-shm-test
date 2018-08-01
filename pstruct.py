from ctypes import *


IPC_CREAT = 512
libc = CDLL("", use_errno=True, use_last_error=True)


# int shmget(key_t key, size_t size, int shmflg);
shmget = libc.shmget
shmget.restype = c_int
shmget.argtypes = (c_int, c_size_t, c_int)


# void* shmat(int shmid, const void *shmaddr, int shmflg);
shmat = libc.shmat
shmat.restype = c_void_p
shmat.argtypes = (c_int, c_void_p, c_int)


# int shmdt(const void *shmaddr);
shmdt = libc.shmdt
shmdt.restype = c_int
shmdt.argtypes = (c_void_p,)


class Struct(Structure):
	_fields_ = [
		("hour", c_ubyte),
		("minute", c_ubyte),
		("msg", c_char * 256),
	]

	def set(self, hour, minute, msg):
		self.hour = hour
		self.minute = minute
		self.msg = msg.encode("utf-8")

	def __str__(self):
		return "{:02d}:{:02d}: {}".format(self.hour, self.minute, self.msg.decode("utf-8"))


PStruct = POINTER(Struct)


def shm_begin(key):
	shm_id = shmget(key, sizeof(Struct), 0o666 | IPC_CREAT)
	if shm_id < 0:
		return
	ptr = shmat(shm_id, 0, 0)
	if ptr:
		return cast(ptr, PStruct)


def shm_done(p_struct):
	ptr = cast(p_struct, c_void_p)
	shmdt(ptr)



__all__ = ["shm_begin", "shm_done", "Struct"]
