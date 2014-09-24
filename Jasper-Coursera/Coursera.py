#!/bin/bash/env python

# Copyright: 2014 Ashish Sharma, Nextcraft
# License: MIT License, see ./LICENSE.txt for details.

"""
    Jasper Coursera Module
    
    The module provides data notifications and interactions sourced from Coursera's Public APIs.

"""

import json
import sys
import urllib2
import os
import bisect
from datetime import date, timedelta

# Get $JASPER_HOME
jasper_home = os.getenv("JASPER_HOME")

# Set coursera open api base url
coursera_api_base_url = 'https://api.coursera.org/api/catalog.v1/'

def fetchSessionsCount(profile, since=date.today(), period=7):
    return len(fetchSessions(profile, since, period))

def fetchSessions(profile, since=date.today(), period=7):
    data = None
    try:
        f = urllib2.urlopen(coursera_api_base_url + 'sessions?fields=startDay,startMonth,startYear&includes=courses')
        data = json.loads(f.read())
    except Exception as e:
        print 'Error occured while accessing Coursera API'
        data = {'elements':[]}

    courses = []
    for element in data['elements']:
        if 'startDay' in element and 'startMonth' in element and 'startYear' in element:
            courses.append({'course': element['links']['courses'][0], 'start': date(element['startYear'], element['startMonth'], element['startDay'])})
        else:
            continue

    courses = sorted(courses, key=lambda course: course['start'])

    courses_keys = [r['start'] for r in courses]
    i = bisect.bisect_left(courses_keys, since)
    j = bisect.bisect_right(courses_keys, since + timedelta(days=period))

    return courses[i:j]

if __name__ == '__main__':
    print fetchSessionsCount(None)
