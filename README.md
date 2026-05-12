# OS_Course_2026
**Name:** DE JESUS CABRAL Ryan
**Student ID:** 64029

This repository contains assignments for the Operating Systems course.

**Assignement 1**
    ## Features
    * **OS & Kernel version** (using `uname -a`)
    * **Current user** (using `whoami`)
    * **Working directory** (using `pwd`)

    ## How to run
    ```bash
    chmod +x system_info.sh
    ./system_info.sh

**RESULT**
===================================
       System Information
===================================
OS & Kernel version : Darwin MacBook-Air-Ryan.local 25.3.0 Darwin Kernel Version 25.3.0: Wed Jan 28 20:56:34 PST 2026; root:xnu-12377.91.3~2/RELEASE_ARM64_T8112 arm64
Current User        : dejesuscabral
Working Directory   : /Users/dejesuscabral/project/ESIEE IT/RIGA/OS_RIGA/OS_Course_2026

**Assignement 2**

For this assignment, I used Python to interact with the OS file system. Here is a brief explanation of the specific libraries and functions I used and why:

* **`os.listdir(target_path)`**: I used this function to read the directory and get a list of everything inside it.
* **`os.path.isfile(filepath)`**: I used this to filter the results so the script only extracts data from actual files and ignores subdirectories.
* **`os.stat(filepath)`**: This is the main system call (similar to `stat()` in C). I used it to retrieve the file's metadata. Specifically, I used `file_stats.st_size` to get the file size in bytes.
* **`stat.filemode(st_mode)`**: Instead of printing raw permission bits, I used the `stat` library to convert the system modes into a human-readable string format (like `-rw-r--r--`).

**RESULT**

python3 file_system_info.py .                                        1 err | took 13s | base py | at 04:35:10 PM 

Listing files in: .

File Name   : file_system_info.py
Size (bytes): 1433
Permissions : -rw-r--r--

File Name   : README.md
Size (bytes): 387
Permissions : -rw-r--r--

File Name   : system_info.sh
Size (bytes): 390
Permissions : -rw-r--r--


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