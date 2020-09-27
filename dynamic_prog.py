import boto3
#import json
from boto3.dynamodb.conditions import Key,Attr
#creating a dynamodb object to access the table
dynamodb = boto3.resource('dynamodb')

#accessing the table "ProductCatalog" and storing it in table
table = dynamodb.Table('ProductCatalog')

def lambda_handler(event,context):
	#here the key input is json format so we use dictionary functions to access the primary key and store it in qrc 
	qrc = event['Id']
	
	#we are storing the json input in the var Item
	Item=event
	
	#In this try block we are getting the object for the query if the query is null
	#It becomes an error so this error is caught in the catch block
	try:
		response = table.query(
		KeyConditionExpression=Key('Id').eq(qrc))
	except:
		print("Please scan a valid QR code from the Kosha Product")
		return "code is invalid"
	else:
		#we collect the query object into items var and check if the query was present
		#and depending upon the results we display the appropriate message
		items = response['Items']
		if items == []:
		    print("Code wasn't scanned!! ")
		else:
		    print("you're looking for : ",items)
		#and finally we return the queried object from the database if present
		try:
			return items[0]
		except:
			return "Your product code wasn't found. Contact us for more help!!! "