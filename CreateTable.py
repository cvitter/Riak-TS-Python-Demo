'''
    CreateTable.py
    Demonstrates how to create a table in Riak TS via the Python Client API
    For more information see the Python Client API documentation at: 
    http://docs.basho.com/riak/latest/dev/taste-of-riak/python/
'''
from riak import RiakClient
client = RiakClient()

table = "waterMeterData"

query = """
CREATE TABLE waterMeterData (
    customerId  varchar not null,
    meterId  varchar not null,
    ts timestamp not null,
    waterPressure double not null,
    gallonsPerHour double not null,
    totalGallons double not null,
    PRIMARY KEY(
        (customerId, meterId, quantum(ts, 30, 'd')),
         customerId, meterId, ts
    )
)
"""

try:
    client.ts_query(table, query)
    print "Table '" + table + "' created successfully"
    
except Exception as e:
    print e
