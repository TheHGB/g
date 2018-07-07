import datetime

birth = raw_input("Please enter your birth date (YYYY-MM-DD)\n")

year, month, day = map(int, birth.split('-'))
birthDate = datetime.date(year, month, day)
now = datetime.datetime.now().date()

print  (now - birthDate).total_seconds()
