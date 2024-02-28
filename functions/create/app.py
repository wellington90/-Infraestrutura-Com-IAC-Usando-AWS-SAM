import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my_table')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item_id = str(uuid.uuid4())
    item_name = body['name']

    table.put_item(Item={'id': item_id, 'name': item_name})

    return {
        'statusCode': 200,
        'body': json.dumps({'id': item_id, 'name': item_name})
    }
