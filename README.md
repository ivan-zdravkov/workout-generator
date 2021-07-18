# Workout Generator
Workout Generator is a [Python](https://www.python.org/) workout generator I created to help me manage and generate incremental load for my workouts. 

The main goal of the application is to receive a formatted [Input.txt](https://github.com/ivan-zdravkov/workout-generator/raw/develop/Examples/Input.JPG) file, containing the year and month the workout is being created for, the number of training and rest days, as well as the workout groups and individual exercices for each group, with their initial load and incremental load for each next session. 

The parser creates the specific month's workout regimen, picking the specified number of random exercices for each work day from each workout group. The rest from the group will be scheduled for the next days, until no exercices are left in the group. Then the number of repetititons will be incremented by the provided parameter, and the rest of the month's workout sessions will be scheduled. When the workout is generated, the user will be prompted to authenticate with a google account and the workouts will be exported as [Google Calendar Events](https://github.com/ivan-zdravkov/workout-generator/raw/develop/Examples/Workout.jpg).

[Day 1](https://github.com/ivan-zdravkov/workout-generator/raw/develop/Examples/Day1.JPG)

[Day 31](https://github.com/ivan-zdravkov/workout-generator/raw/develop/Examples/Day31.JPG)

## Setup
* Install [Python 3.6.2](https://www.python.org/downloads/)
* Edit the Input.txt file in the repository to match your workout preferences
* Open a Command Prompt window, navigate to the Repository directory and execute the Python script > "python WorkoutGenerator.py" 
* [Optional] If you have not yet used the application, your default browser will open and you will be promted to authenticate using a Google account. Your events will then be created to this Google account's calendar.
* The "Google Calendar Events successfully generated..." message will be printed on the console after the Events are created.

## Notes
* Try not to execute the application multiple times for a single month, or you will end up with duplicate Events on your Calendar as did I, while testing.
