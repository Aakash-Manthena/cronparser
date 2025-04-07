Cron Expression Describer

It is a tool that takes a cron expression, which is a string that defines a schedule for running tasks, and converts it into a human-readable description of that schedule. 

Example:
python cron_parser.py "* * * * * /usr/bin/find"

For this input, you should then get the following output:

Minutes:      0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
Hours:        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Day of month: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Month:        1 2 3 4 5 6 7 8 9 10 11 12
Day of Week:  0 1 2 3 4 5 6
Command:      /usr/bin/find

Running the Code
This is assuming you have python 3.6 installed.

Proper syntax to use the cron parser:
python cron_parser.py "CRON_STRING"

Proper syntax to run the unit tests:
python unit_tests.py

There are 41 tests for this parser right now.

Future Development / Current Shortcomings
The following features are not yet complete in this version of the code:

The code does not change the number of days in each month. For example, February has 31 instead of 28 days.
The string format for days of the week and months of the year are case-sensitive. The actual cron spec states that this input is not case-sensitive so this needs to be altered. e.g. MON would succeed, whilst mon would not be recognised.
The special characters '?', 'L' and 'W' are not supported.
Code structure could be improved, and further exceptions could be handled specific to use case.

NOTE:
Standard practice is to create a new virtual environment for every project. I have not attached my venv in this zip folder.
