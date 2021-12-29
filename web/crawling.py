import sys
import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from tqdm import tqdm_notebook
import warnings ; warnings.filterwarnings(action='ignore')
import requests

URL = 'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010008'
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)


headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
url_list=[url.get_attribute('href') for url in driver.find_elements_by_css_selector(".prd_info>a")]
