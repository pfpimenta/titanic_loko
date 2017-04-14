import csv

headerList = ['PassengerId',
                'Survived',
                'Pclass',
                'Name',
                'Sex',
                'Age',
                'SibSp',
                'Parch',
                'Ticket',
                'Fare',
                'Cabin',
                'Embarked']

dataDict = {'PassengerId' : [],
                'Survived': [],
                'Pclass': [],
                'Name': [],
                'Sex': [],
                'Age': [],
                'SibSp': [],
                'Parch': [],
                'Ticket': [],
                'Fare': [],
                'Cabin': [],
                'Embarked': []}

print(dataDict )
'''
print(headerList.keys())
print('::::')
for key in headerList.keys():
    print(headerList[key])
    '''

with open('train.csv', 'rb') as f:
    csvLido = csv.reader(f)
    for row in csvLido:
        if not (row[0] in headerList):
            print(row)
        if not (row[0] in headerList):
            for i in range(0,len(row)):
                chave = headerList[i] 
                dataDict[chave].append(row[i])
        #print listsDict
    for key,value in dataDict.iteritems():
            print(key + ' = ' + value[100])
