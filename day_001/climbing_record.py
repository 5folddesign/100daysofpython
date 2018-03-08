#python3
#climbing_record.py is a script to record the grades, and perceived rate of exertion during an indoor rock climbing session.


# I want this script to record: the number of the climb, wall type, grade of climb, perceived rate of exertion on my body, perceived rate of exertion on my heart, and the date and time of the climbing session. I then want all of this information to be added to a .csv file


import csv

def recordMyClimbs():
    while True:
        csvFile = open('/Users/laptop/github/100daysofpython/day_001/climbinglog.csv','a',newline='')
        csvWriter = csv.writer(csvFile,delimiter=',',lineterminator='\n\n')

        climbNumber = input("What number route is this?")
        wallType = input("What type of wall was the route on?")
        grade = input("What was the grade of the route?")
        preBody = input("On a scale of 1-10, how difficult did this route feel on your body?")
        preHeart = input("On a scale of 1-10, how difficult did this route feel on your heart?")

        csvWriter.writerow([climbNumber,wallType,grade,preBody,preHeart])
        break

recordMyClimbs()
