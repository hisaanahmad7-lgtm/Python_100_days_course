import shutil
# File ka content  copy karta hai. Destination directory bhi ho sakti hai.
shutil.copyfile("34-classes.py" , "MyDownloads.py")

# File ka content aur permissions dono copy karta hai. Destination directory bhi ho sakti hai.
shutil.copy('33-is-vs-==.py', 'Downloads')


import shutil
shutil.copytree('my_project', 'project_backup')


import shutil
usage = shutil.disk_usage('/')
print(f"Free Space: {usage.free / (1024**3):.2f} GB")

import shutil
path = shutil.which('python')
print(path)

import shutil
shutil.copytree("/home/hisaan/Music/shutil", "/home/hisaan/Downloads/shutil")


import shutil
shutil.copy(
    "/home/hisaan/Documents/Python_100_days/Python Course/1st.py",
    "/home/hisaan/Downloads/PythonName.py"   # yeh folder pehle se bana hona chahiye
)



shutil.copytree(
    "/home/hisaan/Documents/Python_100_days/Python Course",
    "/home/hisaan/Downloads/MyPythonCourse"   # yeh folder pehle se bana hona chahiye
)


shutil.rmtree(
    "/home/hisaan/Downloads/MyPythonCourse"   # yeh folder pehle se bana hona chahiye
)


path = shutil.which("/home/hisaan/Documents/Python_100_days/Python Course")
print(path)
