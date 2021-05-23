import decimal
import json
from re import S
from src.utilities.database.db_models import DatabaseEngine, SensorReading
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import * 


class SensorReadingOps:
    
    def __init__(self, session, payload):
        self.session = session
        self.sensor_reagings = []
        self.payload = payload

    def list_sensors_reagings(self):
        try:
            # validate the sensor_id
            print('incoming payload:',self.payload)
            if self.session.query(Sensor).filter(Sensor.sensor_id == self.payload['sensor_id']).first():
                # query db for the selected range of data -->
                max_date = self.session.query(func.max(SensorReading.date_time)).first()
                min_date = self.session.query(func.min(SensorReading.date_time)).first()

                if self.payload['gap']:
                    print(self.payload['gap'])
                    new_date = max_date[0] - timedelta(days=int(self.payload['gap']))
                else:
                    new_date = min_date[0]

                print("max date:",max_date[0])
                print('new date/min date:', new_date.strftime("%Y-%m-%d"))

                result = self.session.query(SensorReading).filter(SensorReading.sensor_id == self.payload['sensor_id'],
                SensorReading.date_time.between(str(new_date.strftime("%Y-%m-%d")),str(max_date[0]))).all()
                
                print('ok')
                list(map(lambda each_reading: self.sensor_reagings.append({
                    "sensor_id": each_reading.sensor_id,
                    "current" : float(each_reading.current),
                    "voltage": float(each_reading.voltage),
                    "duration" : float(each_reading.duration),
                    "power": round(float(each_reading.current * each_reading.voltage),2),
                    "date": each_reading.date_time.strftime("%m/%d/%Y %H:%M")
                }),result))
                
            else:
                print('Incorrect sensorId')
                return False            
            
            return self.sensor_reagings
        except Exception as e:
            print(str(e))


