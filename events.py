from gcsa.google_calendar import GoogleCalendar
from gcsa.attendee import Attendee
import gcsa.event

calendar = GoogleCalendar('marc.teachify@gmail.com')


att = list()
for event in calendar:
    print(event)
    for attendee in event:
        att[attend] = att.get(attend,0) + 1
