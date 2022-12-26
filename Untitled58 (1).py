#!/usr/bin/env python
# coding: utf-8

# In[2]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import time


# In[17]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[18]:


driver.get("https://www.amazon.in/")


# In[19]:


search_product = driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search_product.send_keys("guitar")


# In[20]:


search_btn = driver.find_element(By.XPATH,'//span[@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]')
search_btn.click()


# # question 2
# 

# In[22]:


#scraping all product urls

product_urls = []
start = 0
end = 3
for page in range(start,end):
    url = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url[0:10]:
        product_urls.append(i.get_attribute("href"))
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(2)


# In[23]:


len(product_urls)


# In[24]:


product_urls


# In[ ]:


Brand=[]

for url in product_urls:
    driver.get(url)
    time.sleep(5)
    
    try:
        brand = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[42]/div/table/tbody/tr[1]/td[2]/span')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')


# In[26]:


Product = []

for url in product_urls[:10]:
    driver.get(url)
    time.sleep(5)
    
    try:
        product = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[33]/div[1]/div[3]/div/div/div[2]/span/div/div/div/span[2]')
        Product.append(product.text)
    except NoSuchElementException:
        Product.append('-')


# In[30]:


Price = []

for url in product_urls[:10]:
    driver.get(url)
    time.sleep(2)
    
    try:
        price = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[10]/div/div[1]/div[3]/div[1]/span[2]/span[2]/span[2]')
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('-')


# In[36]:


Delivery = []

for url in product_urls[:10]:
    driver.get(url)
    time.sleep(2)
    
    try:
        delivery = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div/div[1]/div/div/div[1]/div/div[2]/div[12]/div[1]/div/div/div[2]')
        Delivery.append(delivery.text)
    except NoSuchElementException:
        Delivery.append('-')


# In[38]:


Return  = []

for url in product_urls[:10]:
    driver.get(url)
    time.sleep(2)
    
    try: 
        ret = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[5]/div[4]/div[4]/div[21]/div/div[1]/div[2]/div/div/div/div[3]/span/div[2]/a')
        Return.append(ret.text)
    except NoSuchElementException:
        Return.append('-')
        


# In[40]:


import pandas as pd


# In[41]:


df = pd.DataFrame({'Brand':Brand,'Product':Product,'expected_Delivery':Delivery,'Return':Return})
df


# In[ ]:





# In[ ]:





# # question 3

# In[92]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[93]:


driver.get("http://images.google.com/")


# In[94]:


search_product = driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_product.send_keys("Fruits")


# In[96]:


search_btn = driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_btn.click()


# In[98]:


for _ in range(20):
    driver.execute_script("window.scrollBy(0,1000)")
images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls= []
for image in images:
    source = image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)
            
            
for i  in range(len(img_urls)):
    if i>10:
        break 
        print("Downloading {0} of {1} images ".format(i,10))
        response = requests.get(img_urls[i])
        file = open(r"C:\Users\Kavisha\Downloads"+str(i)+".jpg","wb")
        file.write(response.content)


# In[ ]:





# # question 4
# 

# In[15]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[16]:


driver.get("http://www.flipkart.com/")


# In[17]:


search_product = driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_product.send_keys("pixel 4A")


# In[18]:


search_btn = driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn.click()


# In[21]:


product_urls = []

url = driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    product_urls.append(i.get_attribute("href"))


# In[22]:


len(product_urls)


# In[23]:


Brand = []
Phone_name = []
Colour = []
RAM = []
Storage = []
Primary_Camera = []
Secondary_Camera = []
Display_Size = []
Display_Resolution= []
Processor = []
Processor_Cores = []
Battery_Capacity = []
Price = []
URL = []


# In[24]:


product_urls


# In[25]:


Brand=[]

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand = driver.find_element(By.XPATH,'//span[@class="B_NuCI"]')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')


# In[34]:


Phone_name = []

for  url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        name = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[3]/td[2]/ul/li')
        Phone_name.append(name.text)
    except NoSuchElementException:
        Phone_name.append('-')


# In[36]:


Colour = []

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        colour = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[4]/td[2]/ul/li")
        Colour.append(colour.text)
    except NoSuchElementException:
        Colour.append('-')


# In[37]:


RAM = []

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        ram = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table[1]/tbody/tr[2]/td[2]/ul/li')
        RAM.append(ram.text)
    except NoSuchElementException:
        RAM.append('-')
        
     


# In[38]:


Storage = []

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        storage = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table[1]/tbody/tr[1]/td[2]/ul/li')
        Storage.append(storage.text)
    except NoSuchElementException:
        Storage.append('-')


# In[41]:


Primary_Camera = []

for url in product_urls:
    driver.get(url)
    time.sleep(2)
    
    try:
        camera = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table[1]/tbody/tr[2]/td[2]/ul/li')
        Primary_Camera.append(camera.text)
    except NoSuchElementException:
        Primary_Camera.append('-')


# In[44]:


import pandas as pd

df2 = pd.DataFrame({'Brand':Brand,'Phone_name':Phone_name,'colour':Colour,'RAM':RAM,'Storage':Storage,'Primary_Camera':Primary_Camera})
df2


# # QUESTION 5

# In[46]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[47]:


driver.get('https://www.google.co.in/maps')


# In[50]:



search_city = driver.find_element(By.XPATH,'//input[@class="searchboxinput xiQnY"]')
search_city.send_keys("Pune")



# In[51]:


search_btn = driver.find_element(By.XPATH,'//button[@class="mL3xi"]')
search_btn.click()


# In[55]:


try:
    url_string = driver.current_url
    print("URL Extracted: ", url_str)
    latitude_longitude = re.findall(r'@(.*)data',url_string)
    if len(latitude_longitude):
        lat_lng_list = latitude_longitude[0].split(",")
        if len(lat_lng_list)>=2:
            latitude = lat_lng_list[0]
            longitude = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(latitude, longitude))
except Exception as e:
        print("Error: ", str(e))


# # question 7

# In[58]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[59]:


driver.get('https://www.digit.in/')


# In[61]:


best_gam_laptops = driver.find_element(By.XPATH,"//div[@class='listing_container']//ul//li[9]").click()
time.sleep(3)


# In[62]:


Laptop_Name = []
Operating_sys = []
Display = []
Processor = []
Memory = []
Price = []


# In[82]:


laptop_name = driver.find_elements(By.XPATH,"//div[@class='right-container']/div/a/h3")
for name in laptop_name:
    Laptop_Name.append(name.text)
    


# In[73]:


try:
    op_sys = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[1]/div/div")
    for os in op_sys:
        Operating_sys.append(os.text)
except NoSuchElementException:
    pass


# In[74]:


try:
    display = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[2]/div/div")
    for disp in display:
        Display.append(disp.text)
except NoSuchElementException:
    pass


# In[75]:


try:
    processor = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[5]/td[3]")
    for pro in processor:
        Processor.append(pro.text)
except NoSuchElementException:
    pass


# In[76]:


try:
    memory = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[6]/td[3]")
    for memo in memory:
        Memory.append(memo.text)
except NoSuchElementException:
    pass


# In[79]:


try:
    price = driver.find_elements(By.XPATH,"//td[@class='smprice']")
    for pri in price:
        Price.append(pri.text.replace('₹ ','Rs'))
except NoSuchElementException:
    pass


# # QUESTION 8

# In[3]:


driver = webdriver.Chrome(r"C:\Users\Kavisha\Downloads\chromedriver_win32 (3)\chromedriver.exe")


# In[4]:


driver.get('http://www.forbes.com/')


# In[5]:


Rank = []
Person_Name = []
Net_worth = []
Age = []
Citizenship = []
Source = []
Industry = []


# In[ ]:


while(True):
    
    # scraping the data of rank of the billionaires
    rank_tag = driver.find_elements(By.XPATH,"//div[@class='rank']")
    for rank in rank_tag:
        Rank.append(rank.text)
    time.sleep(1)
    
    
 
    # scraping the data  of names of the billionaires
    name_tag = driver.find_elements(By.XPATH,"//div[@class='personName']/div")
    for name in name_tag:
        Person_Name.append(name.text)
    time.sleep(1)
    
    
    # scraping the data of age of the billionaires
    age_tag = driver.find_elements(By.XPATH,"//div[@class='age']/div")
    for age in age_tag:
        Age.append(age.text)
    time.sleep(1)
    
    
    # scraping the data of citizenship of the billionaires
    cit_tag = driver.find_elements(By.XPATH,"//div[@class='countryOfCitizenship']")
    for cit in cit_tag:
        Citizenship.append(cit.text)
    time.sleep(1)


# In[ ]:


# scraping the data of source of income of the billionaires
  sour_tag = driver.find_elements_by_xpath("//div[@class='source']")
  for sour in sour_tag:
      Source.append(sour.text)
  time.sleep(1)
  
  
  # scraping data of industry of the billionaires
  ind_tag = driver.find_elements_by_xpath("//div[@class='category']//div")
  for ind in ind_tag:
      Industry.append(ind.text)
  time.sleep(1)
  
  
  # scraping data of net_worth of billionaires
  net_tag = driver.find_elements_by_xpath("//div[@class='netWorth']/div")
  for net in net_tag:
      Net_worth.append(net.text)
  time.sleep(1)

