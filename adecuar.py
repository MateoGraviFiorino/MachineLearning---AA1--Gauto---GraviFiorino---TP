#Funciones para convertir el input en una entrada valida para el modelo
def oneHotLocation(df):
    if df.Location.values == 'Adelaide':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Canberra':
        df['Location_Canberra'] = 1, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Cobar':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 1, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0 
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Dartmoor':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 1,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Melbourne':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=1, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Melbourne Airport':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=1,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)
        return df
    elif df.Location.values == 'Mount Gambier':
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=1, 
        df['Location_Sydney']=0
        df=df.drop(['Location'], axis=1)    
        return df
    else:
        df['Location_Canberra'] = 0, 
        df['Location_Cobar'] = 0, 
        df['Location_Dartmoor'] = 0,
        df['Location_Melbourne']=0, 
        df['Location_MelbourneAirport']=0,
        df['Location_MountGambier']=0, 
        df['Location_Sydney']=1
        df=df.drop(['Location'], axis=1)    
        return df

def oneHotWindGustDir(df):
    if df.WindGustDir.values == 'ENE':
        df['WindGustDir_ENE']=1,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    
    elif df.WindGustDir.values == 'ESE':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=1,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df

    elif df.WindGustDir.values == 'N':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=1, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    
    elif df.WindGustDir.values == 'NE':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=1, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df

    elif df.WindGustDir.values == 'NNE':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=1,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    
    elif df.WindGustDir.values == 'NNW':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=1, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df

    elif df.WindGustDir.values == 'NW':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=1, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df

    elif df.WindGustDir.values == 'S':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=1, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'SE':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=1,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'SSE':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=1,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'SSW':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=1, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'SW':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=1, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'W':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=1,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    elif df.WindGustDir.values == 'WNW':
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=1, 
        df['WindGustDir_WSW']=0,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
    else:
        df['WindGustDir_ENE']=0,
        df['WindGustDir_ESE']=0,
        df['WindGustDir_N']=0, 
        df['WindGustDir_NE']=0, 
        df['WindGustDir_NNE']=0,
        df['WindGustDir_NNW']=0, 
        df['WindGustDir_NW']=0, 
        df['WindGustDir_S']=0, 
        df['WindGustDir_SE']=0,
        df['WindGustDir_SSE']=0,
        df['WindGustDir_SSW']=0, 
        df['WindGustDir_SW']=0, 
        df['WindGustDir_W']=0,
        df['WindGustDir_WNW']=0, 
        df['WindGustDir_WSW']=1,
        df = df.drop(['WindGustDir'], axis = 1)
        return df
def oneHotRainToday(df):
    if df.RainToday.values == 'Yes':
        df['RainToday_Yes']=1
        df = df.drop(['RainToday'], axis=1)
        return df
    else:
        df['RainToday_Yes']=0
        df = df.drop(['RainToday'], axis=1)
        return df
def oneHotWindDir9am(df):
    if df.WindDir9am.values == 'ENE':
        df['WindDir9am_ENE']=1,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    
    elif df.WindDir9am.values == 'ESE':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=1,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df

    elif df.WindDir9am.values == 'N':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=1, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    
    elif df.WindDir9am.values == 'NE':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=1, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df

    elif df.WindDir9am.values == 'NNE':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=1,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    
    elif df.WindDir9am.values == 'NNW':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=1, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df

    elif df.WindDir9am.values == 'NW':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=1, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df

    elif df.WindDir9am.values == 'S':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=1, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'SE':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=1,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'SSE':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=1,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'SSW':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=1, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'SW':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=1, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'W':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=1,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    elif df.WindDir9am.values == 'WNW':
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=1, 
        df['WindDir9am_WSW']=0,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
    else:
        df['WindDir9am_ENE']=0,
        df['WindDir9am_ESE']=0,
        df['WindDir9am_N']=0, 
        df['WindDir9am_NE']=0, 
        df['WindDir9am_NNE']=0,
        df['WindDir9am_NNW']=0, 
        df['WindDir9am_NW']=0, 
        df['WindDir9am_S']=0, 
        df['WindDir9am_SE']=0,
        df['WindDir9am_SSE']=0,
        df['WindDir9am_SSW']=0, 
        df['WindDir9am_SW']=0, 
        df['WindDir9am_W']=0,
        df['WindDir9am_WNW']=0, 
        df['WindDir9am_WSW']=1,
        df = df.drop(['WindDir9am'], axis = 1)
        return df
def oneHotWindDir3pm(df):
    if df.WindDir3pm.values == 'ENE':
        df['WindDir3pm_ENE']=1,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    
    elif df.WindDir3pm.values == 'ESE':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=1,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df

    elif df.WindDir3pm.values == 'N':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=1, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    
    elif df.WindDir3pm.values == 'NE':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=1, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df

    elif df.WindDir3pm.values == 'NNE':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=1,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    
    elif df.WindDir3pm.values == 'NNW':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=1, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df

    elif df.WindDir3pm.values == 'NW':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=1, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df

    elif df.WindDir3pm.values == 'S':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=1, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'SE':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=1,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'SSE':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=1,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'SSW':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=1, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'SW':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=1, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'W':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=1,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    elif df.WindDir3pm.values == 'WNW':
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=1, 
        df['WindDir3pm_WSW']=0,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
    else:
        df['WindDir3pm_ENE']=0,
        df['WindDir3pm_ESE']=0,
        df['WindDir3pm_N']=0, 
        df['WindDir3pm_NE']=0, 
        df['WindDir3pm_NNE']=0,
        df['WindDir3pm_NNW']=0, 
        df['WindDir3pm_NW']=0, 
        df['WindDir3pm_S']=0, 
        df['WindDir3pm_SE']=0,
        df['WindDir3pm_SSE']=0,
        df['WindDir3pm_SSW']=0, 
        df['WindDir3pm_SW']=0, 
        df['WindDir3pm_W']=0,
        df['WindDir3pm_WNW']=0, 
        df['WindDir3pm_WSW']=1,
        df = df.drop(['WindDir3pm'], axis = 1)
        return df
def oneHotSeason(df):
    if df.Season.values == 'Otoño':
        df['Season_Otoño']=1,
        df['Season_Primavera']=0,
        df['Season_Verano']=0,
        df = df.drop(['Season'], axis = 1)
        return df
    elif df.Season.values == 'Primavera':
        df['Season_Otoño']=0,
        df['Season_Primavera']=1,
        df['Season_Verano']=0,
        df = df.drop(['Season'], axis = 1)
        return df
    elif df.Season.values == 'Verano':
        df['Season_Otoño']=0,
        df['Season_Primavera']=0,
        df['Season_Verano']=1,
        df = df.drop(['Season'], axis = 1)
        return df
    else:
        df['Season_Otoño']=0,
        df['Season_Primavera']=0,
        df['Season_Verano']=0,
        df = df.drop(['Season'], axis = 1)
        return df

def adecuar(data:dict):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler

    df = pd.DataFrame(data)

    df_encoded = oneHotSeason(oneHotWindDir3pm(oneHotWindDir9am(oneHotRainToday(oneHotWindGustDir(oneHotLocation(df))))))
    scaler = StandardScaler()
    scaler.fit(df_encoded)
    df_scaled = scaler.transform(df_encoded)

    return df_scaled
