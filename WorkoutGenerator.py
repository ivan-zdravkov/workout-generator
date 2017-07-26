#!/usr/bin/env python

with open('Input.txt') as f:
    inputRows = f.readlines()

inputRows = [x.strip() for x in inputRows]  # Remove white space, /n
inputRows = [x for x in inputRows if x]  # Remove empty rows

exerciseGroups = []
workoutDays = inputRows[0]
restDays = inputRows[1]

rowsToIterate = range(2, len(inputRows))
currentGroup = lambda: None

for i in rowsToIterate:
    currentRow = inputRows[i]

    if currentRow[0] == '[':  # If name of exercise group
        currentGroup = lambda: None
        currentGroup.name = currentRow[1:len(currentRow) - 1]
        currentGroup.exercises = []
    else:
        parsedCurrentRow = [x.strip() for x in currentRow.split(',', 2)]
        exercise = lambda: None
        exercise.name = parsedCurrentRow[0]
        exercise.repetitions = int(parsedCurrentRow[1])
        exercise.increment = int(parsedCurrentRow[2])
        currentGroup.exercises.append(exercise)

    if i + 1 == len(inputRows):  # If end of file
        exerciseGroups.append(currentGroup)

    if i + 1 <= len(inputRows) - 1:  # If next line is '[xxx]'
        nextRow = inputRows[i + 1]
        if nextRow[0] == '[':
            exerciseGroups.append(currentGroup)
