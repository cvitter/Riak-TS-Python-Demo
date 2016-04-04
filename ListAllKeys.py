'''

'''

from riak import RiakClient

client = RiakClient()

mytable = "WeatherStationData"
table = client.table(mytable)
stream = client.ts_stream_keys(table)

key_count = 0

for list_of_keys in stream:
    for key in list_of_keys:
        key_count += 1
        print key

stream.close()

print "Total Keys: " + str(key_count)
