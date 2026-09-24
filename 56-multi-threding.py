import threading
import time

# def crawl(link, delay=3):
#     print(f"crawl started for {link}")
#     time.sleep(delay) 
#     print(f"crawl ended for {link}")

# links = [
#     "https://python.org",
#     "https://docs.python.org",
#     "https://peps.python.org",
# ]

# threads = []
# for link in links:
#     t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
#     threads.append(t)


# for t in threads:
#     t.start()


# for t in threads:
#     t.join()




def add(*args):
    return args
print("The sun numbers is :", add(45 , 44 , 12))


def system_logger():
    while True:
        print("[LOG] System running smoothly...")
        time.sleep(1)

logger_thread = threading.Thread(target=system_logger, daemon=True)
logger_thread.start()
logger_thread.join()
print("Main Application Started...")
time.sleep(6)
print("Main Application Finished!")


# lient(client_id):
#     print(f"Client {client_id} connected.")
#     time.sleep(2)  
#     print(f"Client {client_id} disconnected.")


# for client_id in range(1, 4):
#     t = threading.Thread(target=handle_client, args=(client_id,))
#     t.start()



# def handle_client(client_id):
#     print(f"Client {client_id} connected.")
#     time.sleep(2)  
#     print(f"Client {client_id} disconnected.")


# for client_id in range(1, 4):
#     t = threading.Thread(target=handle_client, args=(client_id,))
#     t.start()
