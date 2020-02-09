# Generates a time stamp, and humidity percentage.
# day stamp is noted with a single digit indicating day of year
# its easier than writing a day and month formatted, and easier to reprocess
# file is attempt to write as little data as possible to file
# Data is written Hour Colon Minute Dash Humidity
# h:m:-h
# as simple as possible of course
# humidity is primary focus, temperature second.
# the two datas will be written to seperate files.
# when recording real data, humidity will be recorded on the 15 second mark,
# and temperature on the 45 second mark per minute
# averages will be reached, but the question im trying to solve is how much data is enough
# 1 minute seems good


from random import randint as ri
DAYS_IN_YEAR = 365 # just print out day of year
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

starting_humidity = 50
min_humidity = 1
max_humidity = 100

def update_humidity(current):
	# eventually this data will be generated from an actual sensor
	new = ri(current - 5, current + 5)

	# keeps humidity between range of low and high
	if new < min_humidity:
		new = min_humidity
	elif new > max_humidity:
		new = max_humidity
	return new

data_file = open("humidity_data.txt","a+")

# generate a starting humidity
humidity = update_humidity(starting_humidity)

for d in range(DAYS_IN_YEAR):

	data_file.write(f"{d}\n")

	for h in range(HOURS_IN_DAY):
		for m in range(MINUTES_IN_HOUR):

			# print(f"{h}:{m}-{humidity}")
			data_file.write(f"{h}:{m}-{humidity}\n")

			# get a new humidity
			humidity = update_humidity(humidity)

data_file.close()
