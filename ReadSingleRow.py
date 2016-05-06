from datetime import datetime
from riak import RiakClient

# Note: If you wish Riak TS to return date fields as Python dates
# and not epoch you need to set the transport_options as shown below
client = RiakClient(transport_options={'ts_convert_timestamp': True})

__doc__ = """\
ReadSingleRow.py
Demonstrates how to query Riak TS for a single row using the primary key.
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = "waterMeterData"

key = [datetime(2016, 4, 9, 12, 00)]

data_set = client.ts_get(table, key)
print(data_set.rows[0])