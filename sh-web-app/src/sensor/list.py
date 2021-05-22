import json
from src.utilities.modules.sensor.operations import SensorOps
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import *
from src.utilities.database.db_models import *

# create database engine and conn - 
db_obj = DatabaseEngine()
conn = db_obj.get_db_connection()
cur = db_obj.get_db_cursor(conn)

def list_s(event,context):
    try:
        obj = SensorOps(cur,conn)
        sensors = obj.list_sensors()
        return success_response("Data retrieved successfully", sensors)
    except Exception as e:
        return error_response("Data not retrieved successfully",500)