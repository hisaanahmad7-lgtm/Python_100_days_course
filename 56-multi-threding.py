# import threading
# import time

# def crawl(link):
#     print(f"crawl started for {link}")
#     time.sleep(2) 
#     print(f"crawl ended for {link}")

# links = [
#     "https://python.org",
#     "https://docs.python.org",
#     "https://peps.python.org",
# ]

# threads = []
# for link in links:
#     t = threading.Thread(target=crawl, args=(link ,))
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()




# def add(*args):
#     return args
# print("The sun numbers is :", add(45 , 44 , 12))

# def system_logger():
#     while True:
#         print("[LOG] System running smoothly...")
#         time.sleep(1)

# logger_thread = threading.Thread(target=system_logger, daemon=True)
# logger_thread.start()
# print("Main Application Started...")
# time.sleep(6)
# print("Main Application Finished!")







# def handle_client(client_id):
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


# images = [
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUdq-AkHlxZ5TMi-24_3FY5sjyghkdCOqrCFoHJD85kw&s=10",
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0IF7_S3-5d_HUUod_-WjRHcTvpvvsEP35iCWtPEmgPw&s=10",
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTubeVF81Z5Ce73wysbMbRg0U3C8uFP-MQC_sWLExfWfw&s=10",
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvOpBqSLjjbVd5aoxLZm_ECBjlXZW7SFxwGAaSgLzfTg&s=10"
# ]



# def process_image(url):
#     print(f"Starting download: {url[:40]}...")
#     time.sleep(1) 
#     print(f"Finished download: {url[:40]}...")

# threads = []


# for img_url in images:
#     t = threading.Thread(target=process_image, args=(img_url,))
#     threads.append(t)


# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print("All images processed successfully!")



l1 = [
    [1,2,3,4,5],
    ["mango" , "Banana" , "Apple"],
    ["Hisaan", "Ahmad" , "Zain"]
]
for char in l1:
    print(char)


for newchar in l1:
    for mynewchar in newchar:
        print(mynewchar)
