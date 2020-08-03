import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa

# df = pd.DataFrame({'one': [-1, np.nan, 2.5],
#                    'two': ['foo', 'bar', 'baz'],
#                    'three': [True, False, True]},
#                    index=list('abc'))

df = pd.read_json("data.json")

table = pa.Table.from_pandas(df)

pq.write_table(table, 'example.parquet')
print("wrote example.parquet")
print(table)

table2 = pq.read_table('example.parquet')
print("read example.parquet")
print(table2)

table2.to_pandas()

metadata = pq.read_metadata('example.parquet')
print(metadata)
print(metadata.row_group(0))
print(metadata.row_group(0).column(0))



