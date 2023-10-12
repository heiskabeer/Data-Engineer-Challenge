import requests
import time
from bs4 import BeautifulSoup
import pandas as pd


def scrape():

    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    response = requests.get(url)
    timestamp_to_find = "2022-02-07 14:03"

    if response.status_code == 200:
        print('Now Scraping')
        soup = BeautifulSoup(response.content, "html.parser")
        tr_tags = soup.find_all('tr')

        last_href_text = None

        for tr_tag in tr_tags:
            a_tag = tr_tag.find('a', href=True)
            date_time = tr_tag.find_all('td', align='right')

            if a_tag and date_time:
                date_time_text = date_time[0].get_text(strip=True)

                if date_time_text == timestamp_to_find:
                    last_href_text = a_tag.get('href')

        if last_href_text:
            print(f"Last Modified File: {last_href_text} \n ")
            download_file(last_href_text)  # Pass the file name to download_file function

    else:
        print(f"Connection Failed. Status Code: {response.status_code}")



def download_file(file_name):
    
    # Build the URL to download the last_modified file
    url = f'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/{file_name}'

    response = requests.get(url)

    if response.status_code == 200:
        print(f'Now Downloading {file_name}')

        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f'Completed Downloading {file_name} \n')

    else:
        print(f"Connection Failed. Status Code: {response.status_code}")



def transform():
    print('Filtering Begins')

    df = pd.read_csv('A0002453848.csv', low_memory=False)
    
    # Finding the highest temperature
    df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'], errors='coerce')
    highest_temp = df['HourlyDryBulbTemperature'].max()

    # Filtering the entire DataFrame with the highest temperature
    highest_temp_records = df[df['HourlyDryBulbTemperature'] == highest_temp]

    print('Filtering Completed, Below is the Data \n')
    print(highest_temp_records)



if __name__ == '__main__':
    
    start_time = time.time()  

    scrape()
    transform()

    end_time = time.time() 

    elapsed_time = end_time - start_time
    print(f'Total execution time: {elapsed_time:.2f} seconds')