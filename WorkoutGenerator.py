#!/usr/bin/env python

import httplib2
import argparse
import datetime
import sys
import os

from calendar import monthrange
from random import shuffle

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

print('Application is running...')

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Workout Planner'

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def main():
    try:
        file = parse_file('Input.txt')
        print('File successfully parsed...')
    except:
        print('File could not be parsed...')
        return

    try:
        workout_plan = generate_workout_plan(file)
        print('Workout successfully generated...')
    except:
        print('Workout could not be generated...')
        return

    try:
        create_google_calendar_events(workout_plan)
        print('Google Calendar Events successfully generated...')
    except:
        print('Google Calendar Events could not be generated...')
        return


def create_google_calendar_events(workout_plan):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    current = 0

    for workout in workout_plan:
        current += 1
        description = ''

        for exercise in workout.exercises:
            description += exercise.name + ' - ' + str(exercise.repetitions) + '\n'

        date = str(workout.year) + '-' + str(workout.month) + '-' + str(workout.day)

        event = {
            'summary': 'Workout',
            'description': description,
            'start': {
                'dateTime': date + 'T08:00:00+03:00',
                'timeZone': 'Europe/Sofia',
            },
            'end': {
                'dateTime': date + 'T08:30:00+03:00',
                'timeZone': 'Europe/Sofia',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        service.events().insert(calendarId='primary', body=event).execute()

        print(str(int(current / len(workout_plan) * 100)) + '% complete.')


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def generate_day_plan(exercise_groups, number_of_exercises):
    day_plan = lambda: None
    day_plan.exercises = []

    for i in range(0, number_of_exercises):
        shuffle(exercise_groups)

        for exercise_group in exercise_groups:
            not_done_exercises = list(x for x in exercise_group.exercises if x.alreadyUsed is False)

            if not not_done_exercises :
                for exercise in exercise_group.exercises:
                    exercise.repetitions += exercise.increment
                    exercise.alreadyUsed = False

                not_done_exercises = list(x for x in exercise_group.exercises if x.alreadyUsed is False)

            shuffle(not_done_exercises)

            exercise = not_done_exercises[0]
            exercise.alreadyUsed = True

            exerciseToAdd = lambda: None
            exerciseToAdd.name = exercise.name
            exerciseToAdd.repetitions = exercise.repetitions

            day_plan.exercises.append(exerciseToAdd)

    return day_plan


def generate_workout_plan(file):
    workout_days = 0
    rest_days = 0
    mode = 'workout'

    workout_plan = []

    for day in range(1, monthrange(file.year, file.month)[1] + 1):
        if mode == 'workout':
            workout_days += 1

            day_plan = generate_day_plan(file.exerciseGroups, file.numberOfExercises)
            day_plan.year = file.year
            day_plan.month = file.month
            day_plan.day = day

            workout_plan.append(day_plan)

            if workout_days >= file.workoutDays:
                workout_days = 0
                mode = 'rest'
        else:
            rest_days += 1

            if rest_days >= file.restDays:
                rest_days = 0
                mode = 'workout'

    return workout_plan


def parse_file(name):
    with open(name) as f:
        rows = f.readlines()

    rows = [x.strip() for x in rows]  # Remove white space, /n
    rows = [x for x in rows if x]  # Remove empty rows

    current_group = lambda: None
    result = lambda: None
    result.exerciseGroups = []
    result.year = int(rows[0].split(',', 1)[0])
    result.month = int(rows[0].split(',', 1)[1])
    result.workoutDays = int(int(rows[1].split(',', 1)[0]))
    result.restDays = int(int(rows[1].split(',', 1)[1]))
    result.numberOfExercises = int(rows[2])

    for i in range(3, len(rows)):
        row = rows[i]

        if row[0] == '[':  # If name of exercise group
            current_group = lambda: None
            current_group.name = row[1:len(row) - 1]
            current_group.exercises = []
        else:
            parsed_row = [x.strip() for x in row.split(',', 2)]  # Get the 3 comma separated values and trim them
            exercise = lambda: None
            exercise.name = parsed_row[0]
            exercise.repetitions = int(parsed_row[1])
            exercise.increment = int(parsed_row[2])
            exercise.alreadyUsed = False
            current_group.exercises.append(exercise)

        if i + 1 == len(rows):  # If end of file
            result.exerciseGroups.append(current_group)

        if i + 1 <= len(rows) - 1:  # If next line is '[xxx]'
            next_row = rows[i + 1]
            if next_row[0] == '[':
                result.exerciseGroups.append(current_group)

    return result

main()

print("Exiting Application...")
