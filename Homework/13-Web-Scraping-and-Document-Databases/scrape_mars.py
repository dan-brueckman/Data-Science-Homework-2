
# coding: utf-8

# In[137]:


from os import getcwd
from os.path import join
from bs4 import BeautifulSoup as bs
import requests as req
from splinter import Browser
import pandas as pd


# In[ ]:


#MARS NEWS:


# In[186]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
response = req.get(url)
soup = bs(response.text, 'html.parser')


# In[187]:


results = soup.find_all('div', class_="image_and_description_container")


# In[188]:


counter = 0
for result in results:
    if counter == 0:
        try:
            news_p = result.find('div', class_="rollover_description_inner").text
            if (news_p):
                print(news_p)
        except Exception as e:
            print(e)
        counter += 1


# In[ ]:


#JPL IMAGES


# In[84]:


executable_path = {"executable_path": 'C:\\Users\\dan.brueckman\\Desktop\\chromedriver.exe'}


# In[125]:


jpl_link_main = 'www.jpl.nasa.gov'
browser = Browser('chrome', **executable_path, headless = True)
url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_jpl)


# In[126]:


browser.click_link_by_id('full_image')
html = browser.html
soup = bs(html, 'html.parser')


# In[127]:


jpl_results = soup.find_all('a', class_="button fancybox")


# In[128]:


counter = 0
for result in jpl_results:
    if counter == 0:
        try:
            featured_image_url = jpl_link_main + result['data-fancybox-href']
            print(featured_image_url)
        except Exception as e:
            print(e)
        counter += 1
        


# In[129]:


#MARS WEATHER


# In[134]:


weather_url = 'https://twitter.com/marswxreport?lang=en'
response = req.get(weather_url)
soup = bs(response.text, 'html.parser')


# In[135]:


weather_results = soup.find_all('p', class_="TweetTextSize")
counter = 0
for result in weather_results:
    if counter == 0:
        try:
            mars_weather = result.text
            print(mars_weather)
        except Exception as e:
            print(e)
        counter += 1


# In[136]:


#MARS FACTS


# In[141]:


facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)


# In[150]:


facts_df = tables[0]
facts_df.rename(columns={0: "Profile", 1: "Attributes"})


# In[152]:


html_table = facts_df.to_html()


# In[153]:


#MARS HEMISPHERES


# In[154]:


astro_link = 'https://astropedia.astrogeology.usgs.gov'
hem_links = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']


# In[174]:


browser = Browser('chrome', **executable_path, headless = True)
hemisphere_image_urls = []
for link in hem_links:
    browser.visit(link)
    img = browser.find_link_by_partial_href('.tif/full.jpg')
    img_url = img['href']
    print(img_url)
    response = req.get(link)
    soup = bs(response.text, 'html.parser')
    result = soup.find('h2', class_='title')
    img_title = result.text
    print(img_title)
    hemisphere_image_urls.append({"title": img_title, "img_url": img_url})
    


# In[175]:


# In[176]:


#SCRAPE FUNCTION


# In[195]:


def scrape():
    """scrapes everything above"""
    
    all_data = []
    
    #MARS NEWS
    
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = req.get(url)
    soup = bs(response.text, 'html.parser')
    results = soup.find_all('div', class_="image_and_description_container")
    counter = 0
    for result in results:
        if counter == 0:
            news_p = result.find('div', class_="rollover_description_inner").text
            counter += 1
    all_data.append({"news_p": news_p})
    
    #JPL IMAGES
    
    executable_path = {"executable_path": 'C:\\Users\\dan.brueckman\\Desktop\\chromedriver.exe'}
    jpl_link_main = 'www.jpl.nasa.gov'
    browser = Browser('chrome', **executable_path, headless = True)
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)
    browser.click_link_by_id('full_image')
    html = browser.html
    soup = bs(html, 'html.parser')
    jpl_results = soup.find_all('a', class_="button fancybox")
    counter = 0
    for result in jpl_results:
        if counter == 0:
            featured_image_url = jpl_link_main + result['data-fancybox-href']
            counter += 1
    all_data.append({"featured_image_url": featured_image_url})
    
    #MARS WEATHER
    
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    response = req.get(weather_url)
    soup = bs(response.text, 'html.parser')
    weather_results = soup.find_all('p', class_="TweetTextSize")
    counter = 0
    for result in weather_results:
        if counter == 0:
            mars_weather = result.text
            counter += 1
    all_data.append({"weather": mars_weather})
    
    #MARS FACTS
    
    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    facts_df = tables[0]
    facts_df.rename(columns={0: "Profile", 1: "Attributes"})
    html_table = facts_df.to_html()
    all_data.append({"html_table": html_table})
    
    #MARS HEMISPHERES
    
    astro_link = 'https://astropedia.astrogeology.usgs.gov'
    hem_links = ['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
            'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced', 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
    browser = Browser('chrome', **executable_path, headless = True)
    hemisphere_image_urls = []
    for link in hem_links:
        browser.visit(link)
        img = browser.find_link_by_partial_href('.tif/full.jpg')
        img_url = img['href']
        response = req.get(link)
        soup = bs(response.text, 'html.parser')
        result = soup.find('h2', class_='title')
        img_title = result.text
        hemisphere_image_urls.append({"title": img_title, "img_url": img_url})
    all_data.append({"hemisphere_images": hemisphere_image_urls})
    return all_data


# In[196]:




# In[ ]:




