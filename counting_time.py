hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutes = mins + dura
hour += minutes // 60
minutes = minutes % 60
hour = hour % 24

print(f"{hour}:{minutes}")