import pandas as pd
import random

df = pd.read_csv('data.tsv',sep='\t')
df['index'] = df['close'].apply(lambda d: random.choice([1,2,3]))
print "date\tclose\tindex"
for row in df.iterrows():
    print "%s\t%s\t%s" %(row[1]['date'],row[1]['close'],row[1]['index'])