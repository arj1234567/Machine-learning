import pandas as pd
from pathlib import Path

#path2csv = Path("C:/Users/AVITA/Downloads/myfile/")
#csvlist = path2csv.glob("*.csv")
#csvs = [pd.read_csv(g) for g in csvlist ]
#print(csvs)
##
url_2='https://www.cboe.com/us/options/symboldir/equity_index_options/?download=csv'
ufo=pd.read_csv(url_2)
##ufo = pd.read_csv('http://bit.ly/uforeports')
##
##print(ufo)
##print(ufo.head())
##print(ufo['Company Name'])

##ufo.insert(2, column = "location" ,value="") 
##print(ufo.head())
##print(ufo['location'])





##print(ufo.dtypes)
##ufo.drop("Company Name",axis="columns",inplace=True)

##ufo.drop(['Company Name'," Stock Symbol"],axis=1,inplace=True)
##print(ufo.columns)


##print(ufo.sort_values(by=["Company Name"], ascending=False))

print(ufo.sort_values(by=["Company Name"],ascending=True))


                    

