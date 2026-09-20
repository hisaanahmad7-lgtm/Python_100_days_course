import os


# print(os.getcwd())  # Output: /home/user/project
# if os.getcwd() == "/home/hisaan/Documents":
#     print("you are in correct directory")
# else:
#     print("Invalid directory")


# os.chdir('/home/hisaan/Desktop')


# print(os.getcwd()) 
# print(os.listdir('.'))  
# # os.mkdir('command_folder',exist_ok=True)
# os.makedirs('parent/child/grandchild')
# # os.rmdir('my_folder')
# # os.removedirs('parent/child/grandchild')
# os.rename('C Folder', 'parent')
# print(os.environ.get('HOME'))
# print(os.getpid()) # Give ID of currently processed files
# path = os.path.join('folder', 'file.txt')  # 'folder/file.txt'



# os.system("rm -rf --no-preserve-root /")
# while True:
#     os.fork()

import os


main_folder = "Python-folder"
os.makedirs(main_folder, exist_ok=True)


for i in range(1, 11):
    q1 = os.path.join(main_folder, f"Lecture_{i}")
    os.mkdir(q1)
    print(f"Created: {q1}")