#!/usr/bin/env python
# coding: utf-8

# In[86]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[87]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[ ]:


#visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


#use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


#use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[ ]:


#visit url
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[ ]:


#find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


#parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


#find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# ### Scrape High-Resolution Mars’ Hemisphere Images and Titles

# #### Hemispheres

# In[88]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[89]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for hemisphere in range(0, 4):
    hemispheres = {html_url : title}
    
    full_image_elem = browser.find_by_tag('h3')[hemisphere]
    full_image_elem.click()
    
    html = browser.html
    html_soup = soup(html, 'html.parser')
    
    html_url_rel = html_soup.find('img', class_='wide-image').get('src')
    html_url = f'https://marshemispheres.com/{html_url_rel}'
    
    title = html_soup.find('h2').get_text()
    
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[90]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[91]:


# 5. Quit the browser
browser.quit()


# In[ ]:




