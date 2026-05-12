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