#We did Subtask 1 in the end
import numpy as np
import pandas as pd

#Subtask 2
df_weather = pd.read_excel("weather_dataset_stage1.xls")
#Below code will remove the single inverted comma
df_weather = df_weather.replace({'\'': '', ';':''}, regex=True)
#Below code will remove the duplicate rows
df_weather = df_weather.drop_duplicates()
#Below code will transpose the dataframe and will check the duplicate columns
df_weather.T.duplicated()
#Below code will remove the duplicate columns
df_weather = df_weather.T.drop_duplicates().T

#Subtask 3
#Replacing with appropriate labels
columns_list = ["DATE", "TEMPERATURE", "AVG_HUMIDITY_PERC", "AVG_DEWPOINT_F","AVG_BAROMETER_IN", "AVG_WINDSPEED_MPH", "AVG_GUSTSPEED_MPH", "AVG_DIRECTION_DEG","RAINFALL_MONTH", "RAINFALL_YEAR", "MAX_RAIN_PER_MINUTE", "MAX_TEMP_F","MIN_TEMP_F","MAX_HUMIDITY_PERC", "MIN_HUMIDITY_PERC", "MAX_PRESSURE_IN", "MIN_PRESSURE_IN", "MAX_WINDSPEED_MPH", "MAX_GUSTSPEED_MPH","MAX_HEAT_INDEX_F", "MONTH","DIFF_PRESSURE_IN"]
df_weather.columns = columns_list

#Subtask 4
#Encoding into suitable data type
for i in columns_list[1:]:
        df_weather[i] = pd.to_numeric(df_weather[i])

#Subtask 1
#Correct years
pd.set_option('mode.chained_assignment', None)
year = 2022
for i in range(len(df_weather.DATE)):
    if i == 0:
        df_weather['DATE'].loc[i] = df_weather['DATE'].loc[i].replace('2022', str(year))
    else:
        if df_weather.MONTH.loc[i] >= df_weather.MONTH.loc[i-1]:
            df_weather['DATE'].loc[i] = df_weather['DATE'].loc[i].replace('2022',str(year))
        else:
            year += 1
            df_weather['DATE'].loc[i] = df_weather['DATE'].loc[i].replace('2022',str(year))

#filter invalid dates
df_weather = df_weather[pd.to_datetime(df_weather['DATE'], errors='coerce').notna()]

#exporting csv file
df_weather.to_csv("cleaned_weather.dataset.csv", index = False)