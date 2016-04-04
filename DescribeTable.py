'''
    DescribeTable.py
    Demonstrates how to use the DESCRIBE command in Riak TS  via the Python Client API 
    to view a table's schmea or simply verify a table has been created
    For more information see the Java Client API documentation at: 
    http://docs.basho.com/riakts/latest/developing/python/

    Note: This example uses the WeatherStationData table created in
    CreateTable.py and will fail if that code hasn't been successfully
    executed against your Riak TS cluster first.
'''
from riak import RiakClient
client = RiakClient()

table = "waterMeterData"

query = "DESCRIBE waterMeterData"

try:
    response = client.ts_query(table, query)
    rowcount = len(response.rows)
    
    for r in range (0, rowcount):
        print response.rows[r]
    
except Exception as e:
    print e
