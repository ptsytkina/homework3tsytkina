import requests
import pandas as pd

#широта -  49.0390512
#довгота 28.1085937 координати жмеринки. це буде погода в жмеринці
latitude =  49.0352
longitude = 28.114

params = {
"latitude" : latitude, 
"longitude" : longitude,
"hourly": 'temperature_2m,wind_speed_10m', #висота швидкості вітру, висота виміру температури
"timezone" : 'Europe/Moscow' #бачить бог, я не хотіла це писати.
}


url = 'https://api.open-meteo.com/v1/forecast?'


response = requests.get(url, params = params)

if response.status_code == 200:
    data = response.json()


    df = pd.DataFrame({
    "datachas": data['hourly']['time'],
    'temperature':  data['hourly']['temperature_2m'],
    'wind_speed' : data['hourly']['wind_speed_10m']
    })

    df['datachas'] = pd.to_datetime(df['datachas'])
    
    
else:
    print(response.status_code)

print(df.head(168).to_string(index=False))

minimal_temperature = df.head(72)['temperature'].min()
maximum_temperature = df.head(72)['temperature'].max()
mean_temperature = df.head(72)['temperature'].mean()

print("мінімальна температура:", minimal_temperature , "градусів")
print("максимальна температура:", maximum_temperature, "градусів")
print("середня температура:", mean_temperature, "градусів")


print("скільки годин швидкість вітру перевищує загальнусередню швидкість вітру в DataFrame:", (df['wind_speed'] > df['wind_speed'].mean()).sum(), "годин")
#для того щоб додуматись до .mean()).sum() довелося гуглити функціонал pandas та дивитися на приклади підсумувань результату операції (в цій ситуації тру/фолс)