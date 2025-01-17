import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import os

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.clipboard": 1  # Allow clipboard access
})
#chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-popup-blocking')  # Disable pop-up blocking


driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1280, 800)

# Step 3: Open a website
url = 'https://www.nmrdb.org/13c/index.shtml?v=v2.138.0'
driver.get(url)  # Replace with the desired URL

time.sleep(3)

actions = ActionChains(driver)


try:
    privacy = driver.find_element(By.ID, 'ui-id-2')  # Example element by ID
    agree_group = driver.find_element(By.CLASS_NAME, 'ui-dialog-buttonset')
    child_elements = agree_group.find_elements(By.TAG_NAME, 'button')
    for child in child_elements:
        if child.text == 'I agree':
            actions.move_to_element(child).click().perform()
            break
    time.sleep(3)
    print('Privacy agreeded')
except:
    print('No privacy window')


def extract_data(mol):
    
    pyperclip.copy(mol)  # Copies the text to the clipboard

    # paste into interface
    left_div = driver.find_element(By.ID, 'module-14')
    tool_box = left_div.find_elements(By.CLASS_NAME, 'ci-module-header-toolbar')[0]
    li = tool_box.find_elements(By.TAG_NAME, 'li')
    actions.click(li[2]).perform()

    time.sleep(3)
            
    predict = driver.find_element(By.ID, 'button-4')  
    actions.click(predict).perform() 

    time.sleep(3)

    results = driver.find_element(By.ID, 'module-9')
    actions.context_click(results).perform() 

    time.sleep(3)

    context_menu = driver.find_element(By.CLASS_NAME, 'ci-contextmenu') 
    
    items = context_menu.find_elements(By.TAG_NAME, 'li')
    item = items[4]
    actions.click(item).perform() 

    time.sleep(3)

    export_module = driver.find_element(By.CLASS_NAME, 'ci-module-export')
    text = export_module.find_element(By.TAG_NAME, 'textarea').text
    
    return text



def decode_text(text):
    rows = text.split('\n')
    del rows[0]
    
    res = []
    
    for row in rows:
        r = row.split(' ')
        del r[0]
        
        res.append(r)
        
    return res



# Specify the path to your Excel file
#file_path = 'input/test_smiles.csv'
file_path = 'input/pubchem_D1.csv'

# Load the Excel file into a DataFrame
df = pd.read_csv(file_path)
    
# Iterate through each row using `iterrows()`
for index, row in df.iterrows():
    
    id = int(row['CID'])
    value = row['SMILES']
    print(f"{value}")

    if os.path.exists('output/'+str(id)+'.txt'):
        print('file already exists')
        continue

    res = extract_data(value)
    # save single file
    with open('output/'+str(id)+'.txt', 'w') as file:
        file.write(res)
    print(decode_text(res))
    time.sleep(3)
    driver.refresh()
    time.sleep(3)


driver.quit()