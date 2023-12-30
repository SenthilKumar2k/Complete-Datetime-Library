import time

current_time=time.time()
print(current_time)
localtime_string=time.ctime(current_time)
print(localtime_string)
localtime_struct=time.localtime(current_time)
print(localtime_struct)
localtime_format=time.strftime("%Y-%B-%A  %I:%M:%S", localtime_struct)
print(localtime_format)
time.sleep(2)
print("sleep for 2 seconds")