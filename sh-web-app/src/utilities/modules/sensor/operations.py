import json
from src.utilities.database.db_models import Sensor
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import success_response

class SensorOps:
    
    def __init__(self, cur, conn):
        self.cur = cur
        self.conn = conn
        self.senson_list = []
        self.sen = Sensor(conn, cur)
        self.senRead = SensorReading(conn, cur)

    def list_sensors(self):
        try:
            query = "SELECT DISTINCT {1} FROM {0};".format(SensorReading.__tablename__, self.senRead.sensor_id)
            self.cur.execute(query)

            # get the all the sensors -->
            list(map(lambda each_sensor: self.senson_list.append({
                "sensor_id":each_sensor['sensor_id']
            }),self.cur.fetchall()))
            return self.senson_list
        except Exception as e:
            print(str(e))



