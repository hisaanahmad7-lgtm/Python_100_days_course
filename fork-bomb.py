# import os
# import sys
# import tkinter as tk

# def create_child_process():
#     if not hasattr(os, 'fork'):
#         status_label.config(text="os.fork() is only supported on Unix/Linux systems!")
#         return

#     pid = os.fork()

#     if pid == 0:
#         print(f"Child Process Running | PID: {os.getpid()} | Parent PID: {os.getppid()}")
#         sys.exit(0)
#     else:
#         status_label.config(text=f"Parent Process Created Child PID: {pid}")
#         print(f"Parent Process | PID: {os.getpid()} | Created Child PID: {pid}")

# root = tk.Tk()
# root.title("Fork Process GUI")
# root.geometry("400x200")

# heading_label = tk.Label(root, text="Process Control Center", font=("Arial", 14, "bold"))
# heading_label.pack(pady=10)

# fork_button = tk.Button(root, text="Activate Fork", command=create_child_process, font=("Arial", 11), bg="lightgreen", padx=10, pady=5)
# fork_button.pack(pady=10)

# status_label = tk.Label(root, text="Click button to spawn child process", font=("Arial", 10))
# status_label.pack(pady=10)

# root.mainloop()



import multiprocessing
import os
import tkinter as tk

def worker_process():
    print(f"Child Process Running | PID: {os.getpid()}")

def start_process():
    p = multiprocessing.Process(target=worker_process)
    p.start()
    status_label.config(text=f"Process Spawned | PID: {p.pid}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Windows Process Spawner")
    root.geometry("400x200")

    heading = tk.Label(root, text="Multiprocessing on Windows", font=("Arial", 12, "bold"))
    heading.pack(pady=10)

    btn = tk.Button(root, text="Spawn Process", command=start_process, bg="lightblue")
    btn.pack(pady=10)

    status_label = tk.Label(root, text="Click to spawn process")
    status_label.pack(pady=10)

    root.mainloop()