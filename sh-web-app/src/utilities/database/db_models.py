from uuid import uuid4
from src.utilities.libs.db_module_lib import *
from src.utilities.libs.db_libs import *

import os
import json

class DatabaseEngine:
    def __init__(self):
        self.db_engine_str = os.environ['RDS_ENDPOINT_STR']
        # self.db_engine      = create_engine(self.db_engine_str,pool_reset_on_return='rollback',isolation_level = 'AUTOCOMMIT',pool_size=10)
        self.session = None
        self.dbname='smarthelio_dev'
        self.user='postgres'
        self.password='Admin123'
        self.host='smarthelio-dev.cynjegoatv2n.us-east-1.rds.amazonaws.com'
        self.port = 5432
        self.connection = None

    def create_db_connection(self):
        connection = psycopg2.connect(
            dbname      = self.dbname,
            user        = self.user,
            password    = self.password,
            host        = self.host,
            port        = self.port
        )
        return connection

    def get_db_connection(self):
        if not self.connection:
            print('connection not present hence creating an obj....')
            self.connection = self.create_db_connection()
        else:
            print('connection obj present..')

        return self.connection

    def get_db_cursor(self, connection):
        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.itersize = 10000 # chunk size
        return cursor

class Sensor(DatabaseEngine):
    __tablename__ = "sensor"  

    # Constructor-->
    def __init__(self, conn, cur):
        # init column names:
        self.sensor_id = "sensor_id"
        self.created_at = "created_at"
        self.updated_at = "updated_at"
        # init cursor and connection
        self.conn = conn
        self.cursor = cur
        # self.create_table()

    def create_table(self):
        try:
            query = "CREATE TABLE IF NOT EXISTS {0} " \
            "({1} varchar(100) NOT NULL," \
            "{2} TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
            "{3} TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
            "PRIMARY KEY ({1}))".format(Sensor.__tablename__, self.sensor_id,
            self.created_at, self.updated_at)

            print(query)
            # execute the query:
            self.cursor.execute(query)
            # close the conn -->
            self.conn.commit()
            # self.conn.close()
            print('Table created if not exists..')
        except Exception as e:
            print(str(e))
        
    def create_index(self):
        try:
            index_name = 'sensor_index'
            query = "CREATE INDEX {0} " \
            "ON {1} ({2});".format(index_name, Sensor.__tablename__,
                                self.sensor_id)
            
            # execute the query:
            self.cursor.execute(query)
            # close the conn -->
            self.conn.commit()
            # self.conn.close()
            print('Index Created')
        except Exception as e:
            print(str(e))

class SensorReading(Sensor): # Multi-level inheritance A->B->C
    __tablename__ = "sensor_readings"  
    
    # Constructor-->
    def __init__(self, conn, cur):
        self.sensor = Sensor(conn, cur)
        # init column names:
        self.reading_id = "reading_id"
        self.sensor_id = self.sensor.sensor_id # foreign_key ref
        self.date_time = "date_time"
        self.duration = "duration"
        self.current = "current"
        self.voltage = "voltage"
        self.created_at = "created_at"
        self.updated_at = "updated_at"
        # init cursor and connection
        self.conn = conn
        self.cursor = cur
        # self.create_table()
        # self.create_index()

    def create_table(self):
        try:
            query = "CREATE TABLE IF NOT EXISTS {0} " \
            "( {1} varchar(100) NOT NULL," \
            "{2} varchar(100) NOT NULL," \
            "{3} TIMESTAMP NOT NULL," \
            "{4} NUMERIC NOT NULL," \
            "{5} NUMERIC NOT NULL," \
            "{6} NUMERIC NOT NULL," \
            "{7} TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
            "{8} TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
            "PRIMARY KEY ({1})," \
            "CONSTRAINT fk_sensor " \
            "FOREIGN KEY({2})" \
            "REFERENCES {9}({2})" \
            "ON DELETE CASCADE);".format(SensorReading.__tablename__, self.reading_id,
            self.sensor_id,self.date_time, self.duration, self.current, self.voltage,
            self.created_at, self.updated_at, self.sensor.__tablename__)

            print(query)
            # execute the query:
            self.cursor.execute(query)
            # close the conn -->
            self.conn.commit()
            # self.conn.close()
            print('Table created if not exists..')
        except Exception as e:
            print(str(e))
        
    def create_index(self):
        try:
            index_name = 'sensor_reading_index'
            query = "CREATE INDEX {0} " \
            "ON {1} ({2}, {3});".format(index_name, SensorReading.__tablename__,
                                self.sensor_id, self.date_time)
            
            # execute the query:
            self.cursor.execute(query)
            # close the conn -->
            self.conn.commit()
            # self.conn.close()
            print('Index Created')
        except Exception as e:
            print(str(e))
