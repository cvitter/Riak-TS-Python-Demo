from riak import RiakClient
client = RiakClient()

__doc__ = """\
CreateTable.py
Demonstrates how to create a table in Riak TS via the Python Client API

V1.3: Updated to reflect additional flexibility in designating primary
      keys. As of 1.3 only the quantum function is required (as shown
      below) however it is still possible to have multi-part primary
      keys as long as the quantum is the last part of the key specified.

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
        ( quantum(ts, 30, 'd') ),
          ts
    )
)
"""

try:
    client.ts_query(table, query)
    print("Table '{}' created successfully".format(table))
except Exception as e:
    print(e)