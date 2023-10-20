import boto3
import gzip
import time
import io


def download_and_read_in_memory(bucket_name, file_key):
    s3 = boto3.client('s3')

    try:
        # Download the gzipped file directly into memory
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        gzipped_data = response['Body'].read()

        # Extract the gzipped data
        with gzip.GzipFile(fileobj=io.BytesIO(gzipped_data)) as gz_file:
            # Read the extracted data into a variable
            extracted_data = gz_file.read().decode('utf-8')

        # Now you can work with the extracted data
        print(extracted_data)
    except Exception as e:
        print(f'Error: {e}')


# def extract_gz(local_file_path, output):
#     with gzip.open(local_file_path, 'rb') as gz_file, open(output, 'wb') as out_file:
#         print(f'extracting {local_file_path}..')
#         data = gz_file.read()
#         out_file.write(data)


def read_file():
    with open('output.txt', 'r') as file:
        first_line = file.readline().strip()
        print('Reading the first line of the file....')
        print('Downloading the next file..')
        return first_line  # Return the first line for future use


if __name__ == '__main__':

    bucket_name = 'commoncrawl'
    file_key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'
    local_file_path = 'wet.paths.gz'
    output = 'output.txt'

    download_and_read_in_memory(bucket_name, file_key)
    # extract_gz(local_file_path, output)
    # first_line = read_file()  # Get the first line

    #print('Sleeping before making another request to the s3')

    # # Split the local_file_path and get the last part as the new local_file_path
    # local_file_path = local_file_path.split('/')[-1]
    # download_and_read_in_memory(bucket_name, file_key)
    # output = 'output2.txt'
    # extract_gz(local_file_path, output)

