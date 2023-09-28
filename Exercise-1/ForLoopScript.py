import os
import requests
import zipfile
import time
from tqdm import tqdm



urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
]


def download_files(urls: list) -> None:

    download_folder = '.\Download'
    os.makedirs(download_folder, exist_ok=True)
    
    start_time = time.perf_counter()

    for url in tqdm(urls, ncols=100, desc='Downloading...'):

        try:
            file_name = url.split('/')[-1]
            local_file_path = os.path.join(download_folder, file_name)

            # Checking if file already exits before
            if os.path.exists(local_file_path):
                print('\n File already exists...')
            
            else:
                r = requests.get(url)

                # Download Content
                if r.status_code == 200:
                    with open(local_file_path, 'wb') as file:
                        file.write(r.content) 
                
                    print('\n Downloaded' , file_name)

                else:
                    print(f'\n failed with error {r.status_code}')
            
            # Extract the Zipfile
            with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
                for file in zip_ref.infolist():
                    if file.filename.endswith('.csv'):
                        zip_ref.extract(file, './Download')
            
            os.remove(local_file_path) # Delete the Zip file
            print('Extracting the Zip File...')
            print('Deleting the Zip File...')
        
        except Exception as e:
            print(f'\n Error: {e}')

    end_time = time.perf_counter()
    time_taken = end_time - start_time

    minutes, seconds = divmod(time_taken, 60)
    print(f"Elapsed time: {int(minutes)} minutes {seconds: .2f} seconds")

if __name__ == "__main__":
    download_files(urls)
