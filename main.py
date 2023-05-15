#import the needed modules for the program requests
#for collecting the data from api request and boto3 for create, configure, and manage AWS services 
import requests
import boto3

#to collect the data from the given api request url to response variable
response = requests.get("<api request url>")

#setting up the connection for dynamodb database using boto3
db = boto3.resource('dynamodb')
#for the table
dbTable = db.Table('<table name>')

#create an empti list to store the needed values from the json data
ids = []

#iterate through each dictionary to collect the data id=f any field is missing it will give the value "UNKNOWN" inthat field
for x in response.json():
    if 'id' in x:
        data={
            'id': str(x['id']),
            'name': x['name']}
        ids.append(data)               #append the data to the list that created

        dbTable.put_item(
            Item={
            'id': str(x['id']),
            'name': x['name']}         #put item(the data that we collected from the api request) into the dynamodb database
        )

    else:
        data={
            'id': str(x['id']),
            'name': x['name']}
        ids.append(data)               #append the data to the list that created

        dbTable.put_item(
            Item={
                'id': 'UNKNOWN',
                'name': x['name']}     #put the item(the data that we collected from the api request) into the dynamodb database
        )


