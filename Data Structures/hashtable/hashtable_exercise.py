import hashtable as ht
import pandas as pd

#read csv file
weather = pd.read_csv(r'DSA\nyc_weather.csv')
table = ht.HashTable()

for index, row in weather.iterrows():
    table[row['date']] = row['temperature(F)']

print(table.arr)
print(table['Jan 9'])
print(table['Jan 4'])


"""
--------------------------------------Exercise 2---------------------------------------------
"""



word_count={}

with open("poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            if token in word_count:
                word_count[token] +=1
            else:
                word_count[token]=1

print(word_count)