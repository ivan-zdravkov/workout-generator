#Workout Generator

Workout Generator is a [Python](https://www.python.org/) workout generator I created to help me manage and generate incremental load for my workouts. 

The main goal of the application is to receive a formatted [Input.txt](https://bytebucket.org/workoutgeneratorteam/workout-generator/raw/5e3787028d77477c9244ce50acf1182093375383/Examples/Input.JPG) file, containing the year and month the workout is being created for, the number of training and rest days, as well as the workout groups and individual exercices for each group, with their initial load and incremental load for each next session. 

The parser creates the specific month's workout regimen, picking the specified number of random exercices for each work day from each workout group. The rest from the group will be scheduled for the next days, until no exercices are left in the group. Then the number of repetititons will be incremented by the provided parameter, and the rest of the month's workout sessions will be scheduled. When the workout is generated, the user will be prompted to authenticate with a google account and the workouts will be exported as [Google Calendar Events](https://bytebucket.org/workoutgeneratorteam/workout-generator/raw/5e3787028d77477c9244ce50acf1182093375383/Examples/Workout.jpg).

[Day 1](https://bytebucket.org/workoutgeneratorteam/workout-generator/raw/5e3787028d77477c9244ce50acf1182093375383/Examples/Day1.JPG)

[Day 31](https://bytebucket.org/workoutgeneratorteam/workout-generator/raw/5e3787028d77477c9244ce50acf1182093375383/Examples/Day31.JPG)

## Setup
* [Python 3.6.2](https://www.python.org/downloads/)
* Input.txt file example is provided in the repository and must be placed in the same directory as the WorkoutGenerator.py file