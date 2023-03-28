time = input().split(" ")
hour = int(time[0])
minute = int(time[1])
hour %= 12
if time[2] == "pm":
    hour += 12

print(str(hour).rjust(2, "0") + ":" + str(minute).rjust(2, "0"))