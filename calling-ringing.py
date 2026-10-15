import time
import sys
import socket
# user_input = input("Enter your command : ")
# try:
#     if user_input.lower().strip() == "calling":
#         print("Calling", end="")
#         for _ in range(3):
#             time.sleep(0.5)
#             print(".", end="", flush=True)
#             # print()
#     elif user_input.lower().strip() == "ringing":
#         print("Ringing", end="")
#         for _ in range(3):
#             time.sleep(0.5)
#             print(".", end="", flush=True)
#     else:
#         raise ValueError("Incorrect value bro, Try again...")
# except Exception as e:
#     print(e)


import socket
import sys
import time


def check_internet():
  """Internet connection checking function"""
  try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
    return True
  except OSError:
    return False


def show_animation(text):
  """Dots animation  function"""
  print(text, end="")
  for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
  print()


def main():
  user_input = input("Enter your command (calling/ringing) : ").lower().strip()

  try:
    print("Checking network", end="")
    for _ in range(3):
      time.sleep(0.3)
      print(".", end="", flush=True)
    print()

    if not check_internet():
      raise ConnectionError(
          "Internet connection unavailable!."
      )

    
    if user_input == "calling":
      show_animation("Calling")
      time.sleep(1) 
      show_animation("Ringing")
    elif user_input == "ringing":
      show_animation("Ringing")
    else:
      raise ValueError("Incorrect value , 'calling' or 'ringing'...")

  except Exception as e:
    print(f"\n[Error]: {e}")


if __name__ == "__main__":
  main()