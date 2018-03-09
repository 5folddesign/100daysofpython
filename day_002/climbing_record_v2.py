#python3
#climbing_record.py is a script to record the grades, and perceived rate of exertion during an indoor rock climbing session.


# I want this script to record: the number of the climb, wall type, grade of climb, perceived rate of exertion on my body, perceived rate of exertion on my heart, and the date and time of the climbing session. I then want all of this information to be added to a .csv file


import csv
#import the datetime library.
csvFile = open('/Users/laptop/github/100daysofpython/day_001/climbinglog.csv','a',newline='')
csvWriter = csv.writer(csvFile,delimiter=',',lineterminator='\n\n')

#place only the user inputs into their own function.
def recordMyClimbs():
    #what if user input is empty?
    #what if user input is the wrong type?

    while True:
        climb_number = input("What number route is this?")
        wall_type = input("What type of wall was the route on?")
        grade = input("What was the grade of the route?")
        pre_body = input("On a scale of 1-10, how difficult did this route feel on your body?")
        pre_heart = input("On a scale of 1-10, how difficult did this route feel on your heart?")
        csvWriter.writerow([date,time,climb_number,wall_type,grade,pre_body,pre_heart])

recordMyClimbs()

#i want to ask a question, and get user input, and then make sure the input isnt blank. if it is blank i want to give a message that says the input cant be empty.

#def climbNumber(input("What number route is this?")):
