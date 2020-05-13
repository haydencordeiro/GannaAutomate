import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.maximize_window()
vars = {}
driver.get("https://gaana.com/playlist/gaana-dj-gaana-international-top-50")

driver.find_element(By.ID, "p-list-play_all").click()
a=driver.find_elements_by_xpath('//div[@class="playlist_thumb_det"]')
output=''
for j,i in enumerate(a):
	songname=(i.text)
	link=driver.find_element_by_partial_link_text(songname[:len(songname)//2])
	link=(link.get_attribute('href'))
	output+=str(j+1)+'\t'+songname+'\t'+link+'\n'

with open("output.txt",'w') as f:
   f.write(output)




