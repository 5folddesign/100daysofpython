#python3
#climbing_record.py is a script to record the grades, and perceived rate of exertion during an indoor rock climbing session.


# I want this script to record: the number of the climb, wall type, grade of climb, perceived rate of exertion on my body, perceived rate of exertion on my heart, and the date and time of the climbing session. I then want all of this information to be added to a .csv file


import csv
#import the datetime library.
csvFile = open('/Users/laptop/github/100daysofpython/day_001/climbinglog.csv','a',newline='')
csvWriter = csv.writer(csvFile,delimiter=',',lineterminator='\n\n')
#add functions for each question.
climb_number = ''
wall_type = ''
grade = ''
pre_heart = ''
pre_body = ''


def climbNumber():
    climb_number = input("What number route is this? /n > ")
    answer_string = str(climb_number)
    if str.isnumeric(answer_string):
        break
    else:
        print("You must enter a number. Try again.  ")
        climbNumber()


def wallType():
    wall_type = input("What type of wall was the route on?  ")
    while wall_type:
        #if there is text in the input,instead of an alphanumeric, then tell them they must put in a number.
        if str.isalpha(wall_type):
            return wall_type
        else:
            print("You entered a number, you must enter a word. Try again.  ")
            wallType()


def grade():
    grade = input("What was the grade of the route?")
    answer_string = str(grade)
    while grade:
        #if there is text in the input,instead of an alphanumeric, then tell them they must put in a number.
        if answer_string:
            break
        else:
            print("You must enter a number. Try again.  ")
            grade()


def preBody():
    pre_body = input("On a scale of 1-10, how difficult did this route feel on your body?")
    answer_string = str(pre_body)
    while pre_body:
        #if there is text in the input,instead of an alphanumeric, then tell them they must put in a number.
        if str.isnumeric(answer_string):
            break
        else:
            print("You must enter a number. Try again.  ")
            preBody()


def preHeart():
    pre_heart = input("On a scale of 1-10, how difficult did this route feel on your heart?")
    answer_string = str(pre_heart)
    while pre_heart:
        #if there is text in the input,instead of an alphanumeric, then tell them they must put in a number.
        if str.isnumeric(answer_string):
            break
        else:
            print("You must enter a number. Try again.  ")
            preHeart()

climbNumber()
wallType()
grade()
preBody()
preHeart()

csvWriter.writerow([climb_number,wall_type,grade,pre_body,pre_heart])
