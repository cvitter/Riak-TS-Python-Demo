from riak import RiakClient
client = RiakClient()

__doc__ = """\
ListAllKeys.py
Demonstrates how to use the ListKeys builder to return all of the primary keys in a table.

!!WARNING!!
    Listing all of the keys is an expensive operation that shouldn't be run
    against a production cluster for performance reasons.
    
    Bug Warning: .ts_stream_keys only works with tables that have three part
    primary keys and will error out if the primary key only consists of a
    quantum.

For more information see the Python Client API documentation at:
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = client.table("waterMeterData")

key_count = 0
stream = client.ts_stream_keys(table, 1000)

for key_list in stream:
    for key in key_list:
        key_count += 1
        print(key)
stream.close()

print("Total Keys: {}".format(key_count))