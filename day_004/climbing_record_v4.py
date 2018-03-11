#python3
#climbing_record.py is a script to record the grades, and perceived rate of exertion during an indoor rock climbing session.


# I want this script to record: the number of the climb, wall type, grade of climb, perceived rate of exertion on my body, perceived rate of exertion on my heart, and the date and time of the climbing session. I then want all of this information to be added to a .csv file


import csv
#import the datetime library.
csvFile = open('/Users/laptop/github/100daysofpython/day_004/climbinglog.csv','a',newline='')
csvWriter = csv.writer(csvFile,delimiter=',',lineterminator='\n\n')
#add functions for each question.
climb_number =''
wall_type = ''
grade = ''
pre_heart = ''
pre_body = ''


def climbNumber():
    global climb_number
    climb_number = input("What number route is this? \n > ")
    answer_string = str(climb_number)

    if str.isnumeric(answer_string):
        pass
    else:
        print("You must enter a number. Try again.  ")
        climbNumber()


def wallType():
    global wall_type
    wall_type = input("What type of wall was the route on?  \n >")
    if str.isalpha(wall_type):
        pass
    else:
        print("You entered a number, you must enter a word. Try again.  ")
        wallType()


def grade():
    global grade
    grade = input("What was the grade of the route? \n >")
    answer_string = str(grade)
    if answer_string:
        pass
    else:
        print("You must enter a number. Try again.  ")
        grade()


def preBody():
    global pre_body
    pre_body = input("On a scale of 1-10, how difficult did this route feel on your body? \n >")
    answer_string = str(pre_body)
    if str.isnumeric(answer_string):
        pass
    else:
        print("You must enter a number. Try again.  ")
        preBody()


def preHeart():
    global pre_heart
    pre_heart = input("On a scale of 1-10, how difficult did this route feel on your heart? \n >")
    answer_string = str(pre_heart)
    if str.isnumeric(answer_string):
        pass
    else:
        print("You must enter a number. Try again.  ")
        preHeart()

climbNumber()
wallType()
grade()
preBody()
preHeart()

csvWriter.writerow([climb_number,wall_type,grade,pre_body,pre_heart])
