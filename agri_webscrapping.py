import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
dfs = pd.read_html('http://www.agritech.tnau.ac.in/input_source/input_source_tnau_seed_new_rice.html')
for df in dfs:
    print(df)
df.to_csv('agri-data.csv', index=False)    

