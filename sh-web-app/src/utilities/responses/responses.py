import json

def success_response(msg, response_payload):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": msg,
            "data": response_payload
        }),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response

def error_response(msg,code):
    response = {
        "statusCode": code,
        "body": json.dumps({
            "status": "error",
            "message": msg
        }),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response

# "headers": {
#             "Content-Type": "application/json",
#             "Access-Control-Allow-Origin" : "*",
#             "Access-Control-Allow-Methods": "*",
#             'Access-Control-Allow-Headers': "*",
#             'Accept': "'*/*'",
#             'Access-Control-Allow-Credentials': False
#             }