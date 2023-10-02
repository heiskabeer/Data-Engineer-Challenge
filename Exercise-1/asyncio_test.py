import os
import aiohttp
import asyncio
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


download_folder = '.\Download'
os.makedirs(download_folder, exist_ok=True)   

async def download_files(session, url, download_folder):

    try:
        file_name = url.split('/')[-1]
        local_file_path = os.path.join(download_folder, file_name)

        # Checking if file already exits before
        if os.path.exists(local_file_path):
            print('\n File already exists...')
        
        else:
            
            async with session.get(url) as r:

            # Download Content
                    if r.status == 200:
                        with open(local_file_path, 'wb') as file:
                            chunk = await r.content.read()
                            file.write(chunk) 
                    
                        print('\n Downloaded' , file_name)

                    else:
                        print(f'\n failed with error {r.status}')
        
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


async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_files(session, urls, download_folder))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results # can be rewritten to a simple loop comprehension to map the task and download_files function for url in urls


async def main(urls):
    
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls, download_folder)
        return data



if __name__ == "__main__":
    asyncio.run(main(urls))
