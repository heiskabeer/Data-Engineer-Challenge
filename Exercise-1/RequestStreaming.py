import os
import time
import zipfile
import requests
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




def download_files(url):

    try:

        download_folder = '.\Downloads'
        os.makedirs(download_folder, exist_ok=True)
            
        start_time = time.perf_counter()

        for url in urls:

            file_name = url.split('/')[-1]
            local_file_path = os.path.join(download_folder, file_name)


            # Get the total file size from the Content-Length header
            total_size = int(requests.head(url).headers.get('Content-Length', 0))


            # Check if file  already exists in order to resume download
            if os.path.exists(local_file_path):
                print('\n File already exists...')
                file_size = os.path.getsize(local_file_path) 
                # Getting the size of the already downloaded file to resume downloading from there

                
                # Specify the Range header to resume the download from where it left off
                headers = {'Range': f'bytes={file_size}-'}

                print("Resuming download...")

                # Open the file in append mode, and write the file 
                with open(local_file_path, mode="ab") as file:
                    with requests.get(url, headers=headers, stream=True) as response:
                        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", ncols=100) as pbar:
                            for chunk in response.iter_content(chunk_size=10 * 1024):
                                file.write(chunk)
                                pbar.update(len(chunk))
                
                with zipfile.ZipFile(local_file_path, 'r') as zip_ref: # Extract the zipfile
                    for file in zip_ref.infolist():
                        if file.filename.endswith('.csv'):
                            zip_ref.extract(file, './Downloads')

                os.remove(local_file_path) # Delete the Zip file
                print('Extracting the Zip File...')
                print('Deleting the Zip File...')
                            

            else:
                print('Starting a new download...')
                # If file doesn't exist, start a new download.
                with requests.get(url, stream=True) as response:
                    with open(local_file_path, mode="wb") as file:
                        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", ncols=100) as pbar:
                            for chunk in response.iter_content(chunk_size=10 * 1024):
                                file.write(chunk)
                                pbar.update(len(chunk))
                
                with zipfile.ZipFile(local_file_path, 'r') as zip_ref: # Extract the zipfile
                    for file in zip_ref.infolist():
                        if file.filename.endswith('.csv'):
                            zip_ref.extract(file, './Downloads')

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
