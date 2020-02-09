from random import randint as ri
DAYS_IN_YEAR = 365 # just print out day of year
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

starting_humidity = 50
min_humidity = 1
max_humidity = 100

def update_humidity(current):
	new = ri(current - 5, current + 5)

	if new < min_humidity:
		new = min_humidity
	elif new > max_humidity:
		new = max_humidity
	return new

data_file = open("humidity_data.txt","a+")


humidity = update_humidity(starting_humidity)

for d in range(DAYS_IN_YEAR):
	# print(d)
	data_file.write(f"{d}\n")

	for h in range(HOURS_IN_DAY):
		for m in range(MINUTES_IN_HOUR):

			# print(f"{h}:{m}-{humidity}")
			data_file.write(f"{h}:{m}-{humidity}\n")

			humidity = update_humidity(humidity)

data_file.close()
