from datetime import datetime
from riak import RiakClient
client = RiakClient()

__doc__ = """\
WriteTo.py
Demonstrates how to use the Riak TS Client .ts_put method
to write a single record.

For more information see the Python Client API documentation at:
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in
CreateTable.py and will fail if that code hasn't been successfully
executed against your Riak TS cluster first.
"""

table = "waterMeterData"

record_list = [
    ['CUSTOMER-0001', 'METER-0001', datetime(2016, 4, 11, 2, 0), 40.0, 2.0, 1000.0]
]

table_object = client.table(table).new(record_list)

try:
    result = client.ts_put(table_object)
    print("Record written: {}".format(result))
except Exception as e:
    print("Error: {}".format(e))