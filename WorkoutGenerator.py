#!/usr/bin/env python

def main():
    file = parse_file('Input.txt')

    exercise_groups = file.exerciseGroups

def parse_file(name):
    with open(name) as f:
        rows = f.readlines()

    rows = [x.strip() for x in rows]  # Remove white space, /n
    rows = [x for x in rows if x]  # Remove empty rows

    current_group = lambda: None
    result = lambda: None
    result.exerciseGroups = []
    result.workoutDays = rows[0]
    result.restDays = rows[1]

    for i in range(2, len(rows)):
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
