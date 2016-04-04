'''
    ListAllKeys.py
    Demonstrates how to use the ListKeys builder to return all of the primary keys in a table
    HOWEVER listing all of the keys is an expensive operation that shouldn't be run
    against a production cluster for performance reasons.

    For more information see the Java Client API documentation at: 
    http://docs.basho.com/riak/latest/dev/taste-of-riak/python/

    Note: This example uses the WeatherStationData table created in
    CreateTable.py and the data written in WriteTo.py.
'''
from riak import RiakClient
client = RiakClient()

mytable = "WeatherStationData"
table = client.table(mytable)
stream = client.ts_stream_keys(table)

key_count = 0

for list_of_keys in stream:
    for key in list_of_keys:
        key_count += 1
        print key

stream.close()

print "Total Keys: " + str(key_count)
