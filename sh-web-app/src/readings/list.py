try:
  import unzip_requirements
except ImportError:
  pass
import json
from src.utilities.database.db_models import DatabaseEngine, Sensor
from src.utilities.modules.readings.operations import SensorReadingOps
from src.utilities.modules.sensor.operations import SensorOps
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import success_response

db_obj = DatabaseEngine()
conn = db_obj.get_db_connection()
cur = db_obj.get_db_cursor(conn)

def list_r(event,context):
    try:
        obj = SensorReadingOps(cur, conn, json.loads(event['body']))
        sensors = obj.list_s()
        return success_response("Data retrieved successfully", sensors)
    except Exception as e:
        print(str(e))
        return error_response("Data not retrieved successfully",500)