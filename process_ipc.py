import multiprocessing
import os

def child_process_task(conn):
    # Get the Process ID (PID) of the child
    child_pid = os.getpid()
    
    # 1. Receive the data from the parent
    data = conn.recv()
    print(f"Child  [PID {child_pid}] received data: '{data}'")
    
    # 2. Transform the data (Reverse it AND make it uppercase)
    transformed_data = data.upper()[::-1]
    print(f"Child  [PID {child_pid}] processing and transforming data...")
    
    # 3. Send the transformed data back to the parent
    print(f"Child  [PID {child_pid}] sending data back to parent.")
    print() # Empty print for readability
    conn.send(transformed_data)
    
    # Close the child's end of the connection
    conn.close()

if __name__ == '__main__':
    # Get the Process ID (PID) of the parent
    parent_pid = os.getpid()
    
    print(f"\n--- Starting IPC Demonstration ---\n")
    
    # Create a Pipe for 2-way communication (duplex)
    # parent_conn is used by the parent, child_conn is used by the child
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Create the child process, passing its end of the pipe as an argument
    p = multiprocessing.Process(target=child_process_task, args=(child_conn,))
    
    print(f"Parent [PID {parent_pid}] spawning child process...")
    p.start()
    
    # Define the message to send
    original_message = "operating systems are fun"
    
    print(f"Parent [PID {parent_pid}] sending data: '{original_message}'")
    print() # Empty print for readability
    
    # Parent sends data to the child
    parent_conn.send(original_message)
    
    # Parent waits to receive the transformed data from the child
    result = parent_conn.recv()
    
    print(f"Parent [PID {parent_pid}] received final data: '{result}'")
    print() # Empty print for readability
    
    # Wait for the child process to properly terminate
    p.join()
    print(f"Parent [PID {parent_pid}] child process successfully terminated.")
    print(f"\n--- IPC Demonstration Finished ---\n")