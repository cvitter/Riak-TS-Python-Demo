from datetime import datetime
from riak import RiakClient
client = RiakClient()

__doc__ = """\
ReadSingleRow.py
Demonstrates how to query Riak TS for a single row using the primary key.
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = "waterMeterData"

key = ['CUSTOMER-0001', 'METER-0001', datetime(2016, 4, 11, 2, 0)]

data_set = client.ts_get(table, key)
print(data_set.rows[0])