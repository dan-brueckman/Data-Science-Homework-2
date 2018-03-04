

```python
print("Analysis\n")
print("Trend 1: As it currently stands, the NY Times is the only twitter account with a mean compound sentiment score above zero. \n")
print("Trend 2: I have run this analysis a few times over the last few days, and the NY Times has consistently been slightly above zero, while no one else has risen above zero during that time. \n")
print("Trend 3: BBC World has been consistently the most negative over the last few days.")
```

    Analysis
    
    Trend 1: As it currently stands, the NY Times is the only twitter account with a mean compound sentiment score above zero. 
    
    Trend 2: I have run this analysis a few times over the last few days, and the NY Times has consistently been slightly above zero, while no one else has risen above zero during that time. 
    
    Trend 3: BBC World has been consistently the most negative over the last few days.
    


```python
import pandas as pd
import numpy as np
import tweepy
import time
import json
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

consumer_key = "MNtExuoBogl1cSCgbTg99axOn"
consumer_secret = "92ujLKA6rRo2hmYT5RUtFJWE7AcTY7rFNzdzSZwXN1yKAX5cfO"
access_token = "839884351219335169-wjwPEHm50YcZ2NRwdfsiEYVeJ2lNOq5"
access_token_secret = "Y2MlUCFEH6qP0x2eXE7FfD53B7Bp48UzUKBbRbhx0vbR3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```


```python
target_list = ['@FoxNews', '@BBCWorld', '@CBSNews', '@nytimes', '@CNN']
df = {}
```


```python
main_list = []

for target in target_list:
    sentiments = []
    counter = 1
    public_tweets = tweepy.Cursor(api.user_timeline, id=target).items(100) 
    
    for tweet in public_tweets:
        tweet_text = json.dumps(tweet._json, indent=3)
        tweet = json.loads(tweet_text)
        sentiments.append({"Date": tweet["created_at"], 
                       "Compound": analyzer.polarity_scores(tweet["text"])["compound"],
                       "Tweets Ago": counter})
        main_list.append({"Date": tweet["created_at"], 
                       "Compound": analyzer.polarity_scores(tweet["text"])["compound"],"Positive": analyzer.polarity_scores(tweet["text"])["pos"], "Negative": analyzer.polarity_scores(tweet["text"])["neg"], "Neutral": analyzer.polarity_scores(tweet["text"])["neu"],
                       "Tweets Ago": counter, "Network": target, "Tweet Text": tweet["text"]})
        counter += 1
        
    df[target] = pd.DataFrame.from_dict(sentiments)

main_df = pd.DataFrame.from_dict(main_list)
```


```python
df["@FoxNews"].head()
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
      <th>Compound</th>
      <th>Date</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.7906</td>
      <td>Sun Mar 04 23:03:00 +0000 2018</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Sun Mar 04 22:49:06 +0000 2018</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0000</td>
      <td>Sun Mar 04 22:48:43 +0000 2018</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.5267</td>
      <td>Sun Mar 04 22:40:34 +0000 2018</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0000</td>
      <td>Sun Mar 04 22:30:12 +0000 2018</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
fox = plt.scatter(df['@FoxNews']["Tweets Ago"], df['@FoxNews']["Compound"] , marker="o", color="r", edgecolors="black", label = "Fox News")
bbc = plt.scatter(df['@BBCWorld']["Tweets Ago"], df['@BBCWorld']["Compound"] , marker="o", color="b", edgecolors="black", label = "BBC World")
cbs = plt.scatter(df['@CBSNews']["Tweets Ago"], df['@CBSNews']["Compound"] , marker="o", color="g", edgecolors="black", label = "CBS News")
nytimes = plt.scatter(df['@nytimes']["Tweets Ago"], df['@nytimes']["Compound"] , marker="o", color="y", edgecolors="black", label = "NY Times")
cnn = plt.scatter(df['@CNN']["Tweets Ago"], df['@CNN']["Compound"] , marker="o", color="m", edgecolors="black", label = "CNN")

plt.xlim(max(df["@FoxNews"]["Tweets Ago"]) + 5, -5)
plt.ylim(-1,1)
plt.grid()

plt.title("Sentiment Analysis of Media Tweets 3/4/18")
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")

plt.legend(handles=[fox, bbc, cbs, nytimes, cnn], loc='upper left', bbox_to_anchor=(1,1))

plt.savefig("Sentiment Scatter")

plt.show()
```


![png](output_5_0.png)



```python
df_list = [df['@FoxNews'], df['@BBCWorld'], df['@CBSNews'], df['@nytimes'], df['@CNN']]
mean_list = []

for dataframe in df_list:
    mean_list.append(dataframe["Compound"].mean())

edgecolors = ["black", "black", "black", "black", "black"]
x_axis = np.arange(5)

x_ticks = ["Fox", "BBC", "CBS", "NY Times", "CNN"]
colors = ["r", "b", 'g', 'y', 'm']

tick_locations = [value+0.5 for value in x_axis]
plt.xticks(tick_locations, x_ticks)

plt.ylim(min(mean_list) - .05, max(mean_list) + .1)
plt.xlim(0,5)

news_bar = plt.bar(x_axis, mean_list, align="edge", color = colors, width = 1, edgecolor = edgecolors) 

plt.title("Overall Media Sentiment Based on Twitter 3/4/17")
plt.ylabel("Tweet Polarity")

plt.savefig("Overall Score Bar Graph")

plt.show()
```


![png](output_6_0.png)



```python
main_df.to_csv("Twitter Sentiment.csv")
```
