# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
#
# Your task is to make 'Past' function which returns time converted to miliseconds.
#
# #####Example:
#
# past(0, 1, 1) == 61000
# Note! h, m and s will be only Natural numbers! Waiting for translations and Feedback! Thanks!
import datetime


def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000


def past_using_datetime(h, m, s):
    time = datetime.time(h, m, s)
    time_in_seconds = datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second).total_seconds()
    time_in_miliseconds = time_in_seconds * 1000
    return time_in_miliseconds

