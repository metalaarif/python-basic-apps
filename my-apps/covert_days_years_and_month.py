DAYS_IN_WEEK = 7

def find(number_of_days):

    year = int (number_of_days / 365)
    week = int ((number_of_days % 365) /
                DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK

    print ("years = ", year,
           "\nweeks = ", week,
           "\ndays = ", days)

number_of_days = 10096
find (number_of_days)