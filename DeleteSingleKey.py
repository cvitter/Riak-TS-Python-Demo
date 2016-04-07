'''
    DeleteSingleKey.py
    Demonstrates the how to delete a single row from Riak TS using the primary key.
    http://docs.basho.com/riakts/latest/developing/python/

    Note: This example uses the table created in CreateTable.py and 
    the data written in WriteTo.py and will fail if that code hasn't 
    been successfully executed against your Riak TS cluster first.
'''
from datetime import datetime
from riak import RiakClient
client = RiakClient()

table = "waterMeterData"
key = ['CUSTOMER-0001', 'METER-0001', datetime(2016, 4, 13, 3, 0)]

try:
    result = client.ts_delete(table, key)
    print "Key deleted: " + str(result)
except Exception as e:
    print "Error: " + str(e)