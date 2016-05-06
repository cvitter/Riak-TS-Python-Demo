from datetime import datetime
import calendar
from riak import RiakClient
client = RiakClient()

__doc__ = """\
WriteWithSQL.py
Demonstrates how to write to a table using the SQL INSERT command.
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in CreateTable.py and
the data written in WriteTo.py and will fail if that code hasn't
been successfully executed against your Riak TS cluster first.
"""

table = "waterMeterData"

# Function to convert Python date to Unix Epoch
def convert_to_epoch ( date_to_convert ):
    return calendar.timegm(datetime.timetuple( date_to_convert )) * 1000

# Create reading_date and convert to epoch
reading_date = convert_to_epoch( datetime(2016, 4, 9, 12, 00) )

query = """\
INSERT INTO waterMeterData 
    (customer_id, meter_id, ts, water_pressure, gallons_per_hour, total_gallons) 
VALUES
    ('CUSTOMER-0001', 'METER-0001', {}, 40.0, 2.0, 1000.0);
""".format(reading_date)

alternate_query = """\
INSERT INTO waterMeterData VALUES ('CUSTOMER-0001', 'METER-0001', {}, 40.0, 2.0, 1000.0);
""".format(reading_date)

try:
    client.ts_query(table, alternate_query)
    print alternate_query
    print "Record Written"
except Exception as e:
    print(e)
