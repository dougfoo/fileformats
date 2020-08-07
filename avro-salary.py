import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("salary.avsc", "rb").read())  

writer = DataFileWriter(open("salary.avro", "wb"), DatumWriter(), schema)
writer.append({"id": 1, "fname": "DOUG","lname": "FOO", "department":"FOOSTACK","jobtitle":"PROGRAMMER","gender":"M","salary":120000})
writer.append({"id": 2, "fname": "JANE","lname": "FOO", "department":"FOOSTACK","jobtitle":"PROGRAMMER","gender":"F","salary":110000})
writer.append({"id": 3, "fname": "DOUG","lname": "BAR", "department":"FOOSTACK","jobtitle":"PROGRAMMER","gender":"M","salary":100000})
writer.append({"id": 4, "fname": "JANE","lname": "BAR", "department":"FOOSTACK","jobtitle":"PROGRAMMER","gender":"F","salary":130000})
writer.close()

rdr = DataFileReader(open("salary.avro", "rb"), DatumReader()) 
for row in rdr:
    print(row)
rdr.close()

