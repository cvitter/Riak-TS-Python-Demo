from riak import RiakClient
client = RiakClient()

__doc__ = """\
CreateTable.py
Demonstrates how to create a table in Riak TS via the Python Client API

For more information see the Python Client API documentation at:
    http://docs.basho.com/riakts/latest/developing/python/
"""

table = "waterMeterData"

query = """\
CREATE TABLE waterMeterData (
    customer_id       varchar   not null,
    meter_id          varchar   not null,
    ts                timestamp not null,
    water_pressure    double    not null,
    gallons_per_hour  double    not null,
    total_gallons     double    not null,
    PRIMARY KEY(
        (customer_id, meter_id, quantum(ts, 30, 'd')),
         customer_id, meter_id, ts
    )
)
"""

try:
    client.ts_query(table, query)
    print("Table '{}' created successfully".format(table))
except Exception as e:
    print(e)