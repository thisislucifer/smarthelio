from uuid import uuid4
from src.utilities.libs.db_module_lib import *
from src.utilities.libs.db_libs import *

import os
import json


def connect_db():
    # _load_db_vars()
    # create db create_engine
    db = create_engine(os.environ['RDS_ENDPOINT_STR'])
    return db

def check_table_exists(db_engine, tb_name):
    ret = db_engine.dialect.has_table(db_engine, tb_name)
    print('table %s  exists is %s' % (tb_name, ret))
    return ret


def create_tables(db_engine):
    print('creating table')
    Base.metadata.create_all(db_engine)
    # Student.__table__.create(bind= engine)

def check_db_status(db_engine, tb_name):
    # check if table exists-->
    print('tb_name %s' % (tb_name))
    res = check_table_exists(db_engine, tb_name)
    print(res)
    # create tables
    if res is False:
        create_tables(db_engine)
    else:
        print('table already exists hence disposing the db_engine_conn')
        db_engine.dispose()

engine = connect_db()
Base = declarative_base()


class DatabaseEngine:
    def __init__(self):
        self.db_engine_str = os.environ['RDS_ENDPOINT_STR']
        self.session = None

    def get_db_engine(self):
        return None

    def create_db_engine(self):
        print('creating db engine..')
        return create_engine(self.db_engine_str, pool_size=1)

    def create_db_session(self):
        print('creating db session...')
        Session = sessionmaker(bind=self.create_db_engine())
        dbsession = Session()
        return dbsession

    def get_db_session(self):
        if not self.session:
            print('session not present hence creating an obj....')
            self.session = self.create_db_session()
        else:
            print('session obj present..')

        return self.session

class Sensor(Base):
    __tablename__ = "sensor"  
    sensor_id = Column(VARCHAR(100),primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    # # Constructor-->
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
    

    def __repr__(self):
        return "Sensor(sensor_id='%s', created_at='%s', updated_at='%s')\n" % (
            self.sensor_id, self.created_at, self.updated_at)

class SensorReading(Base): # inheritance
    __tablename__ = "sensor_readings"  
    reading_id = Column(String(100), primary_key=True)
    sensor_id   = Column(VARCHAR(100))
    date_time   = Column(DateTime)
    duration    = Column(Numeric)
    current     = Column(Numeric)
    voltage     = Column(Numeric)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    # # Constructor-->
    def __init__(self, reading_id, sensor_id, date_time, duration, current, voltage):
        self.reading_id = reading_id
        self.sensor_id = sensor_id
        self.date_time  = date_time
        self.duration   = duration
        self.current    = current
        self.voltage    = voltage
    
    def __repr__(self):
        return "SensorReading(reading_id='%s', sensor_id='%s', \
            date_time='%s', duration='%s', current='%s', voltage='%s', \
            created_at='%s', updated_at='%s')\n" % (
            self.reading_id, self.sensor_id, 
            self.date_time,self.duration, self.current, self.voltage,
            self.created_at, self.updated_at)
