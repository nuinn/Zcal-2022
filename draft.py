from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              #maxResults=20,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        print(events_result)

        # Prints the start and name of the next 10 events
        days = list()
        while True:
            udaytot = input("What is the maximum amount of hours your are comfortable to work in one day?")
            try:
                daytot = int(udaytot)
                break
            except:
                print("Please enter a valid number.")
                continue
        #n = 1
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            #print("\n")
            #print(n)
            #n = n + 1
            if 'attendees' in event:
                #print(start, event['summary'])
                days.append(start[0:10])
                #print(days)
            #else:
                #print("false")
        #print(start)
        daycount = dict()
        datelist = list()
#to create a histogram of lessons taught per day
#        for day in days:
#            daycount[day] = daycount.get(day,0) + 1
#        for date, hours in daycount.items():
#            if hours == daytot:
        #        print(date)







            #start = event['start'].get('dateTime', event['start'].get('date'))

            #print(start, event['summary'])

            #print(event)

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
