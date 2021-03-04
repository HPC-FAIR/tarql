import csv
import sys

print ('Argument List:', str(sys.argv))
import pandas as pd
df = pd.read_csv(sys.argv[1])
df.insert(loc=0, column='No', value=df.index+1)
df.to_csv(sys.argv[1],index=False)
