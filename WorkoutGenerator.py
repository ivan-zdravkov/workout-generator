#!/usr/bin/env python

from calendar import monthrange

def main():
    file = parse_file('Input.txt')
    workout_plan = generate_workout_plan(file)

def generate_day_plan(exercise_groups):
    day_plan = lambda: None

    return day_plan

def generate_workout_plan(file):
    workout_days = 0
    rest_days = 0
    mode = 'workout'

    workout_plan = []

    for day in range(1, monthrange(file.year, file.month)[1] + 1):
        if mode == 'workout':
            workout_days += 1

            day_plan = generate_day_plan(file.exerciseGroups)
            day_plan.year = file.year
            day_plan.month = file.month
            day_plan.day = day

            workout_plan.append(day_plan)

            if workout_days == file.workoutDays:
                workout_days = 0
                mode = 'rest'
        else:
            rest_days += 1

            if rest_days == file.restDays:
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
    result.workoutDays = int(rows[1])
    result.restDays = int (rows[2])

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
            current_group.exercises.append(exercise)

        if i + 1 == len(rows):  # If end of file
            result.exerciseGroups.append(current_group)

        if i + 1 <= len(rows) - 1:  # If next line is '[xxx]'
            next_row = rows[i + 1]
            if next_row[0] == '[':
                result.exerciseGroups.append(current_group)

    return result

main()
