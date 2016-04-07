'''
    ListAllKeys.py
    Demonstrates how to use the ListKeys builder to return all of the primary keys in a table
    HOWEVER listing all of the keys is an expensive operation that shouldn't be run
    against a production cluster for performance reasons.

    For more information see the Python Client API documentation at: 
    http://docs.basho.com/riakts/latest/developing/python/

    Note: This example uses the table created in
    CreateTable.py and the data written in WriteTo.py.
'''
from riak import RiakClient
client = RiakClient()

mytable = "waterMeterData"
table = client.table(mytable)

key_count = 0

stream = client.ts_stream_keys(table)
for list_of_keys in stream:
    for key in list_of_keys:
        key_count += 1
        print key
stream.close()

print "Total Keys: " + str(key_count)