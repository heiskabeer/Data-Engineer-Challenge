import boto3
import gzip
import time
from botocore.exceptions import ClientError


def download_file(bucket_name, file_key, local_file_path, max_retries=5):

    s3 = boto3.resource('s3')
    retries = 0

    while retries < max_retries:
        try:
            s3.Bucket(bucket_name).download_file(file_key, local_file_path)
            print(f'{file_key} has been successfully downloaded')
            break

        except ClientError as e:
                if 'SlowDown' in str(e):
                    # Implement a backoff strategy
                    wait_time = (2 ** retries)
                    print(f'Rate limited, waiting for {wait_time} seconds before retrying...')
                    time.sleep(wait_time)
                    retries += 1
                else:
                    print(f'Error: {e}')
                    break
        
    

def extract_gz(local_file_path, output):
    with gzip.open(local_file_path, 'rb') as gz_file, open(output, 'wb') as out_file:
        print(f'extracting {local_file_path}..')
        data = gz_file.read()
        out_file.write(data)


def read_file():
    with open('output.txt', 'r') as file:
        first_line = file.readline().strip()
        print('Reading the first line of the file..')
        print('Downloading the next file..')
        return first_line  # Return the first line for future use


if __name__ == '__main__':

    bucket_name = 'commoncrawl'
    file_key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'
    local_file_path = 'wet.paths.gz'
    output = 'output.txt'

    download_file(bucket_name, file_key, local_file_path)
    extract_gz(local_file_path, output)
    first_line = read_file()  # Get the first line

    # Split the local_file_path and get the last part as the new local_file_path
    local_file_path = first_line.split('/')[-1]
    download_file(bucket_name, first_line, local_file_path)
    output = 'output2.txt'
    extract_gz(local_file_path, output)








