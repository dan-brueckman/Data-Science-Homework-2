

```python
print("Analysis")
print("Trend 1: Of the 4 drugs analyzed here, Capomulin had the highest survival rate, losing less than 20% of mice studied. The next best drug (Ketapril), lost 40% of mice.")
print("Trend 2: Of the 4 drugs analyzed here, Capomulin had the fewest instances of metastatic spread during treatment. Capomulin had an average of 1.5 new sites by the 45th day. The next closest (Infubinol) had just over 2 sites on average.")
print("Trend 3: Of the 4 drugs analyzed here, Capomulin was the only drug to show an actual decrease in tumor volume during the study. Tumor volume decreased on average by nearly 20%, while it's closest competitor in the study showed tumor volume increases of 46% on average.")
```

    Analysis
    Trend 1: Of the 4 drugs analyzed here, Capomulin had the highest survival rate, losing less than 20% of mice studied. The next best drug (Ketapril), lost 40% of mice.
    Trend 2: Of the 4 drugs analyzed here, Capomulin had the fewest instances of metastatic spread during treatment. Capomulin had an average of 1.5 new sites by the 45th day. The next closest (Infubinol) had just over 2 sites on average.
    Trend 3: Of the 4 drugs analyzed here, Capomulin was the only drug to show an actual decrease in tumor volume during the study. Tumor volume decreased on average by nearly 20%, while it's closest competitor in the study showed tumor volume increases of 46% on average.
    


```python
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
mouse_csv = os.path.join(".", "mouse_drug_data.csv")
drug_csv = os.path.join(".", "clinicaltrial_data.csv" )

mouse_df = pd.read_csv(mouse_csv)
drug_df = pd.read_csv(drug_csv)

drug_list = ['Capomulin', 'Infubinol', 'Ketapril', 'Placebo']
timepoint = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

```


```python
original_df = mouse_df.merge(drug_df, how = "outer", on = "Mouse ID")
original_df = original_df.loc[(original_df["Drug"] == "Capomulin") | (original_df["Drug"] == "Infubinol") | (original_df["Drug"] == "Ketapril") | (original_df["Drug"] == "Placebo")]

df_2 = mouse_df.merge(drug_df, how = "outer", on = "Mouse ID")
df_2 = original_df.loc[(original_df["Drug"] == "Capomulin") | (original_df["Drug"] == "Infubinol") | (original_df["Drug"] == "Ketapril") | (original_df["Drug"] == "Placebo")]

df_3 = mouse_df.merge(drug_df, how = "outer", on = "Mouse ID")
df_3 = original_df.loc[(original_df["Drug"] == "Capomulin") | (original_df["Drug"] == "Infubinol") | (original_df["Drug"] == "Ketapril") | (original_df["Drug"] == "Placebo")]

original_df.head()
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
      <th>Mouse ID</th>
      <th>Drug</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
      <th>Metastatic Sites</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>393</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>394</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>5</td>
      <td>47.864440</td>
      <td>0</td>
    </tr>
    <tr>
      <th>395</th>
      <td>q119</td>
      <td>Ketapril</td>
      <td>10</td>
      <td>51.236606</td>
      <td>0</td>
    </tr>
    <tr>
      <th>396</th>
      <td>n923</td>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>397</th>
      <td>n923</td>
      <td>Ketapril</td>
      <td>5</td>
      <td>45.824881</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
original_df.drop(original_df.columns[[0, 4]], axis = 1, inplace = True)
original_df.head()
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
      <th>Drug</th>
      <th>Timepoint</th>
      <th>Tumor Volume (mm3)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>393</th>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>394</th>
      <td>Ketapril</td>
      <td>5</td>
      <td>47.864440</td>
    </tr>
    <tr>
      <th>395</th>
      <td>Ketapril</td>
      <td>10</td>
      <td>51.236606</td>
    </tr>
    <tr>
      <th>396</th>
      <td>Ketapril</td>
      <td>0</td>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>397</th>
      <td>Ketapril</td>
      <td>5</td>
      <td>45.824881</td>
    </tr>
  </tbody>
</table>
</div>




```python
tumor_response_gb = original_df.groupby(["Drug", "Timepoint"])
tumor_response_analysis = tumor_response_gb.mean()

capomulin_1 = tumor_response_analysis.loc["Capomulin"]
infubinol_1 = tumor_response_analysis.loc['Infubinol']
ketapril_1 = tumor_response_analysis.loc['Ketapril']
placebo_1 = tumor_response_analysis.loc['Placebo']

tumor_response_sem = tumor_response_gb.sem()
capomulin_tumor_se = tumor_response_sem.loc["Capomulin"]
infubinol_tumor_se = tumor_response_sem.loc['Infubinol']
ketapril_tumor_se = tumor_response_sem.loc['Ketapril']
placebo_tumor_se = tumor_response_sem.loc['Placebo']

capomulin_1.head()
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
      <th>Tumor Volume (mm3)</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>45.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44.266086</td>
    </tr>
    <tr>
      <th>10</th>
      <td>43.084291</td>
    </tr>
    <tr>
      <th>15</th>
      <td>42.064317</td>
    </tr>
    <tr>
      <th>20</th>
      <td>40.716325</td>
    </tr>
  </tbody>
</table>
</div>




```python
capomulin_ta = plt.scatter(timepoint, capomulin_1['Tumor Volume (mm3)'], marker="o", color="r", edgecolors="black", label = "Capomulin")
infubinol_ta = plt.scatter(timepoint, infubinol_1['Tumor Volume (mm3)'], marker="+", color="b", edgecolors="black", label = "Infubinol")
ketapril_ta = plt.scatter(timepoint, ketapril_1['Tumor Volume (mm3)'], marker="<", color="y", edgecolors="black", label = "Ketapril")
placebo_ta = plt.scatter(timepoint, placebo_1['Tumor Volume (mm3)'], marker="*", color="g", edgecolors="black", label = "Placebo")

plt.errorbar(timepoint, capomulin_1['Tumor Volume (mm3)'], yerr= capomulin_tumor_se['Tumor Volume (mm3)'], barsabove = True, capsize = 3, color = "r")
plt.errorbar(timepoint, infubinol_1['Tumor Volume (mm3)'], yerr= infubinol_tumor_se['Tumor Volume (mm3)'], barsabove = True, capsize = 3, color = "b")
plt.errorbar(timepoint, ketapril_1['Tumor Volume (mm3)'], yerr= ketapril_tumor_se['Tumor Volume (mm3)'], barsabove = True, capsize = 3, color = "y")
plt.errorbar(timepoint, placebo_1['Tumor Volume (mm3)'], yerr= placebo_tumor_se['Tumor Volume (mm3)'], barsabove = True, capsize = 3, color = "g")

plt.xlim(min(timepoint), max(timepoint))
plt.ylim(30,80)
plt.xticks(np.arange(0, 50, 5.0))
plt.grid()

plt.title("Tumor Response to Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Tumor Volume (mm3)")

plt.legend(handles=[capomulin_ta, infubinol_ta, ketapril_ta, placebo_ta ], loc="best")

plt.show()
```


![png](output_6_0.png)



```python
df_2.drop(df_2.columns[[0, 3]], axis = 1, inplace = True)
```


```python
metastatic_response_gb = df_2.groupby(["Drug", "Timepoint"])
metastatic_response_analysis = metastatic_response_gb.mean()

capomulin_2 = metastatic_response_analysis.loc["Capomulin"]
infubinol_2 = metastatic_response_analysis.loc['Infubinol']
ketapril_2 = metastatic_response_analysis.loc['Ketapril']
placebo_2 = metastatic_response_analysis.loc['Placebo']

metastatic_response_sem = metastatic_response_gb.sem()
capomulin_metastatic_se = metastatic_response_sem.loc["Capomulin"]
infubinol_metastatic_se = metastatic_response_sem.loc['Infubinol']
ketapril_metastatic_se = metastatic_response_sem.loc['Ketapril']
placebo_metastatic_se = metastatic_response_sem.loc['Placebo']

capomulin_2.head()
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
      <th>Metastatic Sites</th>
    </tr>
    <tr>
      <th>Timepoint</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.160000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.320000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.375000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.652174</td>
    </tr>
  </tbody>
</table>
</div>




```python
capomulin_ma = plt.scatter(timepoint, capomulin_2['Metastatic Sites'], marker="o", color="r", edgecolors="black", label = "Capomulin")
infubinol_ma = plt.scatter(timepoint, infubinol_2['Metastatic Sites'], marker="+", color="b", edgecolors="black", label = "Infubinol")
ketapril_ma = plt.scatter(timepoint, ketapril_2['Metastatic Sites'], marker="<", color="y", edgecolors="black", label = "Ketapril")
placebo_ma = plt.scatter(timepoint, placebo_2['Metastatic Sites'], marker="*", color="g", edgecolors="black", label = "Placebo")

plt.errorbar(timepoint, capomulin_2['Metastatic Sites'], yerr= capomulin_metastatic_se['Metastatic Sites'], barsabove = True, capsize = 3, color = "r")
plt.errorbar(timepoint, infubinol_2['Metastatic Sites'], yerr= infubinol_metastatic_se['Metastatic Sites'], barsabove = True, capsize = 3, color = "b")
plt.errorbar(timepoint, ketapril_2['Metastatic Sites'], yerr= ketapril_metastatic_se['Metastatic Sites'], barsabove = True, capsize = 3, color = "y")
plt.errorbar(timepoint, placebo_2['Metastatic Sites'], yerr= placebo_metastatic_se['Metastatic Sites'], barsabove = True, capsize = 3, color = "g")

plt.xlim(min(timepoint), max(timepoint))
plt.ylim(0,max(metastatic_response_analysis["Metastatic Sites"])+1)
plt.xticks(np.arange(0, 50, 5.0))
plt.grid()

plt.title("Metastatic Spread During Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Metastatic Sites")

plt.legend(handles=[capomulin_ta, infubinol_ta, ketapril_ta, placebo_ta ], loc="best")

plt.show()
```


![png](output_9_0.png)



```python
df_3.drop(original_df.columns[[3, 4]], axis = 1, inplace = True)
```


```python
survival_gb = df_3.groupby(["Drug", "Timepoint"])
survival_analysis = survival_gb.count()

capomulin_3 = survival_analysis.loc["Capomulin"]
infubinol_3 = survival_analysis.loc['Infubinol']
ketapril_3 = survival_analysis.loc['Ketapril']
placebo_3 = survival_analysis.loc['Placebo']

```


```python
capomulin_sr = plt.scatter(timepoint, (capomulin_3['Mouse ID']/max(capomulin_3['Mouse ID']))*100, marker="o", color="r", edgecolors="black", label = "Capomulin")
infubinol_sr = plt.scatter(timepoint, (infubinol_3['Mouse ID']/max(infubinol_3['Mouse ID']))*100, marker="+", color="b", edgecolors="black", label = "Infubinol")
ketapril_sr = plt.scatter(timepoint, (ketapril_3['Mouse ID']/max(ketapril_3['Mouse ID']))*100, marker="<", color="y", edgecolors="black", label = "Ketapril")
placebo_sr = plt.scatter(timepoint, (placebo_3['Mouse ID']/max(placebo_3['Mouse ID']))*100, marker="*", color="g", edgecolors="black", label = "Placebo")

plt.xlim(min(timepoint), max(timepoint))
plt.ylim(0, 100)
plt.xticks(np.arange(0, 50, 5.0))
plt.grid()

plt.title("Survival During Treatment")
plt.xlabel("Time (Days)")
plt.ylabel("Survival Rate (%)")

plt.legend(handles=[capomulin_ta, infubinol_ta, ketapril_ta, placebo_ta ], loc="best")

plt.show()
```


![png](output_12_0.png)



```python
cap_tumor_changes = (((capomulin_1['Tumor Volume (mm3)'].iloc[9]-capomulin_1['Tumor Volume (mm3)'].iloc[0])/45)*100)
inf_tumor_changes = (((infubinol_1['Tumor Volume (mm3)'].iloc[9]-infubinol_1['Tumor Volume (mm3)'].iloc[0])/45)*100)
ket_tumor_changes = (((ketapril_1['Tumor Volume (mm3)'].iloc[9]-ketapril_1['Tumor Volume (mm3)'].iloc[0])/45)*100)
pla_tumor_changes = (((placebo_1['Tumor Volume (mm3)'].iloc[9]-placebo_1['Tumor Volume (mm3)'].iloc[0])/45)*100)

tumor_change_series = pd.Series([cap_tumor_changes, inf_tumor_changes, ket_tumor_changes, pla_tumor_changes], index = drug_list)

tumor_change_series.plot(kind = "bar", color = "g")

plt.title("Tumor Change over 45 Day Treatment")
plt.ylabel("% Tumor Volume Change")

plt.ylim(min(tumor_change_series - 20), max(tumor_change_series + 20))
plt.grid()


plt.show()
```


![png](output_13_0.png)

