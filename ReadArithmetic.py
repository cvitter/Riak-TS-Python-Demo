'''
    ReadArithmetic.py
    Demonstrates the basics of querying Riak TS using arithmetic
    http://docs.basho.com/riakts/latest/developing/python/

    Note: This example uses the table created in CreateTable.py and 
    the data written in WriteTo.py and will fail if that code hasn't 
    been successfully executed against your Riak TS cluster first.
'''
from datetime import datetime
import calendar
from riak import RiakClient
client = RiakClient()

table = "waterMeterData"

# Create start date and end date for the range query and convert to epoch
start_date = calendar.timegm( datetime.timetuple( datetime(2016, 4, 9, 12, 00) ) )*1000 
emd_date = calendar.timegm( datetime.timetuple( datetime(2016, 4, 15, 12, 00) ) )*1000

query = """
    select MAX(totalGallons) - MIN(totalGallons) from waterMeterData where 
        ts > %s and ts < %s and 
        customerId = 'CUSTOMER-0001' and meterId = 'METER-0001'
""" % (start_date, emd_date)

data_set = client.ts_query(table, query)
row = data_set.rows[0]

print "Gallons Used: "  + str(row[0])