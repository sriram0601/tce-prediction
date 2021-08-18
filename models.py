import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def powerPrediction(day,hour,min):
    df=pd.read_csv('tceApril.csv')

    df.drop([306,307],inplace=True)

    newDf=df
    # pd.to_datetime(newDf['Time']) "Will return the DF series into Datetime format" Eg:2018-04-16 15:56:00
    newDf['Day']=pd.to_datetime(newDf['Time']).dt.day
    newDf['Month']=pd.to_datetime(newDf['Time']).dt.month
    newDf['Year']=pd.to_datetime(newDf['Time']).dt.year
    newDf['Hour']=pd.to_datetime(newDf['Time']).dt.hour
    newDf['Minute']=pd.to_datetime(newDf['Time']).dt.minute

    cols=[1,6,9,10]
    df1=df[df.columns[cols]]

    XCols = [1,2,3]
    YCols = [0]
    X = df1[df1.columns[XCols]]
    Y = df1[df1.columns[YCols]]


    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=1)

    rfc = RandomForestRegressor()
    rfc.fit(X_train,Y_train)


    return (rfc.predict([[day,hour,min]])[0])
