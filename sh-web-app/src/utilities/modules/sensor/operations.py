import json
from src.utilities.database.db_models import Sensor
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import success_response

class SensorOps:
    
    def __init__(self, session):
        self.session = session
        self.senson_list = []

    def list_sensors(self):
        try:
            list(map(lambda each_sensor: self.senson_list.append({
                "sensor_id":each_sensor.sensor_id
            }),self.session.query(Sensor).all()))

            return self.senson_list
        except Exception as e:
            print(str(e))



