# returns a copy of string_to_pare where the longest matching prefix is removed
def pare_string_prefix(list_of_prefixes, string_to_pare):
	list_of_prefixes = sorted(list_of_prefixes, key=lambda prefix: len(prefix), reverse=True)
	s_len = len(string_to_pare)
	for prefix in list_of_prefixes:
		p_len = len(prefix)
		if s_len >= p_len and string_to_pare[0:p_len] == prefix:
			return string_to_pare[p_len:]			


MONDAY = 2**0
TUESDAY = 2**1
WEDNESDAY = 2**2
THURSDAY = 2**3
FRIDAY = 2**4
SATURDAY = 2**5
SUNDAY = 2**6

selected_days_of_week = 0
selected_time = 0

availability_list = [ 0 for i in range(7) ]

DAY_MODE = 0
TIME_MODE = 1
mode = DAY_MODE

availability_string = input().lower()

# mark selected days of week
while(len(availability_string) > 0 and mode == DAY_MODE):
	# M, Mon, Monday
	if availability_string[0] == 'm':
		selected_days_of_week |= MONDAY
		availability_string = pare_string_prefix(["monday", "mon", "m"], availability_string)
		continue
	# T, Tue, Tuesday
	if availability_string[0] == 't' and not (len(availability_string) >= 2 and availability_string[1] == 'h'):
		selected_days_of_week |= TUESDAY
		availability_string = pare_string_prefix(["tuesday", "tue", "t"], availability_string)
		continue
	# W, Wed, Wednesday
	if availability_string[0] == 'w':
		selected_days_of_week |= WEDNESDAY
		availability_string = pare_string_prefix(["wednesday", "wed", "w"], availability_string)
		continue
	# R, Th, Thurs, Thursday
	if availability_string[0] == 'r' or (len(availability_string) >= 2 and availability_string[0:2] == "th") :
		selected_days_of_week |= THURSDAY
		availability_string = pare_string_prefix(["thursday", "thurs", "th", "r"], availability_string)
		continue
	# F, Fri, Friday
	if availability_string[0] == 'f':
		selected_days_of_week |= FRIDAY
		availability_string = pare_string_prefix(["friday", "fri", "f"], availability_string)
		continue
	# Sat, Saturday
	if len(availability_string) >= 3 and availability_string[0:3] == "sat":
		selected_days_of_week |= SATURDAY
		availability_string = pare_string_prefix(["saturday", "sat"], availability_string)
		continue
	# Sun, Sunday
	if len(availability_string) >= 3 and availability_string[0:3] == "sun":
		selected_days_of_week |= SUNDAY
		availability_string = pare_string_prefix(["sunday", "sun"], availability_string)
		continue
	
	# !!! <--------------------------- TODO: add functionality to track ranges of days i.e. M-F 
	
	
	# check if number, then grab time / time range
