# from src.utilities.libs.db_module_lib import *
from src.utilities.database.db_models import DatabaseEngine, Sensor, SensorReading
from src.utilities.libs.common_libs import *
import uuid
import csv

# create database engine and conn - 
db_obj = DatabaseEngine()
conn = db_obj.get_db_connection()
cur = db_obj.get_db_cursor(conn)


def populate_data(event, context):
    print('Hello World')
    sensor = Sensor(conn,cur)
    # read the csv file -->
    with open('C:\\Aayush_Workspace\\Assignments\\data\\sensors.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for count, row in enumerate(csv_reader):
            dict_rows = dict(row)
            print("count",count)
            print("incoming payload:",dict_rows)
            sensor_id = dict_rows['sensorId']
            try:
                query = "INSERT into {0} " \
                "VALUES ('{1}')".format(sensor.__tablename__,
                sensor_id)
                print(query)
                cur.execute(query)
                conn.commit()
            except Exception as e:
                print(str(e))
                cur.execute("rollback")

    return success_response("success", {"message":"sensor data populated successfully"})


def populate_reading_data(event, context):
    sensor_reading = SensorReading(conn,cur)
    print('Hello World')
    # read the csv file -->
    with open('C:\\Aayush_Workspace\\Assignments\\data\\sensor_readings.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for count, row in enumerate(csv_reader):
            dict_rows = dict(row)
            print("count",count)
            print("incoming payload:",dict_rows)
            reading_id = str(uuid.uuid4())
            sensor_id   = dict_rows['sensorId']
            date_time   = datetime.fromtimestamp(int(dict_rows['timeStamp'])).strftime("%m/%d/%Y %H:%M:%S"),
            print(type(date_time))
            duration    = dict_rows['duration']
            current     = dict_rows['Current (in milli Amp)']
            voltage     = 0 if not dict_rows['Voltage (in Volts)'] else dict_rows['Voltage (in Volts)']
            try:
                query = "INSERT into {0} " \
                "VALUES ('{1}','{2}','{3}','{4}','{5}','{6}')".format(sensor_reading.__tablename__,reading_id,
                sensor_id,date_time[0], duration, current, voltage)
                print(query)

                cur.execute(query)
                conn.commit()
            except Exception as e:
                print(str(e))
                cur.execute("rollback")

    return success_response("success", {"message":"sensor data populated successfully"})