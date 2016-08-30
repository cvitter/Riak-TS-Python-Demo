from datetime import datetime
import calendar
from riak import RiakClient

# Note: If you wish Riak TS to return date fields as Python dates
# and not epoch you need to set the transport_options as shown below
client = RiakClient(transport_options={'ts_convert_timestamp': True})

__doc__ = """\
ReadRows.py
Demonstrates the basics of querying Riak TS.
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = "waterMeterData"

query = """\
SELECT *
FROM
    waterMeterData
WHERE
    ts > '2016-04-09 12:00' and ts < '2016-04-11 12:00' and
    customer_id = 'CUSTOMER-0001' and meter_id = 'METER-0001'
"""

data_set = client.ts_query(table, query)
rowcount = len(data_set.rows)

for row in data_set.rows:
    print(row)
print("Total Rows: {}".format(rowcount))