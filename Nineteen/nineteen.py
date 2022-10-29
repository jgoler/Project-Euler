days_in_months = {
	"jan": 31,
	"feb": 28,
	"mar": 31,
	"apr": 30,
	"may": 31,
	"jun": 30,
	"jul": 31,
	"aug": 31,
	"sep": 30,
	"oct": 31,
	"nov": 30,
	"dec": 31
}
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
days_of_week = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
cur_year = 1900
day_of_month = 1
cur_day_of_week = days_of_week[0]
month = months[0]
sundays_on_first = 0

days = 36524
for i in range(days):
	

	# move to next day of week
	if (cur_day_of_week == "sun"):
		cur_day_of_week = "mon"
	else:
		cur_day_of_week = days_of_week[days_of_week.index(cur_day_of_week) + 1]

    # move to next day of month, month, and year
	if (month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec") and (day_of_month < 31):
		day_of_month += 1
	elif ((month == "apr" or month == "jun" or month == "sep" or month == "nov") and (day_of_month < 30)):
		day_of_month += 1
	elif (month == "feb" and (cur_year % 4 == 0 and cur_year % 400 != 0)):
		if (day_of_month < 29):
			day_of_month += 1
		else:
			day_of_month = 1
			month = "mar"
	elif (month == "feb" and (cur_year % 4 == 0)):
		if (day_of_month < 28):
			day_of_month += 1
		else:
			day_of_month = 1
			month = "mar"
	else:
		day_of_month = 1
		if (month == "dec"):
			month = "jan"
			cur_year += 1
		else:
			month = months[months.index(month) + 1]

	if (cur_day_of_week == "sun" and day_of_month == 1 and cur_year > 1900 and cur_year < 2001):
		sundays_on_first += 1
		print(str(cur_day_of_week) + ", " + str(day_of_month) + ", " + str(month) + ", " + str(cur_year))

print(sundays_on_first)

#solution is 171
#can also use the datetime module and make it ~10 lines



