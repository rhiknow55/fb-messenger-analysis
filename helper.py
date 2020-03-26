from datetime import datetime
from datetime import timedelta
import pytz

starting_date = datetime(2019, 3, 26).astimezone(pytz.timezone('US/Pacific'))


# Return number of days
def days_since_start(timestamp):
    timestamp = timestamp / 1000

    utc_dt = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    pst_dt = utc_dt.astimezone(pytz.timezone('US/Pacific'))

    test = pst_dt - starting_date

    days = test.days

    return days

# Return the date time
def formatday(days):
    dt = starting_date + timedelta(days)

    date_format='%m/%d/%Y'

    return dt.strftime(date_format)

# Return the datetime "days" from the starting date
def formatdatetime(days):
    return starting_date + timedelta(days)
