import datetime

def enteredMonth():
    month = int(input("Enter a month in terms of a number: "))
    return month

def enteredYear():
    year = int(input("Enter a year: "))
    return year

def numberOfDays(year, month):
    first_of_entered_month = datetime.date(year, month, 1)
    someday_next_month = first_of_entered_month + datetime.timedelta(days=31)
    first_of_next_month = someday_next_month.replace(day=1)
    last_of_entered_month = first_of_next_month - datetime.timedelta(days=1)
    return last_of_entered_month.day

def main():
    month = enteredMonth()
    year = enteredYear()
    number_of_days = numberOfDays(year, month)
    pretty_month_year = datetime.date(year, month, 1).strftime('%B %Y')
    print(pretty_month_year, "has", number_of_days, "days")

main()