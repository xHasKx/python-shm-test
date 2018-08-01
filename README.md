# System V Shared Memory Test on Python

## How To Run:

* run both scripts (writer.py and reader.py) simultaneously
* both scripts is running infinite loops, press Ctrl+C to stop them
* writer script generating random data and writing it to struct placed in shared memory
* reader shows struct placed in shared mempry
* both scripts should generate same output like this:

      11:47: GWzyVNKJXodkxVTAwf1GLwkffeUsrMLf
      20:12: WHXq8cMs7kdYqQhrYm9EIyImyOnR5j0j
      11:53: sR2JOYooBDGhJJuFLcrEqs4hOxdRDnHW
      01:09: s1csST053DTvYZmvKjKgM52Bo38ZzQm0
      13:01: WHyTpAbybw2O8BhA6aiHLl1luPI8Rqa7
      00:08: hWEr6RX72IezYqOcKo42E4EwXyL80LG0
      13:59: inlGCKb26eNWCdZGW2ALyWZemiMzE1IY
      02:54: H6HCD1uO4k8Wz5s4bARnY3G8jBAkiBxo

## Synchronization

No synchronization (semaphores/mutexes) primitives is used.
