from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

with open('smartprix.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all('div', class_='sm-product has-tag has-features has-actions')

data = []

for item in products:
    # Mobile Name
    name_tag = item.find('h2')
    name = name_tag.text.strip() if name_tag else np.nan

    # Price
    price_tag = item.find('span', class_='price')
    price = price_tag.text.strip() if price_tag else np.nan

    # Spec Score
    score_div = item.find('div', class_='score')
    score_b = score_div.find('b') if score_div else None
    score = score_b.text.strip() if score_b else np.nan

    data.append({'Mobile Name': name, 'Price': price, 'Spec Score': score})

# Create DataFrame
df = pd.DataFrame(data)
df.to_csv('smartprix_mobiles.csv', index=False)

d = pd.read_csv('smartprix_mobiles.csv')
print(d.head())


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

with open('smartprix.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
products = soup.find_all('div', class_='sm-product has-tag has-features has-actions')

data = []

for item in products:
    # Name
    name_tag = item.find('h2')
    name = name_tag.text.strip() if name_tag else np.nan

    # Price
    price_tag = item.find('span', class_='price')
    price = price_tag.text.strip() if price_tag else np.nan

    # Spec Score
    score_div = item.find('div', class_='score')
    score_b = score_div.find('b') if score_div else None
    score = score_b.text.strip() if score_b else np.nan

    # Specs list
    specs_list = item.find('ul', class_='sm-feat specs')
    specs = specs_list.find_all('li') if specs_list else []

    # Extracted specs 
    network = specs[0].text.strip() if len(specs) > 0 else np.nan
    processor = specs[1].text.strip() if len(specs) > 1 else np.nan
    ram_storage = specs[2].text.strip() if len(specs) > 2 else np.nan
    battery = specs[3].text.strip() if len(specs) > 3 else np.nan
    display = specs[4].text.strip() if len(specs) > 4 else np.nan
    rear_camera = specs[5].text.strip() if len(specs) > 5 else np.nan

    # Some phones have memory card or OS info in 6th or 7th <li>
    extra1 = specs[6].text.strip() if len(specs) > 6 else np.nan
    extra2 = specs[7].text.strip() if len(specs) > 7 else np.nan

    # extract front camera, OS, memory card info from extra fields 
    # Often, rear_camera contains "&" and the last part is "Front Camera"
    
    front_camera = np.nan
    os = np.nan
    memory_card = np.nan

    for li in specs:
        txt = li.text.strip()
        if "Front Camera" in txt:
            parts = txt.split("&")
            if len(parts) > 1:
                front_camera = parts[-1].strip()
        if "Android" in txt or "v" in txt:
            os = txt
        if "Memory Card" in txt or "No FM Radio" in txt:
            memory_card = txt

    data.append({
        'Mobile Name': name,
        'Price': price,
        'Spec Score': score,
        'Network': network,
        'Processor': processor,
        'RAM & Storage': ram_storage,
        'Battery': battery,
        'Display': display,
        'Rear Camera': rear_camera,
        'Front Camera': front_camera,
        'OS': os,
        'Memory Card': memory_card
    })

df = pd.DataFrame(data)
df.to_csv('smartprix_mobiles_with_specs.csv', index=False)

# Display first 5 rows
print(df.head())
