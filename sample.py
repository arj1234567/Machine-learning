import pandas as pd
from pathlib import Path

##S = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12],index = ['a','b','c','d','e','f','g','h','i','j','k','l'])
# print(S[1])
# print(S.head())
##print(S.head(10))
##print(S['a'])
##print(S['b'])
##print(S[:2])
##print(S[3:])
##print(S[1:5])
##print(pd.__version__)
##print(max(S))
##print(min(S))
##print(S.mean())

##mydata = {'flower':['Rose','Lilly','Jasmine','Hibiscus'],
##          'color':['Red','Green','Yellow','Blue']}
##print(pd.DataFrame(mydata))

##url_2='https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2021-financial-year-provisional/Download-data/annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
##ufo=pd.read_csv(url_2)
##print(ufo)
##print(ufo.head())
##print(ufo.columns)
##print(ufo['Year'])
##ufo.insert(2,column = "location",value="")
##print(ufo['location'])
##ufo.drop("location",axis="columns",inplace=True)
##print(ufo.columns)
##ufo.drop(['Year','Units'],axis=1,inplace=True)
##print(ufo.columns)
##print(ufo.sort_values(by=["Variable_code"],ascending=False))
##print(ufo.sort_values(by=["Variable_code"],ascending=True))

path2csv = Path("C:/Users/Arjun/Downloads/color/")
csvlist = path2csv.glob("*.csv")
csvs = [pd.read_csv(g) for g in csvlist]
print(csvs)
