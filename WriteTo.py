from datetime import datetime, timedelta
import calendar
from riak import RiakClient
client = RiakClient()

__doc__ = """\
WriteTo.py
Demonstrates how to use the Riak TS Table .store() method to write new records.

This example writes 1,000 records, subtly changing the values as
the records get written to make the data more interesting.

For more information see the Python Client API documentation at:
http://docs.basho.com/riakts/latest/developing/python/

Note: This example uses the table created in
CreateTable.py and will fail if that code hasn't been successfully
executed against your Riak TS cluster first.
"""

table = "waterMeterData"

# Create start date for our time series records
reading_date = datetime(2016, 4, 7, 12, 00)

water_pressure = 40.0
gallons_per_hour = 2.0
total_gallons = 1000.0
data_set = []

for row_count in range(1,1001):
    # Convert date to epoch for TS
    epoch_date = calendar.timegm(datetime.timetuple(reading_date))*1000
    
    # Create row object and add to our data_set
    new_row = ['CUSTOMER-0001','METER-0001', epoch_date, water_pressure, gallons_per_hour, total_gallons]
    data_set.append(new_row)
    
    # Update date and values to fake progression of time
    epoch_date += 60000
    if row_count % 2 == 0:
        water_pressure = 41.0
        gallons_per_hour = 2.5
    elif row_count % 3 == 0:
        water_pressure = 42.0
        gallons_per_hour = 3.0
    elif row_count % 5 == 0:
        water_pressure = 39.0
        gallons_per_hour = 3.5
    else:
        water_pressure = 40.0
        gallons_per_hour = 2.0

    total_gallons += gallons_per_hour
    
    # Add one hour to the our date
    reading_date += timedelta(hours=1)
    
    print("{} {}".format(row_count,new_row))

try:   
    # Create new tsObject and save to the database with .store()
    table_object = client.table(table).new(data_set)
    result = table_object.store()
    print("Records written: {}".format(result))
except Exception as e:
    print("Error: {}".format(e))