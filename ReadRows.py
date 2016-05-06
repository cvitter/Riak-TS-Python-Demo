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

# Function to convert Python date to Unix Epoch
def convert_to_epoch ( date_to_convert ):
    return calendar.timegm(datetime.timetuple( date_to_convert )) * 1000

# Create start date and end date for the range query and convert to epoch
start_ts = convert_to_epoch( datetime(2016, 4, 9, 12, 00) )
end_ts = convert_to_epoch( datetime(2016, 4, 11, 12, 00) )

query = """\
SELECT *
FROM
    waterMeterData
WHERE
    ts > {} and ts < {} and
    customer_id = 'CUSTOMER-0001' and meter_id = 'METER-0001'
""".format(start_ts, end_ts)

data_set = client.ts_query(table, query)
rowcount = len(data_set.rows)

for row in data_set.rows:
    print(row)
print("Total Rows: {}".format(rowcount))