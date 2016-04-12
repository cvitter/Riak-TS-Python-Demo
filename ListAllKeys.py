from riak import RiakClient
client = RiakClient()

__doc__ = """\
ListAllKeys.py
Demonstrates how to use the ListKeys builder to return all of the primary keys in a table.

!!WARNING!!
    Listing all of the keys is an expensive operation that shouldn't be run
    against a production cluster for performance reasons.

For more information see the Python Client API documentation at:
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = client.table("waterMeterData")

key_count = 0
stream = client.ts_stream_keys(table)
for list_of_keys in stream:
    for key in list_of_keys:
        key_count += 1
        print(key)
stream.close()

print("Total Keys: {}".format(key_count))