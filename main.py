
import requests  
r = requests.get('https://paytmmall.com/laptops-glpid-6453?channel=web&site_id=1&version=2&use_mw=1&page=1&notebook_type=Convertible&sort_price=0&discoverability=online&src=store')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')  
results = soup.find_all('div', attrs={'class':'_3WhJ'})

records = []  
for result in results: 
    try:
        product = result.find('a')['title']
        image_url = result.find('img')['src']
        current_price = result.find('span').text
    
        original_price = result.select('.dQm2')[0].text[:-4]
    
        discount = result.select('.c-ax')[0].text
    except:
        discount = 0.5
    records.append((product, image_url, current_price, original_price, discount))

import pandas as pd  
df = pd.DataFrame(records, columns=['Product', 'Image Url', 'Current Price', 'Original Price', 'discount'])  

df.to_csv('paytm_d.csv', index=False, encoding='utf-8') 

