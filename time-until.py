#!/usr/bin/python

import datetime
import sys

date = sys.argv[1]
event = sys.argv[2]

dateformat = '%Y-%m-%d'

future = datetime.datetime.strptime(date, dateformat)
now = datetime.datetime.now()

diff = future - now
print type(diff)

timeuntil = ''
if diff.days:
    timeuntil = '%sd ' % diff.days
if diff.seconds:
    seconds = diff.seconds
    hours = minutes = 0

    if seconds >= 3600:
        hours = seconds / 3600
        seconds -= 3600 * hours
    if seconds >= 60:
        minutes = seconds / 60
        seconds -= 60 * minutes

    timeuntil = '%s%sh %sm %ss' % (timeuntil, hours, minutes, seconds)
print 'Time until %s: %s' %(event, timeuntil)
