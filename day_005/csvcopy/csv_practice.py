#start practicing with csv module.
import csv

#Open a csv document and assign it to variable exampleFile
exampleFile = open('/Users/laptop/Documents/Python/automatetheboring/csv/New_Cliffs _Members.csv')
#Use csv.reader to create reader object on variable exampleFile
exampleReader = csv.reader(exampleFile)
#turn data from exampleReader into a list.
exampleData = list(exampleReader)
#show exampleData
print(exampleData[0])

def showIndex():
    item_num = 0
    for item in exampleData[0]:
        print('Column#{} : {} '.format(item_num,item))
        item_num = item_num + 1

showIndex()
