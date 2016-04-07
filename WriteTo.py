'''
    WriteTo.py
    Demonstrates how to use the Riak TS Store object to write new records.
    This example writes 1,000 records, subtly changing the values as
    the records get written to make the data more interesting.
    For more information see the Java Client API documentation at: 
    http://docs.basho.com/riakts/latest/developing/python/

    Note: This example uses the table created in
    CreateTable.py and will fail if that code hasn't been successfully
    executed against your Riak TS cluster first.
'''
from datetime import datetime, timedelta
import calendar
from riak import RiakClient
client = RiakClient()

table = "waterMeterData"

# Create start date for our time series records
reading_date = datetime(2016, 4, 7, 12, 00)

row_count = 1
waterPressure = 40.0
gallonsPerHour = 2.0
totalGallons = 1000.0
data_set = []

while row_count <= 1000:
    # Convert date to epoch for TS
    epoch_date = calendar.timegm(datetime.timetuple(reading_date))*1000
    
    # Create row object and add to our data_set
    new_row = ['CUSTOMER-0001','METER-0001', epoch_date, waterPressure, gallonsPerHour, totalGallons]
    data_set.append(new_row)
    
    # Update date and values to fake progression of time
    epoch_date += 60000
    if row_count % 2 == 0:
        waterPressure = 41.0
        gallonsPerHour = 2.5
    elif row_count % 3 == 0:
        waterPressure = 42.0
        gallonsPerHour = 3.0
    elif row_count % 5 == 0:
        waterPressure = 39.0
        gallonsPerHour = 3.5
    else:
        waterPressure = 40.0
        gallonsPerHour = 2.0
    totalGallons += gallonsPerHour
    
    # Add one hour to the our date
    reading_date += timedelta(hours=1)
    
    print str(row_count) + " " + str(new_row)
    row_count += 1

try:   
    # Create new tsObject and save to the database with .store()
    table_object = client.table(table).new(data_set)
    table_object.store()    
except Exception as e:
    print e