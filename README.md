# Riak TS - Python Demonstration Code

Sample Python 2 and 3 code that demonstrates how to use the Python client to work with
[Riak TS](http://docs.basho.com/riakts/latest/) (Time Series). Riak TS is an extension
of Riak KV that is optimized for storing semistructured data by timestamp.

Note: Please install Version 2.5.2 or later of the Riak Python client.

# What This Code Does

The code in this sample application is designed to demonstrate how to use the
current Riak Python client
(http://docs.basho.com/riakts/latest/developing/python/) to interact with Riak
TS and the features in the 1.3 release
(http://docs.basho.com/riakts/latest/releasenotes/). 

1. CreateTable.py - Creates and activates the waterMeterData table in your Riak TS cluster. Running this class more than once will return the following error: "Failed to create table waterMeterData: already_active".
2. DescribeTable.py - Returns the schema of the table if it has been created.
3. WriteTo.py - Writes a set of records to the waterMeterData table.
4. ReadRows.py - Reads a range of records (based on a time range) and outputs the rows and columns to the console.
5. ReadAggregates.py - Reads a range of records (based on a time range) and outputs the total count of rows in the range and min, max, and average values of the waterPressure field.
6. ReadArithmetic.py - Reads a range of records (based on a time range) and outputs the results of arithmetic operations on three columns.
7. ReadSingleRow.py - Reads one record using the record's primary key.
8. DeleteSingleKey.py - Deletes one record using the record's primary key.
9. ListAllKeys.py - List all of the primary keys for the waterMeterData table. WARNING: Listing all keys is an expensive operation and should not be done in production.
10. WriteWithPut.py - Use `ts_put` for a bulk upload.
11. WriteWithSQL.py - Demonstrates the use of 'INSERT' to write data in Riak TS that was added in TS 1.3.

Please submit PRs and Issues.

Thanks to Sean (https://github.com/seanjensengrey) for rewriting most of this code for the 1.2 release to make it more Python 2/3 compatible and stylish.
