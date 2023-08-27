import pandas as pd
import csv_reader

def main():
    a = csv_reader.csv_read('Netstaler_Enum.csv',"EventTime")
    b = csv_reader.csv_read('Netstaler_Enum.csv',"EventTime")
    c = csv_reader.compare(a,b)
    d = csv_reader.header_read('Netstaler_Enum.csv')
    print (d)
    
if __name__ == "__main__":
    main()

#sorted_df.to_csv('sorted_csvdata.csv', header=None, index=None)
"""
#df = pd.read_csv('Barracuda ESG Message Log.csv')



df = pd.read_csv('Netstaler_Enum.csv')
bf = pd.read_csv('Netstaler_Enum.csv')

#data_top = data.head() 
#data_top = data.head() 

sorted_bf = bf.sort_values(by=["EventTime"], ascending = False)
sorted_df = df.sort_values(by=["EventTime"], ascending = False)


a = (sorted_bf["EventTime"].tolist())
b = (sorted_df["EventTime"].tolist())
#dataframe column needs to be changed to a list 


print(type(sorted_df))
print(type(sorted_bf))

#print(sorted_df[["EventTime"]])
#print(sorted_bf[["EventTime"]])

c = set(a).intersection(b)
print (*c, sep = "\n")




sorted_df.to_csv('sorted_csvdata.csv', header=None, index=None)"""