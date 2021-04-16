import sys
import logging
import pymysql
import json
import os

#rds settings
rds_endpoint = os.environ['rds_endpoint']
username=os.environ['username']
password=os.environ['password']
db_name=os.environ['db_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Connection
try:
    connection = pymysql.connect(host=rds_endpoint, user=username,
        passwd=password, db=db_name)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def handler(event, context):
    cur = connection.cursor()  
## Retrieve Data
    query = "SELECT * FROM Customer where email='{}' and password='{}'".format(event['email'],event['password'])    
    cur.execute(query)
    connection.commit()
## Construct body of the response object
    
    output = []
    rows = cur.fetchall()
    for row in rows:
        print("TEST {0} {1} {2} {3} {4} {5} {6} {7}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        transactionResponse = {}
        transactionResponse['id'] = row[0]
        transactionResponse['email'] = row[1]
        # transactionResponse['password'] = row[2]
        transactionResponse['uin'] = row[3]
        transactionResponse['name'] = row[4]
        transactionResponse['addr'] = row[5]
        transactionResponse['postal'] = row[6]
        transactionResponse['contactNo'] = row[7]
        output.append(transactionResponse)

# Construct http response object
    responseObject = {}
    # responseObject['statusCode'] = 200
    # responseObject['headers'] = {}
    # responseObject['headers']['Content-Type']='application/json'
    # responseObject['headers']['Access-Control-Allow-Origin']='*'
    responseObject['data']= output
    # responseObject['body'] = json.dumps(transactionResponse, sort_keys=True,default=str)
    
    #k = json.loads(responseObject['body'])
    #print(k['uin'])

    return responseObject