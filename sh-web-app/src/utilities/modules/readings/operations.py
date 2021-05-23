import decimal
import json
from re import S
from src.utilities.database.db_models import DatabaseEngine, SensorReading
from src.utilities.libs.common_libs import *
from src.utilities.responses.responses import * 


class SensorReadingOps:
    
    def __init__(self, cur, conn, payload):
        self.cur = cur
        self.conn = conn
        self.sensor_reagings = []
        self.payload = payload
        # init class obj
        self.sensor = Sensor(conn,cur)
        self.sensorRead = SensorReading(conn,cur)

    def list_sensors_reagings(self):
        try:
            # validate the sensor_id
            print('incoming payload:',self.payload)
            if self.session.query(Sensor).filter(Sensor.sensor_id == self.payload['sensor_id']).first():
                # query db for the selected range of data -->
                result = self.session.query(SensorReading).filter(SensorReading.sensor_id == self.payload['sensor_id'],
                SensorReading.date_time.between(self.payload['from_date'], self.payload['to_date'])).all()
                for each_reading in result:
                    print(each_reading)
                    self.sensor_reagings.append({
                    "sensor_id": each_reading.sensor_id,
                    "sensor_name" : self.session.query(Sensor).filter(Sensor.sensor_id == each_reading.sensor_id).first().sensor_name,
                    "current" : each_reading.current,
                    "voltage": each_reading.voltage,
                    "duration" : each_reading.duration,
                    "power": round(float(each_reading.current * each_reading.voltage),2),
                    "date": each_reading.date_time.strftime("%m/%d/%Y %H:%M:%S")
                    })
                
                # list(map(lambda each_reading: self.sensor_reagings.append({
                #     "sensor_id": each_reading.sensor_id,
                #     "sensor_name" : self.session.query(Sensor).filter(Sensor.sensor_id == each_reading.sensor_id).first().sensor_name,
                #     "current" : each_reading.current,
                #     "voltage": each_reading.voltage,
                #     "duration" : each_reading.duration,
                #     "power": round(float(each_reading.current * each_reading.voltage),2),
                #     "date": each_reading.date_time.strftime("%m/%d/%Y %H:%M:%S")
                # }), self.session.query(SensorReading).filter(SensorReading.sensor_id == self.payload['sensor_id'],
                # SensorReading.date_time.between(self.payload['from_date'], self.payload['to_date'])).all()))
                print('no')
            else:
                return False                
            
            print('returning')
            return self.sensor_reagings
        except Exception as e:
            print(str(e))

    def list_s(self):
        try:
            print('incoming payload:',self.payload)
            # get the max date
            max_date_q = "SELECT MAX ({0}) from {1};".format(self.sensorRead.date_time,
            self.sensorRead.__tablename__)
            print(max_date_q)
            self.cur.execute(max_date_q)
            max_date = self.cur.fetchone()['max']
            
            # get the min date
            min_date_q = "SELECT MIN ({0}) from {1};".format(self.sensorRead.date_time,
            self.sensorRead.__tablename__)
            self.cur.execute(min_date_q)
            min_date = self.cur.fetchone()['min']
            

            if self.payload['gap']:
                new_date = max_date - timedelta(days=int(self.payload['gap']))
            else:
                new_date = min_date
            
            #get the data
            readings_q = "SELECT * from {0} where {1} = '{2}' AND {3} BETWEEN '{4}' AND '{5}' ORDER BY {3};".format(self.sensorRead.__tablename__,
            self.sensorRead.sensor_id,str(self.payload['sensor_id']),self.sensorRead.date_time, 
            str(new_date.strftime("%Y-%m-%d")),str(max_date.strftime("%Y-%m-%d")))
            self.cur.execute(readings_q)
            print(readings_q)            

            list(map(lambda each_reading: self.sensor_reagings.append({
                "sensor_id": each_reading['sensor_id'],
                "current" : float(each_reading['current']),
                "voltage": float(each_reading['voltage']),
                "duration" : float(each_reading['duration']),
                "power": round(float(float(each_reading['current']) * float(each_reading['voltage'])),2),
                "date": each_reading['date_time'].strftime("%Y-%m-%d %H:%M:%S")
            }),self.cur.fetchall()))
            
            
            return self.sensor_reagings
        except Exception as e:
            self.cur.execute('ROLLBACK')
            print(str(e))


