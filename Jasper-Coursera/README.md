Jasper-Coursera
===============

Jasper Module based on Coursera public API

### Adding the module to Jasper
First, copy over coursera.py to client/modules folder. 

### Adding Coursera notifications to Jasper
Use the following code to create a new function in notifier.py of Jasper Client and use it to create a new NotificationClient.

```
def handleCourseraNotifications(self, latest):
    from modules import Coursera
    from datetime import date, datetime
    if latest == date.today():
        return latest
    else if datetime.now().hour < 10:
        return latest
    
    sessions_next_week = Coursera.fetchSessionsCount(self.profile, date.today(), 7)
    
    def styleCourse(count):
        return "%s courses starting in the next week." % count
    
    self.q.put(styleCourse(sessions_next_week))
    return date.today()

# Append the new Notification function to Notifiers list like,
self.notifiers = [self.NotificationClient(self.handleCourseraNotifications, None)]

```

### More Interaction with Coursera
Coming up!
