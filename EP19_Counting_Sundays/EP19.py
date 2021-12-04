# Project Euler problem #19
# 2021/11/26
# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

class Date:
    """Class to handle Date objects"""
    max_day = {
        30: [9, 4, 6, 11],
        31: [1, 3, 5, 7, 8, 10, 12],
        29: [2]
    }

    reference_date = {
        "year": 1900,
        "month": 1,
        "day": 1,
        "weekday": 1
    }

    weekday_names = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun",
    }

    def __init__(self, year, month, day, weekday):
        """Year is a four digit integer, month is a integer from 1 - 12, day is an integer from 1 - 31, depending on the month and year.
        Weekday is an integer from 1 - 7 representing the day of the week (Monday = 1)"""
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday

    @staticmethod
    def get_ref_date():
        """Returns a Date object containing the reference date (Mon 1900/01/01). This date was a Monday"""
        return Date(1900, 1, 1, 1)

    @staticmethod
    def is_valid_date(year, month, day):
        """Returns True if the given date is a valid date"""
        pass

    @staticmethod
    def is_leap_year(year):
        """Returns true if the given year is a leap year"""
        # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

        # Test for centuries
        if year % 400 == 0:
            return True

        # Test for other leap years
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False


    def next_day(self):
        """Returns the next date (one day) after the current date. Returns a Date object"""

        # For feb 29
        if Date.is_leap_year(self.year) and self.month == 2 and self.day == 28:
            return Date(self.year, self.month, self.day + 1, self.get_next_weekday())
        if not(Date.is_leap_year(self.year)) and self.month == 2 and self.day == 28:
            return Date(self.year, self.month + 1, 1, self.get_next_weekday())
        if Date.is_leap_year(self.year) and self.month == 2 and self.day == 29:
            return Date(self.year, self.month + 1, 1, self.get_next_weekday())

        # For months with 30 days
        if self.month in Date.max_day[30] and self.day >= 28 and self.day < 30:
            return Date(self.year, self.month, self.day + 1, self.get_next_weekday())
        if self.month in Date.max_day[30] and self.day == 30:
            return Date(self.year, self.month + 1, 1, self.get_next_weekday())

        # For months with 31 days, except December
        if self.month in Date.max_day[31] and self.day >= 28 and self.day < 31 and self.month != 12:
            return Date(self.year, self.month, self.day + 1, self.get_next_weekday())
        if self.month in Date.max_day[31] and self.day == 31 and self.month != 12:
            return Date(self.year, self.month + 1, 1, self.get_next_weekday())

        # For December:
        if self.month == 12 and self.day >= 28 and self.day <= 30:
            return Date(self.year, self.month, self.day + 1, self.get_next_weekday())
        if self.month == 12 and self.day == 31:
            return Date(self.year + 1, 1, 1, self.get_next_weekday())

        # For days 1 - 27 of any month:
        if self.day > 0 and self.day < 28:
            return Date(self.year, self.month, self.day + 1, self.get_next_weekday())

    def get_weekday_name(self):
        """Return the weekday name corresponding the to weekday number (1 - 7)"""
        return Date.weekday_names[self.weekday]

    def is_weekday(self, weekday_number):
        """Returns true if the weekday of the current instance is the same as weekday_number"""
        return self.weekday == weekday_number

    def is_day(self, day_number):
        """Returns true if the day of the current instance is the same as day_number"""
        return self.day == day_number

    def get_next_weekday(self):
        """Return an integer from 1 - 7 representing the next weekday (next day)"""
        if self.weekday > 0 and self.weekday < 7:
            return self.weekday + 1
        else:
            return 1

    @property
    def get_date_string(self):
        """Returns a string version of the date"""
        weekday_name = self.get_weekday_name()
        return "{}, {}/{}/{}".format(weekday_name, self.year, self.month, self.day)

# Test next_day function
#date = Date(2000, 11, 20)
#next_day = Date.get_ref_date()

# Using the next_day function, it was calculated that 1901/1/1 was a Tuesday
days = []
next_day = Date(1901, 1, 1, 2)
days.append([next_day.get_date_string, next_day.is_weekday(7), next_day.is_day(1)])
# print(next_day.get_date_string)
#next_day = ref.next_day()
for i in range(36524):
    next_day = next_day.next_day()
    days.append([next_day.get_date_string, next_day.is_weekday(7), next_day.is_day(1)])
    # print(next_day.get_date_string)
#print(days)

# Count the number of Sundays falling on the first of the month
sunday_first_count = 0
for day in days:
    if day[1] == True and day[2] == True:
        sunday_first_count += 1
print("Sundays falling on the first:", sunday_first_count)

# Test is_leap_year
# years = []
# for year in range(1900, 2001):
#     years.append([year, Date.is_leap_year(year)])
# print(years)

# Resources
# 01 https://www.timeanddate.com/date/weekday.html?day=29&month=2&year=1900

