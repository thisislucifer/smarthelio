import json
from src.utilities.modules.sensor.operations import SensorOps
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import *
from src.utilities.database.db_models import *

db_ops = DatabaseEngine()
session = db_ops.get_db_session()

def list_s(event,context):
    try:
        obj = SensorOps(session)
        sensors = obj.list_sensors()
        return success_response("Data retrieved successfully", sensors)
    except Exception as e:
        return error_response("Data not retrieved successfully",500)