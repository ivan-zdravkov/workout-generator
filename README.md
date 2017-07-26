#Workout Generator

Workout Generator is a [Python](https://www.python.org/) workout generator I created to help me manage and generate incremental load for my workouts. The main goal of the application is to receive a formatted "Input.txt" file, containing the month the workout is being created for, the number of training and rest days, as well as the workout groups and individual exercices for each group, with their initial load and incremental load for each next session. The parser will then create the specific month's workout regimen, picking 2 random exercices for each work day from yeach workout group. The rest from the group will be scheduled for the next days, until no exercices are left. Then the number of repetititons will be incremented by the provided parameter, and the rest of the month's workout sessions will be scheduled. When the workout is generated, an option will be presented to download the workout or upload it as Google Calendar Events (a gmail account and password will have to be provided for that)

## Setup
* [Python 3.6.2](https://www.python.org/downloads/)
* Input.txt file example is provided in the repository and must be placed in the same directory as the WorkoutGenerator.py file
