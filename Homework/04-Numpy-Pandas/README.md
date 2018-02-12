

```python
import pandas as pd
import os
csv_file = os.path.join(".", "purchase_data.csv")
heroes = pd.read_csv(csv_file)
heroes_2 = pd.read_csv(csv_file)
heroes_3 = pd.read_csv(csv_file)
```


```python
player_count = len(heroes["SN"].unique())
total_players_df = pd.DataFrame({"Total Players": [player_count]})
total_players_df
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_count = len(heroes["Item ID"].unique())
avg_price = heroes["Price"].mean()
total_purchases = len(heroes.index)
total_revenue = heroes["Price"].sum()
purchasing_analysis_total_df = pd.DataFrame({"Number of Unique Items": [item_count], "Average Purchase Price": [avg_price], "Total Number of Purchases": [total_purchases], "Total Revenue": [total_revenue]})
purchasing_analysis_total_df["Average Purchase Price"] = purchasing_analysis_total_df["Average Purchase Price"].map('${:,.2f}'.format)
purchasing_analysis_total_df["Total Revenue"] = purchasing_analysis_total_df["Total Revenue"].map('${:,.2f}'.format)
purchasing_analysis_total_df
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
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$2.93</td>
      <td>183</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
gender_group = heroes.groupby("Gender")
gender_count_df = pd.DataFrame((gender_group["Gender"].count()/total_purchases)*100).round(2)
gender_count_df["Total Count"] = gender_group["Gender"].count()
gender_count_df = gender_count_df.rename(columns={"Gender": "Percentage of Players"})
gender_count_df
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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.44</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
gender_purchases_df = pd.DataFrame({"Purchase Count": gender_group["Gender"].count(), "Avg Purchase Price": gender_group["Price"].mean(), "Total Purchase Value": gender_group["Price"].sum(), "Normalized Totals": gender_group["Price"].sum()/gender_group["Gender"].count() }).round(2)

gender_purchases_df["Total Purchase Value"] = gender_purchases_df["Total Purchase Value"].map('${:,.2f}'.format)
gender_purchases_df["Normalized Totals"] = gender_purchases_df["Normalized Totals"].map('${:,.2f}'.format)
gender_purchases_df["Avg Purchase Price"] = gender_purchases_df["Avg Purchase Price"].map('${:,.2f}'.format)

gender_purchases_df
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
      <th>Avg Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$2.82</td>
      <td>$2.82</td>
      <td>136</td>
      <td>$382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$2.95</td>
      <td>$2.95</td>
      <td>633</td>
      <td>$1,867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.25</td>
      <td>$3.25</td>
      <td>11</td>
      <td>$35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
bins = [0,10, 15, 20, 25, 30, 35, 40, 100 ]
group_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
heroes["Age Group"] = pd.cut(heroes["Age"], bins, labels=group_labels)

age_group_df = heroes.groupby("Age Group")
age_demo_df = pd.DataFrame((age_group_df["Age Group"].count()/total_purchases)*100).round(2)
age_demo_df["Total Count"] = age_group_df["Age Group"].count()
age_demo_df = age_demo_df.rename(columns={"Age Group": "Percentage of Players"})

age_demo_df
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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>4.10</td>
      <td>32</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>10.00</td>
      <td>78</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>23.59</td>
      <td>184</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>39.10</td>
      <td>305</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>9.74</td>
      <td>76</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>7.44</td>
      <td>58</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>5.64</td>
      <td>44</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>0.38</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
age_group_summary = pd.DataFrame({"Purchase Count": age_group_df["Age Group"].count(), "Avg Purchase Price": age_group_df["Price"].mean(), "Total Purchase Value": age_group_df["Price"].sum(), "Normalized Totals": age_group_df["Price"].sum()/age_group_df["Age Group"].count() }).round(2)

age_group_summary["Total Purchase Value"] = age_group_summary["Total Purchase Value"].map('${:,.2f}'.format)
age_group_summary["Normalized Totals"] = age_group_summary["Normalized Totals"].map('${:,.2f}'.format)
age_group_summary["Avg Purchase Price"] = age_group_summary["Avg Purchase Price"].map('${:,.2f}'.format)

age_group_summary
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
      <th>Avg Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>$3.02</td>
      <td>$3.02</td>
      <td>32</td>
      <td>$96.62</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>$2.87</td>
      <td>$2.87</td>
      <td>78</td>
      <td>$224.15</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>$2.87</td>
      <td>$2.87</td>
      <td>184</td>
      <td>$528.74</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>$2.96</td>
      <td>$2.96</td>
      <td>305</td>
      <td>$902.61</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>$2.89</td>
      <td>$2.89</td>
      <td>76</td>
      <td>$219.82</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>$3.07</td>
      <td>$3.07</td>
      <td>58</td>
      <td>$178.26</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>$2.90</td>
      <td>$2.90</td>
      <td>44</td>
      <td>$127.49</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>$2.88</td>
      <td>$2.88</td>
      <td>3</td>
      <td>$8.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
sn_group = heroes.groupby("SN")
sn_group["Price"].sum().nlargest(5)
```




    SN
    Undirrala66    17.06
    Saedue76       13.56
    Mindimnya67    12.74
    Haellysu29     12.73
    Eoda93         11.58
    Name: Price, dtype: float64




```python
heroes_2.set_index("SN", inplace=True)

top_5 = heroes_2.loc[["Undirrala66", "Saedue76", "Mindimnya67", "Haellysu29", "Eoda93"]]

top_group = top_5.groupby("SN")

top_df = pd.DataFrame({"Purchase Count": top_group["Price"].count(), "Average Purchase Price": top_group["Price"].mean(), "Total Purchase Value": top_group["Price"].sum()}).round(2)

top_df["Total Purchase Value"] = top_df["Total Purchase Value"].map('${:,.2f}'.format)
top_df["Average Purchase Price"] = top_df["Average Purchase Price"].map('${:,.2f}'.format)

top_df.sort_values("Total Purchase Value", ascending = False, inplace = True)

top_df 
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
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$3.41</td>
      <td>5</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$3.39</td>
      <td>4</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$3.18</td>
      <td>4</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>$4.24</td>
      <td>3</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>$3.86</td>
      <td>3</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_group = heroes.groupby("Item Name")
item_group["Price"].count().nlargest(10)
```




    Item Name
    Final Critic                            14
    Arcane Gem                              11
    Betrayal, Whisper of Grieving Widows    11
    Stormcaller                             10
    Retribution Axe                          9
    Serenity                                 9
    Trickster                                9
    Woeful Adamantite Claymore               9
    Bonecarvin Battle Axe                    8
    Conqueror Adamantite Mace                8
    Name: Price, dtype: int64




```python
heroes_3.set_index("Item Name", inplace=True)

top_items = heroes_3.loc[["Final Critic", "Arcane Gem", "Betrayal, Whisper of Grieving Widows", "Stormcaller", "Retribution Axe", "Serenity", "Trickster", "Woeful Adamantite Claymore"]]
top_items_group = top_items.groupby(["Item Name", "Item ID"])

items_df = pd.DataFrame({"Purchase Count": top_items_group["Price"].count(), "Total Purchase Value": top_items_group["Price"].sum(), "Item Price":top_items_group["Price"].sum()/top_items_group["Price"].count() })
items_df["Total Purchase Value"] = items_df["Total Purchase Value"].map('${:,.2f}'.format)
items_df["Item Price"] = items_df["Item Price"].map('${:,.2f}'.format)
items_df
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
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arcane Gem</th>
      <th>84</th>
      <td>$2.23</td>
      <td>11</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>39</th>
      <td>$2.35</td>
      <td>11</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Final Critic</th>
      <th>92</th>
      <td>$1.36</td>
      <td>8</td>
      <td>$10.88</td>
    </tr>
    <tr>
      <th>101</th>
      <td>$4.62</td>
      <td>6</td>
      <td>$27.72</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <th>34</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>Serenity</th>
      <th>13</th>
      <td>$1.49</td>
      <td>9</td>
      <td>$13.41</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Stormcaller</th>
      <th>30</th>
      <td>$4.15</td>
      <td>5</td>
      <td>$20.75</td>
    </tr>
    <tr>
      <th>180</th>
      <td>$2.78</td>
      <td>5</td>
      <td>$13.90</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <th>31</th>
      <td>$2.07</td>
      <td>9</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>Woeful Adamantite Claymore</th>
      <th>175</th>
      <td>$1.24</td>
      <td>9</td>
      <td>$11.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
item_group["Price"].sum().nlargest(10)
```




    Item Name
    Final Critic                            38.60
    Retribution Axe                         37.26
    Stormcaller                             34.65
    Spectral Diamond Doomblade              29.75
    Orenmir                                 29.70
    Singed Scalpel                          29.22
    Splitter, Foe Of Subtlety               28.88
    Thorn, Satchel of Dark Souls            27.06
    Fiery Glass Crusader                    26.70
    Betrayal, Whisper of Grieving Widows    25.85
    Name: Price, dtype: float64




```python
top_rev_items = heroes_3.loc[["Final Critic", "Retribution Axe", "Stormcaller", "Spectral Diamond Doomblade", "Orenmir"]]
top_rev_items_gb = top_rev_items.groupby(["Item Name", "Item ID"])

revenue_df = pd.DataFrame({"Purchase Count": top_rev_items_gb["Price"].count(), "Total Purchase Value": top_rev_items_gb["Price"].sum(), "Item Price": top_rev_items_gb["Price"].sum()/top_rev_items_gb["Price"].count() })
revenue_df["Total Purchase Value"] = revenue_df["Total Purchase Value"].map('${:,.2f}'.format)
revenue_df["Item Price"] = revenue_df["Item Price"].map('${:,.2f}'.format)

revenue_df
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
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Final Critic</th>
      <th>92</th>
      <td>$1.36</td>
      <td>8</td>
      <td>$10.88</td>
    </tr>
    <tr>
      <th>101</th>
      <td>$4.62</td>
      <td>6</td>
      <td>$27.72</td>
    </tr>
    <tr>
      <th>Orenmir</th>
      <th>32</th>
      <td>$4.95</td>
      <td>6</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <th>34</th>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>Spectral Diamond Doomblade</th>
      <th>115</th>
      <td>$4.25</td>
      <td>7</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Stormcaller</th>
      <th>30</th>
      <td>$4.15</td>
      <td>5</td>
      <td>$20.75</td>
    </tr>
    <tr>
      <th>180</th>
      <td>$2.78</td>
      <td>5</td>
      <td>$13.90</td>
    </tr>
  </tbody>
</table>
</div>


