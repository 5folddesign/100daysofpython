#python3
#climbing_record.py is a script to record the grades, and perceived rate of exertion during an indoor rock climbing session.


# I want this script to record: the number of the climb, wall type, grade of climb, perceived rate of exertion on my body, perceived rate of exertion on my heart, and the date and time of the climbing session. I then want all of this information to be added to a .csv file


import csv
csvFile = open('climbinglog.csv','a',newline='')  # Opens a file in write mode
csvWriter = csv.writer(csvFile,delimiter=',',lineterminator='\n\n')  # Creates a Writer object

climb_number = ''
wall_type = ''
grade = ''
pre_heart = ''
pre_body = ''

def climbNumber():
    climb_number = input("What number is this climb? \n")
    while climb_number.isnumeric():
        break
    else:
        print("You must enter a number. Try again.")
        climbNumber()

def wallType():
    wall_type = input("What type of wall was the route on? \n")
    while wall_type.isalpha():
        break
    else:
        print("You entered a number, you must enter a word. Try again.")
        wallType()

def grade_():
    grade = input("What was the grade of the route? \n")
    while grade.isnumeric():
        break
    else:
        print("You must enter a number. Try again.")
        grade_()

def preBody():
    pre_body = input("On a scale of 1-10, how difficult did this route feel on your body? \n")
    while pre_body.isnumeric():
        break
    else:
        print("You must enter a number. Try again.")
        preBody()

def preHeart():
    pre_heart = input("On a scale of 1-10, how difficult did this route feel on your heart? \n")
    while pre_heart.isnumeric():
        break
    else:
        print("You must enter a number. Try again.")
        preHeart()

climbNumber()
wallType()
grade_()
preBody()
preHeart()

csvWriter.writerow([climb_number, wall_type, grade, pre_body, pre_heart])
csvFile.close()
