**Assignement 3**

### IPC Mechanism Chosen
For this assignment, I chose to implement a **Pipe** using Python's `multiprocessing.Pipe()` module. 

**Why is it appropriate for this task?**
A Pipe is the perfect choice for this specific task because we need direct, one-to-one, two-way (duplex) communication between exactly two processes: a single parent and a single child. 
While a Shared Queue is excellent for scenarios with multiple producers or consumers, a Pipe is much lighter, faster, and simpler to implement for strict pair communication. It creates two connection objects (endpoints), allowing the parent to easily push a string through one end, and the child to pull it from the other end, process it, and push it back through the same channel seamlessly.

**RESULT**
python3 process_ipc.py                                                             ok | base py | at 04:36:34 PM 

--- Starting IPC Demonstration ---

Parent [PID 72465] spawning child process...
Parent [PID 72465] sending data: 'operating systems are fun'

Child  [PID 72467] received data: 'operating systems are fun'
Child  [PID 72467] processing and transforming data...
Child  [PID 72467] sending data back to parent.

Parent [PID 72465] received final data: 'NUF ERA SMETSYS GNITAREPO'

Parent [PID 72465] child process successfully terminated.

--- IPC Demonstration Finished ---