import json
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import success_response

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    return success_response("success", body)
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
