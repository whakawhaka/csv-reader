import pandas as pd


def csv_read(file_name, header):
    df = pd.read_csv(file_name)
    sorted_df = df.sort_values(by=[header], ascending = False)
    return (sorted_df[header].tolist())

def compare (seta, setb):
    setc = set(seta).intersection(setb)
    print (*setc, sep = "\n")
    return setc
    
def header_read(file_name):
    df = pd.read_csv(file_name)
    data_top = list(df.columns)
    return data_top

        
"""
df = pd.read_csv('Netstaler_Enum.csv')
bf = pd.read_csv('Netstaler_Enum.csv')

data_top = data.head() 
data_top = data.head() 

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
print (*c, sep = "\n")*\




sorted_df.to_csv('sorted_csvdata.csv', header=None, index=None)
"""