from datetime import datetime
import calendar
from riak import RiakClient
client = RiakClient()

__doc__ = """\
ReadArithmetic.py
Demonstrates the basics of querying Riak TS using arithmetic
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = "waterMeterData"

# Create start date and end date for the range query and convert to epoch
start_ts = calendar.timegm(datetime.timetuple(datetime(2016, 4, 9, 12, 00))) * 1000
end_ts = calendar.timegm(datetime.timetuple(datetime(2016, 4, 15, 12, 00))) * 1000

query = """\
SELECT
  MAX(total_gallons) - MIN(total_gallons) from waterMeterData
WHERE
  ts > {} AND ts < {}
  AND
  customer_id = 'CUSTOMER-0001' AND meter_id = 'METER-0001'
""".format(start_ts, end_ts)

data_set = client.ts_query(table, query)
row = data_set.rows[0]

print("Gallons Used: {:.2f}".format(row[0]))