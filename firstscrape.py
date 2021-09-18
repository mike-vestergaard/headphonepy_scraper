from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

elgiganten = "https://www.elgiganten.se/product/ljud-hifi/horlurar/200693/sony-tradlosa-around-ear-horlurar-wh-1000xm4-svart?_gl=1*lrlmct*_up*MQ..&gclid=EAIaIQobChMI7fj12fuH8wIVxKOyCh22NgKwEAQYASABEgJ5EvD_BwE&gclsrc=aw.ds"
mediamarkt = "https://www.mediamarkt.se/sv/product/_sony-wh-1000xm4-brusreducerande-tr%C3%A5dl%C3%B6sa-h%C3%B6rlurar-svart-1323521.html"
webhallen = "https://www.webhallen.com/se/product/322871-Sony-WH-1000XM4-Svart"

# Create a webddriver object for chrome-option and configure
wait_imp = 10
co = webdriver.ChromeOptions()
co.add_experimental_option('useAutomationExtension', False)
co.add_argument('--ignore-certificate-errors')
co.add_argument('start-maximized')
wd = webdriver.Chrome(r'C:\Users\mikev\Desktop\Coding Projects\headphonepy_scraper\chromedriver.exe',options=co)
print('******************************************************************************** \n')
print('                     Starting Program, Please wait......                 \n')
print('Connecting to Webhallen')

# Webhallen Source
wd.get(webhallen)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath("/html/body/div[2]")
raw_a = f_price.text
# print(r_price[1:])
print('-----> Successfully retrieved the price from Webhallen  \n')
time.sleep(2)

# Media Markt Source
print('Connecting to MediaMarkt')
wd.get(mediamarkt)
wd.implicitly_wait(wait_imp)
pr_price = wd.find_element_by_xpath("/html/body/div[3]")
raw_b = pr_price.text
# print (raw_c[1:7])
print ('-----> Successfully retrieved the price from MediaMarkt  \n')

# Elgiganten Source
print('Connecting to Elgiganten')
wd.get(elgiganten)
wd.implicitly_wait(wait_imp)
pr_price = wd.find_element_by_xpath("/html/body/div[4]/main/div[1]/section[1]/div[3]/div[3]")
raw_c = pr_price.text
print('-----> Successfully retrieved the price from Elgiganten  \n')

# Final Display
print('#-----------------------------------------------------------------------#')
print('Prices for [{}] on all websites, Prices are in SEK \n')
print("Price available at Webhallen is: " + raw_a)
print('Price available at MediaMarkt is: ' + raw_b)
print('Price available at Elgiganten is: ' + raw_c)
