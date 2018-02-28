

```python
print("Analysis\n")
print("Trend 1: The temperature on this day was much higher on average at and below the equator than above it. At about 20 degrees latitude, we see a drop in temperature. \n")
print("Trend 2: Humidity and cloudiness do not seem to be very affected by latitudinal position. Though, at higher lines of latitude there do seem to be more locations registering higher humidity on this day.\n")
print("Trend 3: Wind speed also does not seem to be very affected by latitudinal position. \n")
```

    Analysis
    
    Trend 1: The temperature on this day was much higher on average at and below the equator than above it. At about 20 degrees latitude, we see a drop in temperature. 
    
    Trend 2: Humidity and cloudiness do not seem to be very affected by latitudinal position. Though, at higher lines of latitude there do seem to be more locations registering higher humidity on this day.
    
    Trend 3: Wind speed also does not seem to be very affected by latitudinal position. 
    
    


```python
import json
import matplotlib.pyplot as plt
import pandas as pd
import random
import requests as req
from citipy import citipy as cp
```


```python
api_key = "c2ebe13b2ca2223ec9fac09b14ce02ee"
url = "http://api.openweathermap.org/data/2.5/weather?"
```


```python
cities_list = []
country_list = []
while len(cities_list) < 1000:
    city = cp.nearest_city(random.randint(-90, 90), random.randint(-180, 180))
    name = city.city_name
    country = city.country_code
    if name not in cities_list:
        cities_list.append(name)
        country_list.append(country)
```


```python
city_df = pd.DataFrame({"City Name": cities_list, "Country Code": country_list, "Temperature (F)": "", "Humidity (%)": "", "Cloudiness (%)": "", "Wind Speed (MPH)": "", "Latitude": "", "Longitude": ""})
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Cloudiness (%)</th>
      <th>Country Code</th>
      <th>Humidity (%)</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature (F)</th>
      <th>Wind Speed (MPH)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>faya</td>
      <td></td>
      <td>td</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>khatima</td>
      <td></td>
      <td>in</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>seoul</td>
      <td></td>
      <td>kr</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>aasiaat</td>
      <td></td>
      <td>gl</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>torbay</td>
      <td></td>
      <td>ca</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
row_count = 0

for index, row in city_df.iterrows():
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&units=%s&appid=%s" % (row["City Name"], row["Country Code"], "imperial", api_key)
    weather_json = req.get(weather_url).json()
    print("Processing - City Name: " + row["City Name"] + "\n" + "City Number: #" + str(row_count) + "\n" + "City URL: " + weather_url)
    row_count += 1
    
    try:
        temp = weather_json["main"]["temp"]
        humid = weather_json["main"]["humidity"]
        speed = weather_json["wind"]["speed"]
        clouds = weather_json["clouds"]["all"]
        lat = weather_json["coord"]["lat"]
        lon = weather_json["coord"]["lon"]
        
        city_df.at[index, "Temperature (F)"] = temp
        city_df.at[index, "Humidity (%)"] = humid
        city_df.at[index, "Wind Speed (MPH)"] = speed
        city_df.at[index, "Cloudiness (%)"] = clouds
        city_df.at[index, "Latitude"] = lat
        city_df.at[index, "Longitude"] = lon
        
    except:
        print("ERROR WITH CITY DATA, SKIPPING")
        city_df.at[index, "Latitude"] = "N/A"
        continue
```

    Processing - City Name: faya
    City Number: #0
    City URL: http://api.openweathermap.org/data/2.5/weather?q=faya,td&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: khatima
    City Number: #1
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khatima,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: seoul
    City Number: #2
    City URL: http://api.openweathermap.org/data/2.5/weather?q=seoul,kr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: aasiaat
    City Number: #3
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aasiaat,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: torbay
    City Number: #4
    City URL: http://api.openweathermap.org/data/2.5/weather?q=torbay,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: codrington
    City Number: #5
    City URL: http://api.openweathermap.org/data/2.5/weather?q=codrington,ag&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: loja
    City Number: #6
    City URL: http://api.openweathermap.org/data/2.5/weather?q=loja,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: castro
    City Number: #7
    City URL: http://api.openweathermap.org/data/2.5/weather?q=castro,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: narsaq
    City Number: #8
    City URL: http://api.openweathermap.org/data/2.5/weather?q=narsaq,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: barentsburg
    City Number: #9
    City URL: http://api.openweathermap.org/data/2.5/weather?q=barentsburg,sj&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: albany
    City Number: #10
    City URL: http://api.openweathermap.org/data/2.5/weather?q=albany,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port alfred
    City Number: #11
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port alfred,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: attawapiskat
    City Number: #12
    City URL: http://api.openweathermap.org/data/2.5/weather?q=attawapiskat,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: bluff
    City Number: #13
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bluff,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto ayora
    City Number: #14
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto ayora,ec&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: qaanaaq
    City Number: #15
    City URL: http://api.openweathermap.org/data/2.5/weather?q=qaanaaq,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ahipara
    City Number: #16
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ahipara,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: punta arenas
    City Number: #17
    City URL: http://api.openweathermap.org/data/2.5/weather?q=punta arenas,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shingu
    City Number: #18
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shingu,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bethel
    City Number: #19
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bethel,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yellowknife
    City Number: #20
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yellowknife,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: itaituba
    City Number: #21
    City URL: http://api.openweathermap.org/data/2.5/weather?q=itaituba,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: matay
    City Number: #22
    City URL: http://api.openweathermap.org/data/2.5/weather?q=matay,eg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: carlton
    City Number: #23
    City URL: http://api.openweathermap.org/data/2.5/weather?q=carlton,gb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chokurdakh
    City Number: #24
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chokurdakh,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sola
    City Number: #25
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sola,vu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: anadyr
    City Number: #26
    City URL: http://api.openweathermap.org/data/2.5/weather?q=anadyr,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: arraial do cabo
    City Number: #27
    City URL: http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nanakuli
    City Number: #28
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nanakuli,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: khatanga
    City Number: #29
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khatanga,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mataura
    City Number: #30
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mataura,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sobolevo
    City Number: #31
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sobolevo,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: upernavik
    City Number: #32
    City URL: http://api.openweathermap.org/data/2.5/weather?q=upernavik,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ushuaia
    City Number: #33
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ushuaia,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: fevralsk
    City Number: #34
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fevralsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tokur
    City Number: #35
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tokur,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: avarua
    City Number: #36
    City URL: http://api.openweathermap.org/data/2.5/weather?q=avarua,ck&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kruisfontein
    City Number: #37
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kruisfontein,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: provideniya
    City Number: #38
    City URL: http://api.openweathermap.org/data/2.5/weather?q=provideniya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marcona
    City Number: #39
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marcona,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: rikitea
    City Number: #40
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rikitea,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alta floresta
    City Number: #41
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alta floresta,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: severo-kurilsk
    City Number: #42
    City URL: http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: roebourne
    City Number: #43
    City URL: http://api.openweathermap.org/data/2.5/weather?q=roebourne,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hilo
    City Number: #44
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hilo,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: balkhash
    City Number: #45
    City URL: http://api.openweathermap.org/data/2.5/weather?q=balkhash,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ancud
    City Number: #46
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ancud,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cape town
    City Number: #47
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cape town,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mitsamiouli
    City Number: #48
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mitsamiouli,km&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: okha
    City Number: #49
    City URL: http://api.openweathermap.org/data/2.5/weather?q=okha,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: busselton
    City Number: #50
    City URL: http://api.openweathermap.org/data/2.5/weather?q=busselton,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: samusu
    City Number: #51
    City URL: http://api.openweathermap.org/data/2.5/weather?q=samusu,ws&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: saint george
    City Number: #52
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint george,bm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-joseph
    City Number: #53
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-joseph,re&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: oranjestad
    City Number: #54
    City URL: http://api.openweathermap.org/data/2.5/weather?q=oranjestad,aw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: qaqortoq
    City Number: #55
    City URL: http://api.openweathermap.org/data/2.5/weather?q=qaqortoq,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nizhniy odes
    City Number: #56
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nizhniy odes,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kloulklubed
    City Number: #57
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kloulklubed,pw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: esperance
    City Number: #58
    City URL: http://api.openweathermap.org/data/2.5/weather?q=esperance,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tarudant
    City Number: #59
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tarudant,ma&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: ayan
    City Number: #60
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ayan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: broome
    City Number: #61
    City URL: http://api.openweathermap.org/data/2.5/weather?q=broome,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kapaa
    City Number: #62
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kapaa,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vaini
    City Number: #63
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vaini,to&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: leshukonskoye
    City Number: #64
    City URL: http://api.openweathermap.org/data/2.5/weather?q=leshukonskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ponto novo
    City Number: #65
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ponto novo,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: srednekolymsk
    City Number: #66
    City URL: http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: divnomorskoye
    City Number: #67
    City URL: http://api.openweathermap.org/data/2.5/weather?q=divnomorskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porteirinha
    City Number: #68
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porteirinha,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-philippe
    City Number: #69
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-philippe,re&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: east london
    City Number: #70
    City URL: http://api.openweathermap.org/data/2.5/weather?q=east london,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: thompson
    City Number: #71
    City URL: http://api.openweathermap.org/data/2.5/weather?q=thompson,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: olafsvik
    City Number: #72
    City URL: http://api.openweathermap.org/data/2.5/weather?q=olafsvik,is&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: new norfolk
    City Number: #73
    City URL: http://api.openweathermap.org/data/2.5/weather?q=new norfolk,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jeremie
    City Number: #74
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jeremie,ht&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: barrow
    City Number: #75
    City URL: http://api.openweathermap.org/data/2.5/weather?q=barrow,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: illoqqortoormiut
    City Number: #76
    City URL: http://api.openweathermap.org/data/2.5/weather?q=illoqqortoormiut,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: auki
    City Number: #77
    City URL: http://api.openweathermap.org/data/2.5/weather?q=auki,sb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hermanus
    City Number: #78
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hermanus,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lucapa
    City Number: #79
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lucapa,ao&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tuktoyaktuk
    City Number: #80
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sinazongwe
    City Number: #81
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sinazongwe,zm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: verkhoyansk
    City Number: #82
    City URL: http://api.openweathermap.org/data/2.5/weather?q=verkhoyansk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: korla
    City Number: #83
    City URL: http://api.openweathermap.org/data/2.5/weather?q=korla,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nizhneyansk
    City Number: #84
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nizhneyansk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: airai
    City Number: #85
    City URL: http://api.openweathermap.org/data/2.5/weather?q=airai,pw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: acacias
    City Number: #86
    City URL: http://api.openweathermap.org/data/2.5/weather?q=acacias,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: husavik
    City Number: #87
    City URL: http://api.openweathermap.org/data/2.5/weather?q=husavik,is&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hobart
    City Number: #88
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hobart,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bobrovka
    City Number: #89
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bobrovka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sandy bay
    City Number: #90
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sandy bay,hn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: faro
    City Number: #91
    City URL: http://api.openweathermap.org/data/2.5/weather?q=faro,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: beringovskiy
    City Number: #92
    City URL: http://api.openweathermap.org/data/2.5/weather?q=beringovskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: parangan
    City Number: #93
    City URL: http://api.openweathermap.org/data/2.5/weather?q=parangan,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: teguldet
    City Number: #94
    City URL: http://api.openweathermap.org/data/2.5/weather?q=teguldet,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wentzville
    City Number: #95
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wentzville,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kodiak
    City Number: #96
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kodiak,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: harper
    City Number: #97
    City URL: http://api.openweathermap.org/data/2.5/weather?q=harper,lr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: letterkenny
    City Number: #98
    City URL: http://api.openweathermap.org/data/2.5/weather?q=letterkenny,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zapolyarnyy
    City Number: #99
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zapolyarnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rossland
    City Number: #100
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rossland,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maragogi
    City Number: #101
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maragogi,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sentyabrskiy
    City Number: #102
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sentyabrskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: oistins
    City Number: #103
    City URL: http://api.openweathermap.org/data/2.5/weather?q=oistins,bb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: victoria
    City Number: #104
    City URL: http://api.openweathermap.org/data/2.5/weather?q=victoria,sc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tuatapere
    City Number: #105
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tuatapere,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nantucket
    City Number: #106
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nantucket,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dwarka
    City Number: #107
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dwarka,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bredasdorp
    City Number: #108
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bredasdorp,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tasiilaq
    City Number: #109
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tasiilaq,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chuy
    City Number: #110
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chuy,uy&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahebourg
    City Number: #111
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahebourg,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: oktyabrskiy
    City Number: #112
    City URL: http://api.openweathermap.org/data/2.5/weather?q=oktyabrskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coquimbo
    City Number: #113
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coquimbo,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chimoio
    City Number: #114
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chimoio,mz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: grand river south east
    City Number: #115
    City URL: http://api.openweathermap.org/data/2.5/weather?q=grand river south east,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: huarmey
    City Number: #116
    City URL: http://api.openweathermap.org/data/2.5/weather?q=huarmey,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: skalistyy
    City Number: #117
    City URL: http://api.openweathermap.org/data/2.5/weather?q=skalistyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: eldikan
    City Number: #118
    City URL: http://api.openweathermap.org/data/2.5/weather?q=eldikan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sao gabriel da cachoeira
    City Number: #119
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sao gabriel da cachoeira,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: iquitos
    City Number: #120
    City URL: http://api.openweathermap.org/data/2.5/weather?q=iquitos,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pemangkat
    City Number: #121
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pemangkat,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: lebu
    City Number: #122
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lebu,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lompoc
    City Number: #123
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lompoc,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: laguna
    City Number: #124
    City URL: http://api.openweathermap.org/data/2.5/weather?q=laguna,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: mar del plata
    City Number: #125
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mar del plata,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa eulalia del rio
    City Number: #126
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa eulalia del rio,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: paita
    City Number: #127
    City URL: http://api.openweathermap.org/data/2.5/weather?q=paita,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kingaroy
    City Number: #128
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kingaroy,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pisco
    City Number: #129
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pisco,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: taolanaro
    City Number: #130
    City URL: http://api.openweathermap.org/data/2.5/weather?q=taolanaro,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: homer
    City Number: #131
    City URL: http://api.openweathermap.org/data/2.5/weather?q=homer,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lorengau
    City Number: #132
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lorengau,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jamestown
    City Number: #133
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jamestown,sh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: eureka
    City Number: #134
    City URL: http://api.openweathermap.org/data/2.5/weather?q=eureka,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kozhva
    City Number: #135
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kozhva,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saleaula
    City Number: #136
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saleaula,ws&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: santa cruz
    City Number: #137
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa cruz,cr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tilichiki
    City Number: #138
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tilichiki,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: plettenberg bay
    City Number: #139
    City URL: http://api.openweathermap.org/data/2.5/weather?q=plettenberg bay,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yeppoon
    City Number: #140
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yeppoon,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alofi
    City Number: #141
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alofi,nu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: preobrazheniye
    City Number: #142
    City URL: http://api.openweathermap.org/data/2.5/weather?q=preobrazheniye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kourou
    City Number: #143
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kourou,gf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pandan
    City Number: #144
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pandan,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: umm kaddadah
    City Number: #145
    City URL: http://api.openweathermap.org/data/2.5/weather?q=umm kaddadah,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hasaki
    City Number: #146
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hasaki,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: faanui
    City Number: #147
    City URL: http://api.openweathermap.org/data/2.5/weather?q=faanui,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saldanha
    City Number: #148
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saldanha,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: medicine hat
    City Number: #149
    City URL: http://api.openweathermap.org/data/2.5/weather?q=medicine hat,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: litovko
    City Number: #150
    City URL: http://api.openweathermap.org/data/2.5/weather?q=litovko,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ruatoria
    City Number: #151
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ruatoria,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: atuona
    City Number: #152
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atuona,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: aykhal
    City Number: #153
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aykhal,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cidreira
    City Number: #154
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cidreira,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: arvika
    City Number: #155
    City URL: http://api.openweathermap.org/data/2.5/weather?q=arvika,se&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pangnirtung
    City Number: #156
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pangnirtung,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hamilton
    City Number: #157
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hamilton,bm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: belushya guba
    City Number: #158
    City URL: http://api.openweathermap.org/data/2.5/weather?q=belushya guba,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: butaritari
    City Number: #159
    City URL: http://api.openweathermap.org/data/2.5/weather?q=butaritari,ki&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: salalah
    City Number: #160
    City URL: http://api.openweathermap.org/data/2.5/weather?q=salalah,om&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gat
    City Number: #161
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gat,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: saint-augustin
    City Number: #162
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-augustin,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kahului
    City Number: #163
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kahului,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ahuimanu
    City Number: #164
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ahuimanu,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pecos
    City Number: #165
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pecos,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maloshuyka
    City Number: #166
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maloshuyka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: karratha
    City Number: #167
    City URL: http://api.openweathermap.org/data/2.5/weather?q=karratha,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kavaratti
    City Number: #168
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kavaratti,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-tsilma
    City Number: #169
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-tsilma,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: komsomolskiy
    City Number: #170
    City URL: http://api.openweathermap.org/data/2.5/weather?q=komsomolskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cabo san lucas
    City Number: #171
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cabo san lucas,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: fuerte olimpo
    City Number: #172
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fuerte olimpo,py&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: carnarvon
    City Number: #173
    City URL: http://api.openweathermap.org/data/2.5/weather?q=carnarvon,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nome
    City Number: #174
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nome,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tuljapur
    City Number: #175
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tuljapur,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: berberati
    City Number: #176
    City URL: http://api.openweathermap.org/data/2.5/weather?q=berberati,cf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: brae
    City Number: #177
    City URL: http://api.openweathermap.org/data/2.5/weather?q=brae,gb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: beloha
    City Number: #178
    City URL: http://api.openweathermap.org/data/2.5/weather?q=beloha,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: huaiyuan
    City Number: #179
    City URL: http://api.openweathermap.org/data/2.5/weather?q=huaiyuan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: norman wells
    City Number: #180
    City URL: http://api.openweathermap.org/data/2.5/weather?q=norman wells,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port hardy
    City Number: #181
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port hardy,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: goiatuba
    City Number: #182
    City URL: http://api.openweathermap.org/data/2.5/weather?q=goiatuba,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: freeport
    City Number: #183
    City URL: http://api.openweathermap.org/data/2.5/weather?q=freeport,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sao jose da coroa grande
    City Number: #184
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sao jose da coroa grande,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dingle
    City Number: #185
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dingle,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: woodward
    City Number: #186
    City URL: http://api.openweathermap.org/data/2.5/weather?q=woodward,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: portland
    City Number: #187
    City URL: http://api.openweathermap.org/data/2.5/weather?q=portland,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: asau
    City Number: #188
    City URL: http://api.openweathermap.org/data/2.5/weather?q=asau,tv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tsihombe
    City Number: #189
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tsihombe,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: longlac
    City Number: #190
    City URL: http://api.openweathermap.org/data/2.5/weather?q=longlac,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: cap malheureux
    City Number: #191
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cap malheureux,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wyndham
    City Number: #192
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wyndham,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kavieng
    City Number: #193
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kavieng,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: senneterre
    City Number: #194
    City URL: http://api.openweathermap.org/data/2.5/weather?q=senneterre,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san carlos de bariloche
    City Number: #195
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san carlos de bariloche,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kaitangata
    City Number: #196
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kaitangata,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: georgetown
    City Number: #197
    City URL: http://api.openweathermap.org/data/2.5/weather?q=georgetown,sh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wagar
    City Number: #198
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wagar,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: muroto
    City Number: #199
    City URL: http://api.openweathermap.org/data/2.5/weather?q=muroto,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chapais
    City Number: #200
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chapais,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: qiongshan
    City Number: #201
    City URL: http://api.openweathermap.org/data/2.5/weather?q=qiongshan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: anchorage
    City Number: #202
    City URL: http://api.openweathermap.org/data/2.5/weather?q=anchorage,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: fairbanks
    City Number: #203
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fairbanks,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kandrian
    City Number: #204
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kandrian,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alyangula
    City Number: #205
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alyangula,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ribeira grande
    City Number: #206
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ribeira grande,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: liwale
    City Number: #207
    City URL: http://api.openweathermap.org/data/2.5/weather?q=liwale,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: licata
    City Number: #208
    City URL: http://api.openweathermap.org/data/2.5/weather?q=licata,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mangan
    City Number: #209
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mangan,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: souillac
    City Number: #210
    City URL: http://api.openweathermap.org/data/2.5/weather?q=souillac,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: amderma
    City Number: #211
    City URL: http://api.openweathermap.org/data/2.5/weather?q=amderma,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sao joao da barra
    City Number: #212
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gornopravdinsk
    City Number: #213
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gornopravdinsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tengzhou
    City Number: #214
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tengzhou,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: malwan
    City Number: #215
    City URL: http://api.openweathermap.org/data/2.5/weather?q=malwan,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: muros
    City Number: #216
    City URL: http://api.openweathermap.org/data/2.5/weather?q=muros,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port elizabeth
    City Number: #217
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port elizabeth,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: verkhnyaya inta
    City Number: #218
    City URL: http://api.openweathermap.org/data/2.5/weather?q=verkhnyaya inta,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-pierre
    City Number: #219
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-pierre,pm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san cristobal
    City Number: #220
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san cristobal,ec&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mys shmidta
    City Number: #221
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mys shmidta,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: akcakoca
    City Number: #222
    City URL: http://api.openweathermap.org/data/2.5/weather?q=akcakoca,tr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bandarbeyla
    City Number: #223
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bandarbeyla,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: unai
    City Number: #224
    City URL: http://api.openweathermap.org/data/2.5/weather?q=unai,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: biltine
    City Number: #225
    City URL: http://api.openweathermap.org/data/2.5/weather?q=biltine,td&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port lincoln
    City Number: #226
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port lincoln,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nikolsk
    City Number: #227
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nikolsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ilulissat
    City Number: #228
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ilulissat,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: valparaiso
    City Number: #229
    City URL: http://api.openweathermap.org/data/2.5/weather?q=valparaiso,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: champerico
    City Number: #230
    City URL: http://api.openweathermap.org/data/2.5/weather?q=champerico,gt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: naze
    City Number: #231
    City URL: http://api.openweathermap.org/data/2.5/weather?q=naze,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: palatka
    City Number: #232
    City URL: http://api.openweathermap.org/data/2.5/weather?q=palatka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hobyo
    City Number: #233
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hobyo,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san patricio
    City Number: #234
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san patricio,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: richards bay
    City Number: #235
    City URL: http://api.openweathermap.org/data/2.5/weather?q=richards bay,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: aklavik
    City Number: #236
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aklavik,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: petit goave
    City Number: #237
    City URL: http://api.openweathermap.org/data/2.5/weather?q=petit goave,ht&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: riihimaki
    City Number: #238
    City URL: http://api.openweathermap.org/data/2.5/weather?q=riihimaki,fi&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nabire
    City Number: #239
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nabire,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: margate
    City Number: #240
    City URL: http://api.openweathermap.org/data/2.5/weather?q=margate,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: iqaluit
    City Number: #241
    City URL: http://api.openweathermap.org/data/2.5/weather?q=iqaluit,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wicklow
    City Number: #242
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wicklow,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chitral
    City Number: #243
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chitral,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wanning
    City Number: #244
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wanning,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ponta do sol
    City Number: #245
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ponta do sol,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: klaksvik
    City Number: #246
    City URL: http://api.openweathermap.org/data/2.5/weather?q=klaksvik,fo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sayanskiy
    City Number: #247
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sayanskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: bathsheba
    City Number: #248
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bathsheba,bb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saskylakh
    City Number: #249
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saskylakh,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: soe
    City Number: #250
    City URL: http://api.openweathermap.org/data/2.5/weather?q=soe,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: haines junction
    City Number: #251
    City URL: http://api.openweathermap.org/data/2.5/weather?q=haines junction,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: palabuhanratu
    City Number: #252
    City URL: http://api.openweathermap.org/data/2.5/weather?q=palabuhanratu,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tiksi
    City Number: #253
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tiksi,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bilma
    City Number: #254
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bilma,ne&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san miguel
    City Number: #255
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san miguel,pa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: luocheng
    City Number: #256
    City URL: http://api.openweathermap.org/data/2.5/weather?q=luocheng,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: magistralnyy
    City Number: #257
    City URL: http://api.openweathermap.org/data/2.5/weather?q=magistralnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: umm lajj
    City Number: #258
    City URL: http://api.openweathermap.org/data/2.5/weather?q=umm lajj,sa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-ilimsk
    City Number: #259
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-ilimsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kiunga
    City Number: #260
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kiunga,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vila franca do campo
    City Number: #261
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: linxia
    City Number: #262
    City URL: http://api.openweathermap.org/data/2.5/weather?q=linxia,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: camacha
    City Number: #263
    City URL: http://api.openweathermap.org/data/2.5/weather?q=camacha,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa rosa
    City Number: #264
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa rosa,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gladstone
    City Number: #265
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gladstone,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: betanzos
    City Number: #266
    City URL: http://api.openweathermap.org/data/2.5/weather?q=betanzos,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: owando
    City Number: #267
    City URL: http://api.openweathermap.org/data/2.5/weather?q=owando,cg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cairns
    City Number: #268
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cairns,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chute-aux-outardes
    City Number: #269
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chute-aux-outardes,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ranong
    City Number: #270
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ranong,th&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hithadhoo
    City Number: #271
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hithadhoo,mv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-paul
    City Number: #272
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-paul,re&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tura
    City Number: #273
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tura,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: parkes
    City Number: #274
    City URL: http://api.openweathermap.org/data/2.5/weather?q=parkes,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ostrovnoy
    City Number: #275
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ostrovnoy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: waipawa
    City Number: #276
    City URL: http://api.openweathermap.org/data/2.5/weather?q=waipawa,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: khasan
    City Number: #277
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khasan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: arman
    City Number: #278
    City URL: http://api.openweathermap.org/data/2.5/weather?q=arman,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: arlit
    City Number: #279
    City URL: http://api.openweathermap.org/data/2.5/weather?q=arlit,ne&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marawi
    City Number: #280
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marawi,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nguiu
    City Number: #281
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nguiu,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: pochutla
    City Number: #282
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pochutla,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: batagay-alyta
    City Number: #283
    City URL: http://api.openweathermap.org/data/2.5/weather?q=batagay-alyta,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rio grande
    City Number: #284
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rio grande,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: leningradskiy
    City Number: #285
    City URL: http://api.openweathermap.org/data/2.5/weather?q=leningradskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: poum
    City Number: #286
    City URL: http://api.openweathermap.org/data/2.5/weather?q=poum,nc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alpena
    City Number: #287
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alpena,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: verkhnyaya toyma
    City Number: #288
    City URL: http://api.openweathermap.org/data/2.5/weather?q=verkhnyaya toyma,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: juegang
    City Number: #289
    City URL: http://api.openweathermap.org/data/2.5/weather?q=juegang,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: anshun
    City Number: #290
    City URL: http://api.openweathermap.org/data/2.5/weather?q=anshun,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bridlington
    City Number: #291
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bridlington,gb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kariba
    City Number: #292
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kariba,zw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vila do maio
    City Number: #293
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vila do maio,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sayville
    City Number: #294
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sayville,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: henties bay
    City Number: #295
    City URL: http://api.openweathermap.org/data/2.5/weather?q=henties bay,na&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: abu jubayhah
    City Number: #296
    City URL: http://api.openweathermap.org/data/2.5/weather?q=abu jubayhah,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: camana
    City Number: #297
    City URL: http://api.openweathermap.org/data/2.5/weather?q=camana,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: port-cartier
    City Number: #298
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port-cartier,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bintulu
    City Number: #299
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bintulu,my&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porto novo
    City Number: #300
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porto novo,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cherskiy
    City Number: #301
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cherskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dikson
    City Number: #302
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dikson,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kalmunai
    City Number: #303
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kalmunai,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pitea
    City Number: #304
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pitea,se&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mpanda
    City Number: #305
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mpanda,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: suslovo
    City Number: #306
    City URL: http://api.openweathermap.org/data/2.5/weather?q=suslovo,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kathmandu
    City Number: #307
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kathmandu,np&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sita road
    City Number: #308
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sita road,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: karur
    City Number: #309
    City URL: http://api.openweathermap.org/data/2.5/weather?q=karur,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bud
    City Number: #310
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bud,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: byron bay
    City Number: #311
    City URL: http://api.openweathermap.org/data/2.5/weather?q=byron bay,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: policoro
    City Number: #312
    City URL: http://api.openweathermap.org/data/2.5/weather?q=policoro,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la peca
    City Number: #313
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la peca,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mikun
    City Number: #314
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mikun,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: manggar
    City Number: #315
    City URL: http://api.openweathermap.org/data/2.5/weather?q=manggar,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: samarai
    City Number: #316
    City URL: http://api.openweathermap.org/data/2.5/weather?q=samarai,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: adrar
    City Number: #317
    City URL: http://api.openweathermap.org/data/2.5/weather?q=adrar,dz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bauchi
    City Number: #318
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bauchi,ng&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: farafangana
    City Number: #319
    City URL: http://api.openweathermap.org/data/2.5/weather?q=farafangana,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: valvedditturai
    City Number: #320
    City URL: http://api.openweathermap.org/data/2.5/weather?q=valvedditturai,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bolungarvik
    City Number: #321
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bolungarvik,is&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: mandurah
    City Number: #322
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mandurah,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kirakira
    City Number: #323
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kirakira,sb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: blagoveshchenka
    City Number: #324
    City URL: http://api.openweathermap.org/data/2.5/weather?q=blagoveshchenka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahuva
    City Number: #325
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahuva,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jieshi
    City Number: #326
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jieshi,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sorvag
    City Number: #327
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sorvag,fo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: yulara
    City Number: #328
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yulara,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pacific grove
    City Number: #329
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pacific grove,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tarauaca
    City Number: #330
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tarauaca,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tukrah
    City Number: #331
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tukrah,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: atherton
    City Number: #332
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atherton,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: longyearbyen
    City Number: #333
    City URL: http://api.openweathermap.org/data/2.5/weather?q=longyearbyen,sj&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: talnakh
    City Number: #334
    City URL: http://api.openweathermap.org/data/2.5/weather?q=talnakh,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa marta
    City Number: #335
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa marta,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: grindavik
    City Number: #336
    City URL: http://api.openweathermap.org/data/2.5/weather?q=grindavik,is&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: acarau
    City Number: #337
    City URL: http://api.openweathermap.org/data/2.5/weather?q=acarau,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: cayenne
    City Number: #338
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cayenne,gf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ruteng
    City Number: #339
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ruteng,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: broken hill
    City Number: #340
    City URL: http://api.openweathermap.org/data/2.5/weather?q=broken hill,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ystad
    City Number: #341
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ystad,se&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nardaran
    City Number: #342
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nardaran,az&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: corning
    City Number: #343
    City URL: http://api.openweathermap.org/data/2.5/weather?q=corning,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ossora
    City Number: #344
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ossora,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: along
    City Number: #345
    City URL: http://api.openweathermap.org/data/2.5/weather?q=along,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: isangel
    City Number: #346
    City URL: http://api.openweathermap.org/data/2.5/weather?q=isangel,vu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lagoa
    City Number: #347
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lagoa,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kaeo
    City Number: #348
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kaeo,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vila velha
    City Number: #349
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vila velha,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maniitsoq
    City Number: #350
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maniitsoq,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: olovyannaya
    City Number: #351
    City URL: http://api.openweathermap.org/data/2.5/weather?q=olovyannaya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: luganville
    City Number: #352
    City URL: http://api.openweathermap.org/data/2.5/weather?q=luganville,vu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bengkulu
    City Number: #353
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bengkulu,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: hammerfest
    City Number: #354
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hammerfest,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tessalit
    City Number: #355
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tessalit,ml&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: takapau
    City Number: #356
    City URL: http://api.openweathermap.org/data/2.5/weather?q=takapau,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: necochea
    City Number: #357
    City URL: http://api.openweathermap.org/data/2.5/weather?q=necochea,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: turayf
    City Number: #358
    City URL: http://api.openweathermap.org/data/2.5/weather?q=turayf,sa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rjukan
    City Number: #359
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rjukan,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sarangani
    City Number: #360
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sarangani,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: beatrice
    City Number: #361
    City URL: http://api.openweathermap.org/data/2.5/weather?q=beatrice,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: khonuu
    City Number: #362
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khonuu,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: solnechnyy
    City Number: #363
    City URL: http://api.openweathermap.org/data/2.5/weather?q=solnechnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: borogontsy
    City Number: #364
    City URL: http://api.openweathermap.org/data/2.5/weather?q=borogontsy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vila
    City Number: #365
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vila,vu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: brooks
    City Number: #366
    City URL: http://api.openweathermap.org/data/2.5/weather?q=brooks,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: brainerd
    City Number: #367
    City URL: http://api.openweathermap.org/data/2.5/weather?q=brainerd,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mabaruma
    City Number: #368
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mabaruma,gy&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pincher creek
    City Number: #369
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pincher creek,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: blackwater
    City Number: #370
    City URL: http://api.openweathermap.org/data/2.5/weather?q=blackwater,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: price
    City Number: #371
    City URL: http://api.openweathermap.org/data/2.5/weather?q=price,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bubaque
    City Number: #372
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bubaque,gw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: samana
    City Number: #373
    City URL: http://api.openweathermap.org/data/2.5/weather?q=samana,do&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: khor
    City Number: #374
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khor,qa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: ulaangom
    City Number: #375
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ulaangom,mn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: awbari
    City Number: #376
    City URL: http://api.openweathermap.org/data/2.5/weather?q=awbari,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: suchitoto
    City Number: #377
    City URL: http://api.openweathermap.org/data/2.5/weather?q=suchitoto,sv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sitrah
    City Number: #378
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sitrah,bh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: langley park
    City Number: #379
    City URL: http://api.openweathermap.org/data/2.5/weather?q=langley park,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yerbogachen
    City Number: #380
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yerbogachen,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marsh harbour
    City Number: #381
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marsh harbour,bs&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: touros
    City Number: #382
    City URL: http://api.openweathermap.org/data/2.5/weather?q=touros,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mandalay
    City Number: #383
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mandalay,mm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: eyl
    City Number: #384
    City URL: http://api.openweathermap.org/data/2.5/weather?q=eyl,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vesele
    City Number: #385
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vesele,ua&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: umba
    City Number: #386
    City URL: http://api.openweathermap.org/data/2.5/weather?q=umba,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: two rivers
    City Number: #387
    City URL: http://api.openweathermap.org/data/2.5/weather?q=two rivers,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chunskiy
    City Number: #388
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chunskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yian
    City Number: #389
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yian,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: juneau
    City Number: #390
    City URL: http://api.openweathermap.org/data/2.5/weather?q=juneau,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hirado
    City Number: #391
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hirado,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: karpathos
    City Number: #392
    City URL: http://api.openweathermap.org/data/2.5/weather?q=karpathos,gr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: perleberg
    City Number: #393
    City URL: http://api.openweathermap.org/data/2.5/weather?q=perleberg,de&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: prince rupert
    City Number: #394
    City URL: http://api.openweathermap.org/data/2.5/weather?q=prince rupert,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: half moon bay
    City Number: #395
    City URL: http://api.openweathermap.org/data/2.5/weather?q=half moon bay,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ozgon
    City Number: #396
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ozgon,kg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: egvekinot
    City Number: #397
    City URL: http://api.openweathermap.org/data/2.5/weather?q=egvekinot,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coihaique
    City Number: #398
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coihaique,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maraa
    City Number: #399
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maraa,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mulchen
    City Number: #400
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mulchen,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bairiki
    City Number: #401
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bairiki,ki&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sirjan
    City Number: #402
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sirjan,ir&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ijaki
    City Number: #403
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ijaki,ki&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: teeli
    City Number: #404
    City URL: http://api.openweathermap.org/data/2.5/weather?q=teeli,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto del rosario
    City Number: #405
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto del rosario,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nueva gerona
    City Number: #406
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nueva gerona,cu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: turkistan
    City Number: #407
    City URL: http://api.openweathermap.org/data/2.5/weather?q=turkistan,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: yarmouth
    City Number: #408
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yarmouth,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tobolsk
    City Number: #409
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tobolsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vaitape
    City Number: #410
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vaitape,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rosendal
    City Number: #411
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rosendal,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: praia
    City Number: #412
    City URL: http://api.openweathermap.org/data/2.5/weather?q=praia,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nhulunbuy
    City Number: #413
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nhulunbuy,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: caravelas
    City Number: #414
    City URL: http://api.openweathermap.org/data/2.5/weather?q=caravelas,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pueblo
    City Number: #415
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pueblo,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jiangyou
    City Number: #416
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jiangyou,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mackay
    City Number: #417
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mackay,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sciacca
    City Number: #418
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sciacca,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bonthe
    City Number: #419
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bonthe,sl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rocha
    City Number: #420
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rocha,uy&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tall kayf
    City Number: #421
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tall kayf,iq&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: pimenta bueno
    City Number: #422
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pimenta bueno,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gemena
    City Number: #423
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gemena,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: matara
    City Number: #424
    City URL: http://api.openweathermap.org/data/2.5/weather?q=matara,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porirua
    City Number: #425
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porirua,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: guerrero negro
    City Number: #426
    City URL: http://api.openweathermap.org/data/2.5/weather?q=guerrero negro,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sasaram
    City Number: #427
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sasaram,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: namibe
    City Number: #428
    City URL: http://api.openweathermap.org/data/2.5/weather?q=namibe,ao&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marathon
    City Number: #429
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marathon,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jibuti
    City Number: #430
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jibuti,dj&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: leh
    City Number: #431
    City URL: http://api.openweathermap.org/data/2.5/weather?q=leh,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: atka
    City Number: #432
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tawkar
    City Number: #433
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tawkar,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: meulaboh
    City Number: #434
    City URL: http://api.openweathermap.org/data/2.5/weather?q=meulaboh,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: buariki
    City Number: #435
    City URL: http://api.openweathermap.org/data/2.5/weather?q=buariki,ki&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: manuk mangkaw
    City Number: #436
    City URL: http://api.openweathermap.org/data/2.5/weather?q=manuk mangkaw,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nanortalik
    City Number: #437
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nanortalik,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: banepa
    City Number: #438
    City URL: http://api.openweathermap.org/data/2.5/weather?q=banepa,np&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: corpus christi
    City Number: #439
    City URL: http://api.openweathermap.org/data/2.5/weather?q=corpus christi,py&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lolua
    City Number: #440
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lolua,tv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: imeni poliny osipenko
    City Number: #441
    City URL: http://api.openweathermap.org/data/2.5/weather?q=imeni poliny osipenko,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cabedelo
    City Number: #442
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cabedelo,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ca mau
    City Number: #443
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ca mau,vn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alexandria
    City Number: #444
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alexandria,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hualmay
    City Number: #445
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hualmay,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ileza
    City Number: #446
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ileza,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nikolskoye
    City Number: #447
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nikolskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: morros
    City Number: #448
    City URL: http://api.openweathermap.org/data/2.5/weather?q=morros,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: baherden
    City Number: #449
    City URL: http://api.openweathermap.org/data/2.5/weather?q=baherden,tm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: roald
    City Number: #450
    City URL: http://api.openweathermap.org/data/2.5/weather?q=roald,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san quintin
    City Number: #451
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san quintin,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: lashio
    City Number: #452
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lashio,mm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kysyl-syr
    City Number: #453
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kysyl-syr,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: masuguru
    City Number: #454
    City URL: http://api.openweathermap.org/data/2.5/weather?q=masuguru,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san joaquin
    City Number: #455
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san joaquin,bo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pindiga
    City Number: #456
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pindiga,ng&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: biala podlaska
    City Number: #457
    City URL: http://api.openweathermap.org/data/2.5/weather?q=biala podlaska,pl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: singaparna
    City Number: #458
    City URL: http://api.openweathermap.org/data/2.5/weather?q=singaparna,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cervo
    City Number: #459
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cervo,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kattivakkam
    City Number: #460
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kattivakkam,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tocopilla
    City Number: #461
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tocopilla,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pella
    City Number: #462
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pella,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tumannyy
    City Number: #463
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tumannyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: andevoranto
    City Number: #464
    City URL: http://api.openweathermap.org/data/2.5/weather?q=andevoranto,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sitka
    City Number: #465
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sitka,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa maria
    City Number: #466
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa maria,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: keta
    City Number: #467
    City URL: http://api.openweathermap.org/data/2.5/weather?q=keta,gh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: buta
    City Number: #468
    City URL: http://api.openweathermap.org/data/2.5/weather?q=buta,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nuevo progreso
    City Number: #469
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nuevo progreso,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mogadishu
    City Number: #470
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mogadishu,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kindu
    City Number: #471
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kindu,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: naryan-mar
    City Number: #472
    City URL: http://api.openweathermap.org/data/2.5/weather?q=naryan-mar,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bourail
    City Number: #473
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bourail,nc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zonguldak
    City Number: #474
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zonguldak,tr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shevchenkove
    City Number: #475
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shevchenkove,ua&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kurchum
    City Number: #476
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kurchum,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: buala
    City Number: #477
    City URL: http://api.openweathermap.org/data/2.5/weather?q=buala,sb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mezen
    City Number: #478
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mezen,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: naron
    City Number: #479
    City URL: http://api.openweathermap.org/data/2.5/weather?q=naron,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: crestview
    City Number: #480
    City URL: http://api.openweathermap.org/data/2.5/weather?q=crestview,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ambon
    City Number: #481
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ambon,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: havoysund
    City Number: #482
    City URL: http://api.openweathermap.org/data/2.5/weather?q=havoysund,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: labuhan
    City Number: #483
    City URL: http://api.openweathermap.org/data/2.5/weather?q=labuhan,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: viedma
    City Number: #484
    City URL: http://api.openweathermap.org/data/2.5/weather?q=viedma,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port-gentil
    City Number: #485
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port-gentil,ga&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: opuwo
    City Number: #486
    City URL: http://api.openweathermap.org/data/2.5/weather?q=opuwo,na&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cotonou
    City Number: #487
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cotonou,bj&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: matamoros
    City Number: #488
    City URL: http://api.openweathermap.org/data/2.5/weather?q=matamoros,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: deer lake
    City Number: #489
    City URL: http://api.openweathermap.org/data/2.5/weather?q=deer lake,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kumluca
    City Number: #490
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kumluca,tr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porbandar
    City Number: #491
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porbandar,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: amazar
    City Number: #492
    City URL: http://api.openweathermap.org/data/2.5/weather?q=amazar,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san pedro buenavista
    City Number: #493
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san pedro buenavista,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rawson
    City Number: #494
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rawson,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: north platte
    City Number: #495
    City URL: http://api.openweathermap.org/data/2.5/weather?q=north platte,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: del rio
    City Number: #496
    City URL: http://api.openweathermap.org/data/2.5/weather?q=del rio,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gagnoa
    City Number: #497
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gagnoa,ci&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yar-sale
    City Number: #498
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yar-sale,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la ronge
    City Number: #499
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la ronge,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: warqla
    City Number: #500
    City URL: http://api.openweathermap.org/data/2.5/weather?q=warqla,dz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: rassvet
    City Number: #501
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rassvet,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: iquique
    City Number: #502
    City URL: http://api.openweathermap.org/data/2.5/weather?q=iquique,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: malm
    City Number: #503
    City URL: http://api.openweathermap.org/data/2.5/weather?q=malm,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-francois
    City Number: #504
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-francois,gp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: avanigadda
    City Number: #505
    City URL: http://api.openweathermap.org/data/2.5/weather?q=avanigadda,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sri aman
    City Number: #506
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sri aman,my&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: boyle
    City Number: #507
    City URL: http://api.openweathermap.org/data/2.5/weather?q=boyle,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sechura
    City Number: #508
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sechura,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: azangaro
    City Number: #509
    City URL: http://api.openweathermap.org/data/2.5/weather?q=azangaro,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: suzu
    City Number: #510
    City URL: http://api.openweathermap.org/data/2.5/weather?q=suzu,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: aleksandrov gay
    City Number: #511
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aleksandrov gay,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san juan
    City Number: #512
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san juan,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: whitehorse
    City Number: #513
    City URL: http://api.openweathermap.org/data/2.5/weather?q=whitehorse,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: boundiali
    City Number: #514
    City URL: http://api.openweathermap.org/data/2.5/weather?q=boundiali,ci&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: laje
    City Number: #515
    City URL: http://api.openweathermap.org/data/2.5/weather?q=laje,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: grand baie
    City Number: #516
    City URL: http://api.openweathermap.org/data/2.5/weather?q=grand baie,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jagdalpur
    City Number: #517
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jagdalpur,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: te anau
    City Number: #518
    City URL: http://api.openweathermap.org/data/2.5/weather?q=te anau,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gannan
    City Number: #519
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gannan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lata
    City Number: #520
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lata,sb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sassenberg
    City Number: #521
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sassenberg,de&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: muscat
    City Number: #522
    City URL: http://api.openweathermap.org/data/2.5/weather?q=muscat,om&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: son la
    City Number: #523
    City URL: http://api.openweathermap.org/data/2.5/weather?q=son la,vn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sinnamary
    City Number: #524
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sinnamary,gf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sulangan
    City Number: #525
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sulangan,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: scottsbluff
    City Number: #526
    City URL: http://api.openweathermap.org/data/2.5/weather?q=scottsbluff,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: channel-port aux basques
    City Number: #527
    City URL: http://api.openweathermap.org/data/2.5/weather?q=channel-port aux basques,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: veraval
    City Number: #528
    City URL: http://api.openweathermap.org/data/2.5/weather?q=veraval,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pevek
    City Number: #529
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pevek,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nyurba
    City Number: #530
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nyurba,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zhuhai
    City Number: #531
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zhuhai,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sindand
    City Number: #532
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sindand,af&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: chivilcoy
    City Number: #533
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chivilcoy,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: baruun-urt
    City Number: #534
    City URL: http://api.openweathermap.org/data/2.5/weather?q=baruun-urt,mn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: atbasar
    City Number: #535
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atbasar,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lakhdenpokhya
    City Number: #536
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lakhdenpokhya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kaoma
    City Number: #537
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kaoma,zm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bambous virieux
    City Number: #538
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bambous virieux,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jonuta
    City Number: #539
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jonuta,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-nera
    City Number: #540
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-nera,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sunrise manor
    City Number: #541
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sunrise manor,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: constitucion
    City Number: #542
    City URL: http://api.openweathermap.org/data/2.5/weather?q=constitucion,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rapid valley
    City Number: #543
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rapid valley,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wahiawa
    City Number: #544
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wahiawa,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tondano
    City Number: #545
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tondano,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: phonhong
    City Number: #546
    City URL: http://api.openweathermap.org/data/2.5/weather?q=phonhong,la&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san luis
    City Number: #547
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san luis,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahon
    City Number: #548
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahon,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: formosa do rio preto
    City Number: #549
    City URL: http://api.openweathermap.org/data/2.5/weather?q=formosa do rio preto,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bima
    City Number: #550
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bima,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dodge city
    City Number: #551
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dodge city,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: senno
    City Number: #552
    City URL: http://api.openweathermap.org/data/2.5/weather?q=senno,by&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: jabiru
    City Number: #553
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jabiru,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: ashqelon
    City Number: #554
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ashqelon,il&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tank
    City Number: #555
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tank,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nsanje
    City Number: #556
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nsanje,mw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: geraldton
    City Number: #557
    City URL: http://api.openweathermap.org/data/2.5/weather?q=geraldton,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nisia floresta
    City Number: #558
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nisia floresta,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nara
    City Number: #559
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nara,ml&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: quelimane
    City Number: #560
    City URL: http://api.openweathermap.org/data/2.5/weather?q=quelimane,mz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ulety
    City Number: #561
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ulety,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: acapulco
    City Number: #562
    City URL: http://api.openweathermap.org/data/2.5/weather?q=acapulco,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hun
    City Number: #563
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hun,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: caborca
    City Number: #564
    City URL: http://api.openweathermap.org/data/2.5/weather?q=caborca,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dolores
    City Number: #565
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dolores,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa rosalia
    City Number: #566
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa rosalia,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vagay
    City Number: #567
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vagay,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mountain home
    City Number: #568
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mountain home,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: iskateley
    City Number: #569
    City URL: http://api.openweathermap.org/data/2.5/weather?q=iskateley,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kampot
    City Number: #570
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kampot,kh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: keti bandar
    City Number: #571
    City URL: http://api.openweathermap.org/data/2.5/weather?q=keti bandar,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: baghdad
    City Number: #572
    City URL: http://api.openweathermap.org/data/2.5/weather?q=baghdad,iq&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: newport
    City Number: #573
    City URL: http://api.openweathermap.org/data/2.5/weather?q=newport,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vestmannaeyjar
    City Number: #574
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vestmannaeyjar,is&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: celestun
    City Number: #575
    City URL: http://api.openweathermap.org/data/2.5/weather?q=celestun,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: westport
    City Number: #576
    City URL: http://api.openweathermap.org/data/2.5/weather?q=westport,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vao
    City Number: #577
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vao,nc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gamba
    City Number: #578
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gamba,ga&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: micheweni
    City Number: #579
    City URL: http://api.openweathermap.org/data/2.5/weather?q=micheweni,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sao marcos
    City Number: #580
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sao marcos,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: katherine
    City Number: #581
    City URL: http://api.openweathermap.org/data/2.5/weather?q=katherine,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: burica
    City Number: #582
    City URL: http://api.openweathermap.org/data/2.5/weather?q=burica,pa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: port hedland
    City Number: #583
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port hedland,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-kuyga
    City Number: #584
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-kuyga,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: leverkusen
    City Number: #585
    City URL: http://api.openweathermap.org/data/2.5/weather?q=leverkusen,de&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coos bay
    City Number: #586
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coos bay,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ishigaki
    City Number: #587
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ishigaki,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la florida
    City Number: #588
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la florida,hn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shchelyayur
    City Number: #589
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shchelyayur,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: fortuna
    City Number: #590
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fortuna,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: araouane
    City Number: #591
    City URL: http://api.openweathermap.org/data/2.5/weather?q=araouane,ml&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mitu
    City Number: #592
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mitu,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: grand centre
    City Number: #593
    City URL: http://api.openweathermap.org/data/2.5/weather?q=grand centre,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: port blair
    City Number: #594
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port blair,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: aleksandrovsk-sakhalinskiy
    City Number: #595
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aleksandrovsk-sakhalinskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porto torres
    City Number: #596
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porto torres,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bundaberg
    City Number: #597
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bundaberg,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: christchurch
    City Number: #598
    City URL: http://api.openweathermap.org/data/2.5/weather?q=christchurch,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: millinocket
    City Number: #599
    City URL: http://api.openweathermap.org/data/2.5/weather?q=millinocket,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: patan
    City Number: #600
    City URL: http://api.openweathermap.org/data/2.5/weather?q=patan,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: haimen
    City Number: #601
    City URL: http://api.openweathermap.org/data/2.5/weather?q=haimen,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: inta
    City Number: #602
    City URL: http://api.openweathermap.org/data/2.5/weather?q=inta,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vaitupu
    City Number: #603
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vaitupu,wf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: trairi
    City Number: #604
    City URL: http://api.openweathermap.org/data/2.5/weather?q=trairi,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zile
    City Number: #605
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zile,tr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tenenkou
    City Number: #606
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tenenkou,ml&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sol-iletsk
    City Number: #607
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sol-iletsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nalut
    City Number: #608
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nalut,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: takoradi
    City Number: #609
    City URL: http://api.openweathermap.org/data/2.5/weather?q=takoradi,gh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alihe
    City Number: #610
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alihe,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: okmulgee
    City Number: #611
    City URL: http://api.openweathermap.org/data/2.5/weather?q=okmulgee,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto rico
    City Number: #612
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto rico,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sooke
    City Number: #613
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sooke,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: deep river
    City Number: #614
    City URL: http://api.openweathermap.org/data/2.5/weather?q=deep river,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: erenhot
    City Number: #615
    City URL: http://api.openweathermap.org/data/2.5/weather?q=erenhot,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mildura
    City Number: #616
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mildura,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: boffa
    City Number: #617
    City URL: http://api.openweathermap.org/data/2.5/weather?q=boffa,gn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kamaishi
    City Number: #618
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kamaishi,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coruripe
    City Number: #619
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coruripe,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bardiyah
    City Number: #620
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bardiyah,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tutoia
    City Number: #621
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tutoia,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maiduguri
    City Number: #622
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maiduguri,ng&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: varhaug
    City Number: #623
    City URL: http://api.openweathermap.org/data/2.5/weather?q=varhaug,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hagere hiywet
    City Number: #624
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hagere hiywet,et&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san ramon
    City Number: #625
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san ramon,bo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lira
    City Number: #626
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lira,ug&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kazanka
    City Number: #627
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kazanka,ua&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: murliganj
    City Number: #628
    City URL: http://api.openweathermap.org/data/2.5/weather?q=murliganj,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coahuayana
    City Number: #629
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coahuayana,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: praia da vitoria
    City Number: #630
    City URL: http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san andres
    City Number: #631
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san andres,gt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: udachnyy
    City Number: #632
    City URL: http://api.openweathermap.org/data/2.5/weather?q=udachnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: messina
    City Number: #633
    City URL: http://api.openweathermap.org/data/2.5/weather?q=messina,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tucuman
    City Number: #634
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tucuman,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: charters towers
    City Number: #635
    City URL: http://api.openweathermap.org/data/2.5/weather?q=charters towers,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: amurzet
    City Number: #636
    City URL: http://api.openweathermap.org/data/2.5/weather?q=amurzet,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: moree
    City Number: #637
    City URL: http://api.openweathermap.org/data/2.5/weather?q=moree,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sorong
    City Number: #638
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sorong,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: catuday
    City Number: #639
    City URL: http://api.openweathermap.org/data/2.5/weather?q=catuday,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: netrakona
    City Number: #640
    City URL: http://api.openweathermap.org/data/2.5/weather?q=netrakona,bd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: las choapas
    City Number: #641
    City URL: http://api.openweathermap.org/data/2.5/weather?q=las choapas,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ntcheu
    City Number: #642
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ntcheu,mw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ritto
    City Number: #643
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ritto,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nova olimpia
    City Number: #644
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nova olimpia,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: porto belo
    City Number: #645
    City URL: http://api.openweathermap.org/data/2.5/weather?q=porto belo,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nagato
    City Number: #646
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nagato,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cockburn town
    City Number: #647
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cockburn town,bs&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: castlemaine
    City Number: #648
    City URL: http://api.openweathermap.org/data/2.5/weather?q=castlemaine,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ahlat
    City Number: #649
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ahlat,tr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dawei
    City Number: #650
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dawei,mm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: choucheng
    City Number: #651
    City URL: http://api.openweathermap.org/data/2.5/weather?q=choucheng,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: turukhansk
    City Number: #652
    City URL: http://api.openweathermap.org/data/2.5/weather?q=turukhansk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ormara
    City Number: #653
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ormara,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: terrasini
    City Number: #654
    City URL: http://api.openweathermap.org/data/2.5/weather?q=terrasini,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: drayton valley
    City Number: #655
    City URL: http://api.openweathermap.org/data/2.5/weather?q=drayton valley,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lazaro cardenas
    City Number: #656
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lazaro cardenas,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: elk point
    City Number: #657
    City URL: http://api.openweathermap.org/data/2.5/weather?q=elk point,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: temaraia
    City Number: #658
    City URL: http://api.openweathermap.org/data/2.5/weather?q=temaraia,ki&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: rabaul
    City Number: #659
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rabaul,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bhaderwah
    City Number: #660
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bhaderwah,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: college
    City Number: #661
    City URL: http://api.openweathermap.org/data/2.5/weather?q=college,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: havre-saint-pierre
    City Number: #662
    City URL: http://api.openweathermap.org/data/2.5/weather?q=havre-saint-pierre,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: laem sing
    City Number: #663
    City URL: http://api.openweathermap.org/data/2.5/weather?q=laem sing,th&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vernon
    City Number: #664
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vernon,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jalu
    City Number: #665
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jalu,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mehamn
    City Number: #666
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mehamn,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mullaitivu
    City Number: #667
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mullaitivu,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: mitha tiwana
    City Number: #668
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mitha tiwana,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: galgani
    City Number: #669
    City URL: http://api.openweathermap.org/data/2.5/weather?q=galgani,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: adelaide
    City Number: #670
    City URL: http://api.openweathermap.org/data/2.5/weather?q=adelaide,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marzuq
    City Number: #671
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marzuq,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: coari
    City Number: #672
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coari,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tabou
    City Number: #673
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tabou,ci&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: soyo
    City Number: #674
    City URL: http://api.openweathermap.org/data/2.5/weather?q=soyo,ao&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: grand gaube
    City Number: #675
    City URL: http://api.openweathermap.org/data/2.5/weather?q=grand gaube,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: havre
    City Number: #676
    City URL: http://api.openweathermap.org/data/2.5/weather?q=havre,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tabuk
    City Number: #677
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tabuk,sa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: taksimo
    City Number: #678
    City URL: http://api.openweathermap.org/data/2.5/weather?q=taksimo,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lavrentiya
    City Number: #679
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lavrentiya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: colborne
    City Number: #680
    City URL: http://api.openweathermap.org/data/2.5/weather?q=colborne,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tanout
    City Number: #681
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tanout,ne&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: atar
    City Number: #682
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atar,mr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tadine
    City Number: #683
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tadine,nc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: blagoveshchensk
    City Number: #684
    City URL: http://api.openweathermap.org/data/2.5/weather?q=blagoveshchensk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: severo-yeniseyskiy
    City Number: #685
    City URL: http://api.openweathermap.org/data/2.5/weather?q=severo-yeniseyskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: erzin
    City Number: #686
    City URL: http://api.openweathermap.org/data/2.5/weather?q=erzin,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sharjah
    City Number: #687
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sharjah,ae&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la romana
    City Number: #688
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la romana,do&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: guantanamo
    City Number: #689
    City URL: http://api.openweathermap.org/data/2.5/weather?q=guantanamo,cu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: oum hadjer
    City Number: #690
    City URL: http://api.openweathermap.org/data/2.5/weather?q=oum hadjer,td&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sakakah
    City Number: #691
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sakakah,sa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: dolbeau
    City Number: #692
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dolbeau,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: changji
    City Number: #693
    City URL: http://api.openweathermap.org/data/2.5/weather?q=changji,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: deputatskiy
    City Number: #694
    City URL: http://api.openweathermap.org/data/2.5/weather?q=deputatskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: belmonte
    City Number: #695
    City URL: http://api.openweathermap.org/data/2.5/weather?q=belmonte,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: carutapera
    City Number: #696
    City URL: http://api.openweathermap.org/data/2.5/weather?q=carutapera,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nueva imperial
    City Number: #697
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nueva imperial,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: edd
    City Number: #698
    City URL: http://api.openweathermap.org/data/2.5/weather?q=edd,er&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: neuquen
    City Number: #699
    City URL: http://api.openweathermap.org/data/2.5/weather?q=neuquen,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: batemans bay
    City Number: #700
    City URL: http://api.openweathermap.org/data/2.5/weather?q=batemans bay,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: haripur
    City Number: #701
    City URL: http://api.openweathermap.org/data/2.5/weather?q=haripur,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint-georges
    City Number: #702
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint-georges,gf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: toktogul
    City Number: #703
    City URL: http://api.openweathermap.org/data/2.5/weather?q=toktogul,kg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vardo
    City Number: #704
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vardo,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la reforma
    City Number: #705
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la reforma,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ishim
    City Number: #706
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ishim,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shakawe
    City Number: #707
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shakawe,bw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wembley
    City Number: #708
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wembley,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: moussoro
    City Number: #709
    City URL: http://api.openweathermap.org/data/2.5/weather?q=moussoro,td&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gotsu
    City Number: #710
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gotsu,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: troitskoye
    City Number: #711
    City URL: http://api.openweathermap.org/data/2.5/weather?q=troitskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: balabac
    City Number: #712
    City URL: http://api.openweathermap.org/data/2.5/weather?q=balabac,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: acayucan
    City Number: #713
    City URL: http://api.openweathermap.org/data/2.5/weather?q=acayucan,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: khirkiya
    City Number: #714
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khirkiya,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hefei
    City Number: #715
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hefei,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: macau
    City Number: #716
    City URL: http://api.openweathermap.org/data/2.5/weather?q=macau,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gurskoye
    City Number: #717
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gurskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: talcahuano
    City Number: #718
    City URL: http://api.openweathermap.org/data/2.5/weather?q=talcahuano,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tuy hoa
    City Number: #719
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tuy hoa,vn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: northam
    City Number: #720
    City URL: http://api.openweathermap.org/data/2.5/weather?q=northam,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: one hundred mile house
    City Number: #721
    City URL: http://api.openweathermap.org/data/2.5/weather?q=one hundred mile house,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: aguai
    City Number: #722
    City URL: http://api.openweathermap.org/data/2.5/weather?q=aguai,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: halalo
    City Number: #723
    City URL: http://api.openweathermap.org/data/2.5/weather?q=halalo,wf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: kushima
    City Number: #724
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kushima,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto asis
    City Number: #725
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto asis,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pyapon
    City Number: #726
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pyapon,mm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hambantota
    City Number: #727
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hambantota,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kachikau
    City Number: #728
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kachikau,bw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: west wendover
    City Number: #729
    City URL: http://api.openweathermap.org/data/2.5/weather?q=west wendover,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: boatlaname
    City Number: #730
    City URL: http://api.openweathermap.org/data/2.5/weather?q=boatlaname,bw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: sumbe
    City Number: #731
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sumbe,ao&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wilmington
    City Number: #732
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wilmington,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sarai naurang
    City Number: #733
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sarai naurang,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: guanare
    City Number: #734
    City URL: http://api.openweathermap.org/data/2.5/weather?q=guanare,ve&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dharchula
    City Number: #735
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dharchula,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ponta delgada
    City Number: #736
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ponta delgada,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: biaora
    City Number: #737
    City URL: http://api.openweathermap.org/data/2.5/weather?q=biaora,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: comodoro rivadavia
    City Number: #738
    City URL: http://api.openweathermap.org/data/2.5/weather?q=comodoro rivadavia,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: meyungs
    City Number: #739
    City URL: http://api.openweathermap.org/data/2.5/weather?q=meyungs,pw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: gorno-chuyskiy
    City Number: #740
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gorno-chuyskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: nuuk
    City Number: #741
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nuuk,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sambava
    City Number: #742
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sambava,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: avera
    City Number: #743
    City URL: http://api.openweathermap.org/data/2.5/weather?q=avera,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: lixourion
    City Number: #744
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lixourion,gr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: khuzhir
    City Number: #745
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khuzhir,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sikeston
    City Number: #746
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sikeston,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: moron
    City Number: #747
    City URL: http://api.openweathermap.org/data/2.5/weather?q=moron,mn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: olinda
    City Number: #748
    City URL: http://api.openweathermap.org/data/2.5/weather?q=olinda,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: varias
    City Number: #749
    City URL: http://api.openweathermap.org/data/2.5/weather?q=varias,ro&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rockhampton
    City Number: #750
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rockhampton,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: galle
    City Number: #751
    City URL: http://api.openweathermap.org/data/2.5/weather?q=galle,lk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lima
    City Number: #752
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lima,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mokhotlong
    City Number: #753
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mokhotlong,ls&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nouadhibou
    City Number: #754
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nouadhibou,mr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pauini
    City Number: #755
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pauini,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: berlevag
    City Number: #756
    City URL: http://api.openweathermap.org/data/2.5/weather?q=berlevag,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kwinana
    City Number: #757
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kwinana,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: valle de allende
    City Number: #758
    City URL: http://api.openweathermap.org/data/2.5/weather?q=valle de allende,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mercedes
    City Number: #759
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mercedes,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: manokwari
    City Number: #760
    City URL: http://api.openweathermap.org/data/2.5/weather?q=manokwari,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wewak
    City Number: #761
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wewak,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mudyuga
    City Number: #762
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mudyuga,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: trencin
    City Number: #763
    City URL: http://api.openweathermap.org/data/2.5/weather?q=trencin,sk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tamandare
    City Number: #764
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tamandare,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: guangyuan
    City Number: #765
    City URL: http://api.openweathermap.org/data/2.5/weather?q=guangyuan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la mana
    City Number: #766
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la mana,ec&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: rovaniemi
    City Number: #767
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rovaniemi,fi&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: agua branca
    City Number: #768
    City URL: http://api.openweathermap.org/data/2.5/weather?q=agua branca,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alice
    City Number: #769
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alice,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zhigansk
    City Number: #770
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zhigansk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: greenwood
    City Number: #771
    City URL: http://api.openweathermap.org/data/2.5/weather?q=greenwood,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: poplar bluff
    City Number: #772
    City URL: http://api.openweathermap.org/data/2.5/weather?q=poplar bluff,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: panzhihua
    City Number: #773
    City URL: http://api.openweathermap.org/data/2.5/weather?q=panzhihua,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: petropavlovsk-kamchatskiy
    City Number: #774
    City URL: http://api.openweathermap.org/data/2.5/weather?q=petropavlovsk-kamchatskiy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nelson bay
    City Number: #775
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nelson bay,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kazalinsk
    City Number: #776
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kazalinsk,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: senanga
    City Number: #777
    City URL: http://api.openweathermap.org/data/2.5/weather?q=senanga,zm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: poronaysk
    City Number: #778
    City URL: http://api.openweathermap.org/data/2.5/weather?q=poronaysk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pierre
    City Number: #779
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pierre,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto escondido
    City Number: #780
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto escondido,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-kamchatsk
    City Number: #781
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-kamchatsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tautira
    City Number: #782
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tautira,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: quatre cocos
    City Number: #783
    City URL: http://api.openweathermap.org/data/2.5/weather?q=quatre cocos,mu&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sayyan
    City Number: #784
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sayyan,ye&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dunda
    City Number: #785
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dunda,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la asuncion
    City Number: #786
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la asuncion,ve&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: marsa matruh
    City Number: #787
    City URL: http://api.openweathermap.org/data/2.5/weather?q=marsa matruh,eg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kharovsk
    City Number: #788
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kharovsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: turgoyak
    City Number: #789
    City URL: http://api.openweathermap.org/data/2.5/weather?q=turgoyak,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sinjar
    City Number: #790
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sinjar,iq&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dekoa
    City Number: #791
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dekoa,cf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: praya
    City Number: #792
    City URL: http://api.openweathermap.org/data/2.5/weather?q=praya,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: qui nhon
    City Number: #793
    City URL: http://api.openweathermap.org/data/2.5/weather?q=qui nhon,vn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: roros
    City Number: #794
    City URL: http://api.openweathermap.org/data/2.5/weather?q=roros,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bentiu
    City Number: #795
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bentiu,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: cubara
    City Number: #796
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cubara,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sydney
    City Number: #797
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sydney,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: itarema
    City Number: #798
    City URL: http://api.openweathermap.org/data/2.5/weather?q=itarema,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port augusta
    City Number: #799
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port augusta,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ketchenery
    City Number: #800
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ketchenery,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: whitehaven
    City Number: #801
    City URL: http://api.openweathermap.org/data/2.5/weather?q=whitehaven,gb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: terra roxa
    City Number: #802
    City URL: http://api.openweathermap.org/data/2.5/weather?q=terra roxa,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: barcelos
    City Number: #803
    City URL: http://api.openweathermap.org/data/2.5/weather?q=barcelos,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: roseburg
    City Number: #804
    City URL: http://api.openweathermap.org/data/2.5/weather?q=roseburg,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahalapye
    City Number: #805
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahalapye,bw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: achit
    City Number: #806
    City URL: http://api.openweathermap.org/data/2.5/weather?q=achit,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: surat
    City Number: #807
    City URL: http://api.openweathermap.org/data/2.5/weather?q=surat,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: herat
    City Number: #808
    City URL: http://api.openweathermap.org/data/2.5/weather?q=herat,af&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: omsukchan
    City Number: #809
    City URL: http://api.openweathermap.org/data/2.5/weather?q=omsukchan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: maghama
    City Number: #810
    City URL: http://api.openweathermap.org/data/2.5/weather?q=maghama,mr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: atocha
    City Number: #811
    City URL: http://api.openweathermap.org/data/2.5/weather?q=atocha,bo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bereda
    City Number: #812
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bereda,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: bonavista
    City Number: #813
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bonavista,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: natal
    City Number: #814
    City URL: http://api.openweathermap.org/data/2.5/weather?q=natal,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kyaikkami
    City Number: #815
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kyaikkami,mm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bukama
    City Number: #816
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bukama,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: terenos
    City Number: #817
    City URL: http://api.openweathermap.org/data/2.5/weather?q=terenos,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: flagstaff
    City Number: #818
    City URL: http://api.openweathermap.org/data/2.5/weather?q=flagstaff,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la rioja
    City Number: #819
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la rioja,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: corinto
    City Number: #820
    City URL: http://api.openweathermap.org/data/2.5/weather?q=corinto,ni&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sarandi
    City Number: #821
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sarandi,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: liepaja
    City Number: #822
    City URL: http://api.openweathermap.org/data/2.5/weather?q=liepaja,lv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: colares
    City Number: #823
    City URL: http://api.openweathermap.org/data/2.5/weather?q=colares,pt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sibolga
    City Number: #824
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sibolga,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: williamsburg
    City Number: #825
    City URL: http://api.openweathermap.org/data/2.5/weather?q=williamsburg,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: port macquarie
    City Number: #826
    City URL: http://api.openweathermap.org/data/2.5/weather?q=port macquarie,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lamidan
    City Number: #827
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lamidan,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: laramie
    City Number: #828
    City URL: http://api.openweathermap.org/data/2.5/weather?q=laramie,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: manono
    City Number: #829
    City URL: http://api.openweathermap.org/data/2.5/weather?q=manono,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cozumel
    City Number: #830
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cozumel,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: gillette
    City Number: #831
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gillette,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: viljoenskroon
    City Number: #832
    City URL: http://api.openweathermap.org/data/2.5/weather?q=viljoenskroon,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: haibowan
    City Number: #833
    City URL: http://api.openweathermap.org/data/2.5/weather?q=haibowan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: okhotsk
    City Number: #834
    City URL: http://api.openweathermap.org/data/2.5/weather?q=okhotsk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mirnyy
    City Number: #835
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mirnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: axim
    City Number: #836
    City URL: http://api.openweathermap.org/data/2.5/weather?q=axim,gh&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: washington
    City Number: #837
    City URL: http://api.openweathermap.org/data/2.5/weather?q=washington,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: koslan
    City Number: #838
    City URL: http://api.openweathermap.org/data/2.5/weather?q=koslan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yook
    City Number: #839
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yook,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: townsville
    City Number: #840
    City URL: http://api.openweathermap.org/data/2.5/weather?q=townsville,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: orel
    City Number: #841
    City URL: http://api.openweathermap.org/data/2.5/weather?q=orel,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: suba
    City Number: #842
    City URL: http://api.openweathermap.org/data/2.5/weather?q=suba,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vikindu
    City Number: #843
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vikindu,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hovd
    City Number: #844
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hovd,mn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kamiiso
    City Number: #845
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kamiiso,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: monrovia
    City Number: #846
    City URL: http://api.openweathermap.org/data/2.5/weather?q=monrovia,lr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: beyneu
    City Number: #847
    City URL: http://api.openweathermap.org/data/2.5/weather?q=beyneu,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahibadhoo
    City Number: #848
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahibadhoo,mv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: melfort
    City Number: #849
    City URL: http://api.openweathermap.org/data/2.5/weather?q=melfort,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: coxim
    City Number: #850
    City URL: http://api.openweathermap.org/data/2.5/weather?q=coxim,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dien bien
    City Number: #851
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dien bien,vn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: hunza
    City Number: #852
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hunza,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: san jeronimo
    City Number: #853
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san jeronimo,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sterling
    City Number: #854
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sterling,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kompaniyivka
    City Number: #855
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kompaniyivka,ua&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: verkhnevilyuysk
    City Number: #856
    City URL: http://api.openweathermap.org/data/2.5/weather?q=verkhnevilyuysk,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mount gambier
    City Number: #857
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mount gambier,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: stornoway
    City Number: #858
    City URL: http://api.openweathermap.org/data/2.5/weather?q=stornoway,gb&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vestmanna
    City Number: #859
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vestmanna,fo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: los llanos de aridane
    City Number: #860
    City URL: http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ouesso
    City Number: #861
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ouesso,cg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: palora
    City Number: #862
    City URL: http://api.openweathermap.org/data/2.5/weather?q=palora,ec&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tukan
    City Number: #863
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tukan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: resen
    City Number: #864
    City URL: http://api.openweathermap.org/data/2.5/weather?q=resen,mk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ratnagiri
    City Number: #865
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ratnagiri,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tsentralnyy
    City Number: #866
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tsentralnyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: merrill
    City Number: #867
    City URL: http://api.openweathermap.org/data/2.5/weather?q=merrill,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kone
    City Number: #868
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kone,nc&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shushenskoye
    City Number: #869
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shushenskoye,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sao filipe
    City Number: #870
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sao filipe,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kobelyaky
    City Number: #871
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kobelyaky,ua&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kungurtug
    City Number: #872
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kungurtug,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: egersund
    City Number: #873
    City URL: http://api.openweathermap.org/data/2.5/weather?q=egersund,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: methoni
    City Number: #874
    City URL: http://api.openweathermap.org/data/2.5/weather?q=methoni,gr&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kapoeta
    City Number: #875
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kapoeta,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: rahon
    City Number: #876
    City URL: http://api.openweathermap.org/data/2.5/weather?q=rahon,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zhengjiatun
    City Number: #877
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zhengjiatun,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sadon
    City Number: #878
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sadon,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gimli
    City Number: #879
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gimli,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: brigantine
    City Number: #880
    City URL: http://api.openweathermap.org/data/2.5/weather?q=brigantine,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: chambersburg
    City Number: #881
    City URL: http://api.openweathermap.org/data/2.5/weather?q=chambersburg,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: diffa
    City Number: #882
    City URL: http://api.openweathermap.org/data/2.5/weather?q=diffa,ne&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: voyvozh
    City Number: #883
    City URL: http://api.openweathermap.org/data/2.5/weather?q=voyvozh,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: svetlyy
    City Number: #884
    City URL: http://api.openweathermap.org/data/2.5/weather?q=svetlyy,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: doctor pedro p. pena
    City Number: #885
    City URL: http://api.openweathermap.org/data/2.5/weather?q=doctor pedro p. pena,py&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: taltal
    City Number: #886
    City URL: http://api.openweathermap.org/data/2.5/weather?q=taltal,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: basco
    City Number: #887
    City URL: http://api.openweathermap.org/data/2.5/weather?q=basco,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: katsuura
    City Number: #888
    City URL: http://api.openweathermap.org/data/2.5/weather?q=katsuura,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: fairfield
    City Number: #889
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fairfield,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: piacabucu
    City Number: #890
    City URL: http://api.openweathermap.org/data/2.5/weather?q=piacabucu,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: belyy yar
    City Number: #891
    City URL: http://api.openweathermap.org/data/2.5/weather?q=belyy yar,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: merauke
    City Number: #892
    City URL: http://api.openweathermap.org/data/2.5/weather?q=merauke,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: south valley
    City Number: #893
    City URL: http://api.openweathermap.org/data/2.5/weather?q=south valley,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: libenge
    City Number: #894
    City URL: http://api.openweathermap.org/data/2.5/weather?q=libenge,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jawa
    City Number: #895
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jawa,jo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mikhaylovka
    City Number: #896
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mikhaylovka,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: cheuskiny
    City Number: #897
    City URL: http://api.openweathermap.org/data/2.5/weather?q=cheuskiny,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: paamiut
    City Number: #898
    City URL: http://api.openweathermap.org/data/2.5/weather?q=paamiut,gl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: zhob
    City Number: #899
    City URL: http://api.openweathermap.org/data/2.5/weather?q=zhob,pk&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: upata
    City Number: #900
    City URL: http://api.openweathermap.org/data/2.5/weather?q=upata,ve&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: misasi
    City Number: #901
    City URL: http://api.openweathermap.org/data/2.5/weather?q=misasi,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yanam
    City Number: #902
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yanam,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: baneh
    City Number: #903
    City URL: http://api.openweathermap.org/data/2.5/weather?q=baneh,ir&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mbandaka
    City Number: #904
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mbandaka,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: massakory
    City Number: #905
    City URL: http://api.openweathermap.org/data/2.5/weather?q=massakory,td&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ugoofaaru
    City Number: #906
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ugoofaaru,mv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: la paz
    City Number: #907
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la paz,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: gaogou
    City Number: #908
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gaogou,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: olden
    City Number: #909
    City URL: http://api.openweathermap.org/data/2.5/weather?q=olden,no&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: dunedin
    City Number: #910
    City URL: http://api.openweathermap.org/data/2.5/weather?q=dunedin,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ler
    City Number: #911
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ler,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: gambela
    City Number: #912
    City URL: http://api.openweathermap.org/data/2.5/weather?q=gambela,et&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: palmer
    City Number: #913
    City URL: http://api.openweathermap.org/data/2.5/weather?q=palmer,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: fare
    City Number: #914
    City URL: http://api.openweathermap.org/data/2.5/weather?q=fare,pf&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: benjamin hill
    City Number: #915
    City URL: http://api.openweathermap.org/data/2.5/weather?q=benjamin hill,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ngerengere
    City Number: #916
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ngerengere,tz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: alice springs
    City Number: #917
    City URL: http://api.openweathermap.org/data/2.5/weather?q=alice springs,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: adeje
    City Number: #918
    City URL: http://api.openweathermap.org/data/2.5/weather?q=adeje,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nuqui
    City Number: #919
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nuqui,co&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: umzimvubu
    City Number: #920
    City URL: http://api.openweathermap.org/data/2.5/weather?q=umzimvubu,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: luanda
    City Number: #921
    City URL: http://api.openweathermap.org/data/2.5/weather?q=luanda,ao&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: banda aceh
    City Number: #922
    City URL: http://api.openweathermap.org/data/2.5/weather?q=banda aceh,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ternate
    City Number: #923
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ternate,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: narrabri
    City Number: #924
    City URL: http://api.openweathermap.org/data/2.5/weather?q=narrabri,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: north myrtle beach
    City Number: #925
    City URL: http://api.openweathermap.org/data/2.5/weather?q=north myrtle beach,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shenjiamen
    City Number: #926
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shenjiamen,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jomalig
    City Number: #927
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jomalig,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: bennington
    City Number: #928
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bennington,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: vostok
    City Number: #929
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vostok,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bayan
    City Number: #930
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bayan,kw&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: killybegs
    City Number: #931
    City URL: http://api.openweathermap.org/data/2.5/weather?q=killybegs,ie&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bertinoro
    City Number: #932
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bertinoro,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mindelo
    City Number: #933
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mindelo,cv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mount isa
    City Number: #934
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mount isa,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: castrillon
    City Number: #935
    City URL: http://api.openweathermap.org/data/2.5/weather?q=castrillon,es&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ingraj bazar
    City Number: #936
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ingraj bazar,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tubruq
    City Number: #937
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tubruq,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: yakeshi
    City Number: #938
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yakeshi,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: malakal
    City Number: #939
    City URL: http://api.openweathermap.org/data/2.5/weather?q=malakal,sd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: luderitz
    City Number: #940
    City URL: http://api.openweathermap.org/data/2.5/weather?q=luderitz,na&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sucua
    City Number: #941
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sucua,ec&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: manakara
    City Number: #942
    City URL: http://api.openweathermap.org/data/2.5/weather?q=manakara,mg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nioro
    City Number: #943
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nioro,ml&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: boca do acre
    City Number: #944
    City URL: http://api.openweathermap.org/data/2.5/weather?q=boca do acre,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: jumla
    City Number: #945
    City URL: http://api.openweathermap.org/data/2.5/weather?q=jumla,np&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san jose
    City Number: #946
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san jose,gt&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: wamba
    City Number: #947
    City URL: http://api.openweathermap.org/data/2.5/weather?q=wamba,cd&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: lumby
    City Number: #948
    City URL: http://api.openweathermap.org/data/2.5/weather?q=lumby,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: preobrazhenskaya
    City Number: #949
    City URL: http://api.openweathermap.org/data/2.5/weather?q=preobrazhenskaya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: tres passos
    City Number: #950
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tres passos,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hihifo
    City Number: #951
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hihifo,to&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: khandyga
    City Number: #952
    City URL: http://api.openweathermap.org/data/2.5/weather?q=khandyga,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ascension
    City Number: #953
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ascension,bo&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: hattiesburg
    City Number: #954
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hattiesburg,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ust-maya
    City Number: #955
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ust-maya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: eufaula
    City Number: #956
    City URL: http://api.openweathermap.org/data/2.5/weather?q=eufaula,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mecca
    City Number: #957
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mecca,sa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bargal
    City Number: #958
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bargal,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: la union
    City Number: #959
    City URL: http://api.openweathermap.org/data/2.5/weather?q=la union,cl&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pilar
    City Number: #960
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pilar,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: thibodaux
    City Number: #961
    City URL: http://api.openweathermap.org/data/2.5/weather?q=thibodaux,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kununurra
    City Number: #962
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kununurra,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pangai
    City Number: #963
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pangai,to&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ningan
    City Number: #964
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ningan,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: ixtapa
    City Number: #965
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ixtapa,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: mahadday weyne
    City Number: #966
    City URL: http://api.openweathermap.org/data/2.5/weather?q=mahadday weyne,so&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: kuruman
    City Number: #967
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kuruman,za&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: tupik
    City Number: #968
    City URL: http://api.openweathermap.org/data/2.5/weather?q=tupik,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: arkadelphia
    City Number: #969
    City URL: http://api.openweathermap.org/data/2.5/weather?q=arkadelphia,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: san isidro
    City Number: #970
    City URL: http://api.openweathermap.org/data/2.5/weather?q=san isidro,ph&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: nishihara
    City Number: #971
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nishihara,jp&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ngukurr
    City Number: #972
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ngukurr,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: nueva italia de ruiz
    City Number: #973
    City URL: http://api.openweathermap.org/data/2.5/weather?q=nueva italia de ruiz,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: goianesia
    City Number: #974
    City URL: http://api.openweathermap.org/data/2.5/weather?q=goianesia,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: halifax
    City Number: #975
    City URL: http://api.openweathermap.org/data/2.5/weather?q=halifax,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: karangampel
    City Number: #976
    City URL: http://api.openweathermap.org/data/2.5/weather?q=karangampel,id&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kawardha
    City Number: #977
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kawardha,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: yanchukan
    City Number: #978
    City URL: http://api.openweathermap.org/data/2.5/weather?q=yanchukan,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: vanimo
    City Number: #979
    City URL: http://api.openweathermap.org/data/2.5/weather?q=vanimo,pg&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: saint anthony
    City Number: #980
    City URL: http://api.openweathermap.org/data/2.5/weather?q=saint anthony,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    ERROR WITH CITY DATA, SKIPPING
    Processing - City Name: teya
    City Number: #981
    City URL: http://api.openweathermap.org/data/2.5/weather?q=teya,ru&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: okato
    City Number: #982
    City URL: http://api.openweathermap.org/data/2.5/weather?q=okato,nz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: shetpe
    City Number: #983
    City URL: http://api.openweathermap.org/data/2.5/weather?q=shetpe,kz&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pitimbu
    City Number: #984
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pitimbu,br&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: flin flon
    City Number: #985
    City URL: http://api.openweathermap.org/data/2.5/weather?q=flin flon,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: neuruppin
    City Number: #986
    City URL: http://api.openweathermap.org/data/2.5/weather?q=neuruppin,de&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: waddan
    City Number: #987
    City URL: http://api.openweathermap.org/data/2.5/weather?q=waddan,ly&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: kulhudhuffushi
    City Number: #988
    City URL: http://api.openweathermap.org/data/2.5/weather?q=kulhudhuffushi,mv&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: makakilo city
    City Number: #989
    City URL: http://api.openweathermap.org/data/2.5/weather?q=makakilo city,us&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hungund
    City Number: #990
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hungund,in&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: santa fe
    City Number: #991
    City URL: http://api.openweathermap.org/data/2.5/weather?q=santa fe,ar&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: pedasi
    City Number: #992
    City URL: http://api.openweathermap.org/data/2.5/weather?q=pedasi,pa&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: ahome
    City Number: #993
    City URL: http://api.openweathermap.org/data/2.5/weather?q=ahome,mx&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: bordighera
    City Number: #994
    City URL: http://api.openweathermap.org/data/2.5/weather?q=bordighera,it&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: hay river
    City Number: #995
    City URL: http://api.openweathermap.org/data/2.5/weather?q=hay river,ca&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: puerto maldonado
    City Number: #996
    City URL: http://api.openweathermap.org/data/2.5/weather?q=puerto maldonado,pe&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: sangmelima
    City Number: #997
    City URL: http://api.openweathermap.org/data/2.5/weather?q=sangmelima,cm&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: altay
    City Number: #998
    City URL: http://api.openweathermap.org/data/2.5/weather?q=altay,cn&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    Processing - City Name: victoria point
    City Number: #999
    City URL: http://api.openweathermap.org/data/2.5/weather?q=victoria point,au&units=imperial&appid=c2ebe13b2ca2223ec9fac09b14ce02ee
    


```python
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Cloudiness (%)</th>
      <th>Country Code</th>
      <th>Humidity (%)</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature (F)</th>
      <th>Wind Speed (MPH)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>faya</td>
      <td></td>
      <td>td</td>
      <td></td>
      <td>N/A</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>khatima</td>
      <td>0</td>
      <td>in</td>
      <td>83</td>
      <td>28.92</td>
      <td>79.97</td>
      <td>55.68</td>
      <td>2.71</td>
    </tr>
    <tr>
      <th>2</th>
      <td>seoul</td>
      <td>80</td>
      <td>kr</td>
      <td>89</td>
      <td>37.57</td>
      <td>126.98</td>
      <td>36.15</td>
      <td>2.59</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aasiaat</td>
      <td>36</td>
      <td>gl</td>
      <td>100</td>
      <td>68.71</td>
      <td>-52.87</td>
      <td>8.84</td>
      <td>10.76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>torbay</td>
      <td>88</td>
      <td>ca</td>
      <td>95</td>
      <td>47.66</td>
      <td>-52.73</td>
      <td>31.38</td>
      <td>22.84</td>
    </tr>
  </tbody>
</table>
</div>




```python
city_df = city_df[city_df.Latitude != "N/A"]
city_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City Name</th>
      <th>Cloudiness (%)</th>
      <th>Country Code</th>
      <th>Humidity (%)</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature (F)</th>
      <th>Wind Speed (MPH)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>khatima</td>
      <td>0</td>
      <td>in</td>
      <td>83</td>
      <td>28.92</td>
      <td>79.97</td>
      <td>55.68</td>
      <td>2.71</td>
    </tr>
    <tr>
      <th>2</th>
      <td>seoul</td>
      <td>80</td>
      <td>kr</td>
      <td>89</td>
      <td>37.57</td>
      <td>126.98</td>
      <td>36.15</td>
      <td>2.59</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aasiaat</td>
      <td>36</td>
      <td>gl</td>
      <td>100</td>
      <td>68.71</td>
      <td>-52.87</td>
      <td>8.84</td>
      <td>10.76</td>
    </tr>
    <tr>
      <th>4</th>
      <td>torbay</td>
      <td>88</td>
      <td>ca</td>
      <td>95</td>
      <td>47.66</td>
      <td>-52.73</td>
      <td>31.38</td>
      <td>22.84</td>
    </tr>
    <tr>
      <th>6</th>
      <td>loja</td>
      <td>64</td>
      <td>es</td>
      <td>98</td>
      <td>37.17</td>
      <td>-4.15</td>
      <td>45.65</td>
      <td>4.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
temp_scat = plt.scatter(city_df["Latitude"], city_df["Temperature (F)"], marker="o", color="r", edgecolors="black")

plt.xlim((city_df["Latitude"].min()) - 10, (city_df["Latitude"].max()) + 10)
plt.ylim((city_df["Temperature (F)"].min()) - 5,(city_df["Temperature (F)"].max()) + 5)
plt.grid()

plt.title("City Temperatures vs. Latitude (2/27/18)")
plt.xlabel("Latitude")
plt.ylabel("Temperature (F)")

plt.savefig("temp png")

plt.show()
```


![png](output_8_0.png)



```python
humid_scat = plt.scatter(city_df["Latitude"], city_df["Humidity (%)"], marker="o", color="b", edgecolors="black")

plt.xlim((city_df["Latitude"].min()) - 10, (city_df["Latitude"].max()) + 10)
plt.ylim((city_df["Humidity (%)"].min()) - 5, (city_df["Humidity (%)"].max()) + 10)
plt.grid()

plt.title("City Humidity vs. Latitude (2/27/18)")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")

plt.savefig("humidity png")

plt.show()
```


![png](output_9_0.png)



```python
cloud_scat = plt.scatter(city_df["Latitude"], city_df["Cloudiness (%)"], marker="o", color="g", edgecolors="black")

plt.xlim((city_df["Latitude"].min()) - 10, (city_df["Latitude"].max()) + 10)
plt.ylim((city_df["Cloudiness (%)"].min()) - 5, (city_df["Cloudiness (%)"].max()) + 10)
plt.grid()

plt.title("City Cloudiness vs. Latitude (2/27/18)")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")

plt.savefig("clouds png")

plt.show()
```


![png](output_10_0.png)



```python
temp_scat = plt.scatter(city_df["Latitude"], city_df["Wind Speed (MPH)"], marker="o", color="b", edgecolors="black")

plt.xlim((city_df["Latitude"].min()) - 10, (city_df["Latitude"].max()) + 10)
plt.ylim((city_df["Wind Speed (MPH)"].min()) - 5,(city_df["Wind Speed (MPH)"].max()) + 5)
plt.grid()

plt.title("City Wind Speed vs. Latitude (2/27/18)")
plt.xlabel("Wind Speed (MPH)")
plt.ylabel("Temperature (F)")

plt.savefig("wind speed png")

plt.show()
```


![png](output_11_0.png)



```python
city_df.to_csv("City API Homework.csv")
```
