import time
timestamp = time.strftime('%H')
name = input("Enter your name: ")
if int(timestamp) >= 0 and int(timestamp) < 12:
  print("Good Morning", name)
elif int(timestamp) >=12 and int(timestamp) <17:
    print("Good Afternoon", name)
elif int(timestamp) >=17 and int(timestamp) <(20):
    print("Good Evening", name)
elif int(timestamp) >=(20) and int(timestamp) <(24):
    print("Good Night", name)