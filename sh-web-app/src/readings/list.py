import json
from src.utilities.database.db_models import DatabaseEngine, Sensor
from src.utilities.modules.readings.operations import SensorReadingOps
from src.utilities.modules.sensor.operations import SensorOps
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import success_response

db_ops = DatabaseEngine()
session = db_ops.get_db_session()

def list_r(event,context):
    try:
        obj = SensorReadingOps(session, json.loads(event['body']))
        sensors = obj.list_sensors_reagings()
        if sensors:
            return success_response("Data retrieved successfully", sensors)
        else:
            return error_response("Incorrect sensor_id",400)
    except Exception as e:
        print(str(e))
        return error_response("Data not retrieved successfully",500)