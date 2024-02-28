import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my_table')

def lambda_handler(event, context):
    response = table.scan()

    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
