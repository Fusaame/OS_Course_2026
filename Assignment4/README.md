**Assignement 4**

Based on my observation in Part 1, a **Race Condition** happens when multiple threads try to read and modify the exact same shared variable at the exact same time without any coordination. 
Even though `counter += 1` looks like a single command, the CPU executes it in steps (read, add, write). Because our 4 threads were running simultaneously, they constantly interrupted each other. For example, Thread A and Thread B often read the same value, added 1, and both wrote the same result back. Instead of the counter going up by 2, it only went up by 1. The increments "collided" and overwrote each other, which is why the final number was only `100,064` instead of the expected `400,000`.

### How the Mutex/Lock Solved the Problem (Based on Part 2)
To fix this, I used `threading.Lock()` as a **Mutex** (Mutual Exclusion). 
A Mutex acts like a single key to a room. When a thread wants to increment the counter, it must first "acquire" the lock. If another thread already has the lock, it is forced to wait in line. Once the thread finishes the operation, it releases the lock for the next thread. 
This ensures that the read-add-write steps become an **atomic operation**—meaning they cannot be interrupted by other threads. As proven in Part 2, the final result was exactly `400,000` because no increments were lost to collisions.

**RESULT**

python3 threads_sync.py                                                         ok | base py | at 05:00:22 PM 

=== Assignment 4: Threads & Synchronization ===

[Part 1] Running 4 threads WITHOUT synchronization...
Expected result : 400000
Actual result   : 100064
Notice the missing increments due to the Race Condition!

[Part 2] Running 4 threads WITH a Mutex (Lock)...
(Please wait a few seconds, locks make execution safer but slightly slower)
Expected result : 400000
Actual result   : 400000
Success! The Mutex protected the shared variable.
===============================================