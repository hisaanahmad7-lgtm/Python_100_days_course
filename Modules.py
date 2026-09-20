
import os
import random
import calendar
import time

print(time.time())

text = "Hy ! My Name is Hisaan ahmad and i Love Python Language"
print(text)

encoded_text = text.encode()


current_directory = os.getcwd()
print(current_directory)

directory_contents = os.listdir(current_directory)
print(directory_contents)

process_id = os.getpid()
print(process_id)

environment_path = os.getenv("PATH")
print(environment_path)

is_file_exists = os.path.exists("test.txt")
print(is_file_exists)

random_int = random.randint(1, 100)
print(random_int)

random_float = random.random()
print(random_float)

sample_list = ["Python", "FastAPI", "Linux", "Robotics", "AI"]
random_choice = random.choice(sample_list)
print(random_choice)

random.shuffle(sample_list)
print(sample_list)

random_samples = random.sample(range(1, 1000), 5)
print(random_samples)

current_year = 2026
current_month = 9
lendar.monthcalendar(current_year, current_month)
print(calendar_matrix)
month_calendar = calendar.month(current_year, current_month)
print(month_calendar)

is_leap = calendar.isleap(current_year)
print(is_leap)

leap_years_count = calendar.leapdays(2000, 2030)
print(leap_years_count)

month_days = calendar.monthrange(current_year, current_month)
print(month_days)

calendar_matrix = calendar.monthcalendar(current_year, current_month)
print(calendar_matrix)

epoch_time = time.time()
print(epoch_time)

formatted_time = time.ctime(epoch_time)
print(formatted_time)

time_struct = time.localtime(epoch_time)
print(time_struct)

year = time_struct.tm_year
month = time_struct.tm_mon
day = time_struct.tm_mday
hour = time_struct.tm_hour
minute = time_struct.tm_min
second = time_struct.tm_sec

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)

time.sleep(0.5)

end_time = time.time()
execution_time = end_time - epoch_time
print(execution_time)

combined_data = f"{text}{random_int}{epoch_time}"
combined_hash = hashlib.sha256(combined_data.encode()).hexdigest()
print(combined_data)
print(combined_hash)
