import glob
import os
import csv
import json

# Specify the data directory
data_directory = './data/'

combined_data = []


def process_json_files(data_directory):
    json_files = glob.glob(os.path.join(data_directory, '**/*.json'), recursive=True)
    
    for json_file_path in json_files:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Extract the specific nested part
        geolocation = data.get('geolocation', {})
        geolocation_type = geolocation.get('type', '')
        coordinates = geolocation.get('coordinates', [])

        # Flatten the geolocation data
        flattened_geolocation = {
            'geolocation_type': geolocation_type,
            'longitude': coordinates[0],
            'latitude': coordinates[1]
        }

        data.pop('geolocation', None) # Delete the nested geolocation from the original json

        # Add the flattened data to the original JSON
        data.update(flattened_geolocation)

        combined_data.append(data)  # Append the updated data to the list

        # Write the updated data back to the JSON file
        with open(json_file_path, 'w') as updated_json_file:
            json.dump(data, updated_json_file, indent=0)

        print(f"Processed {os.path.basename(json_file_path)} by adding flattened data")

    # Save the combined data to a single JSON file
    with open('combined_data.json', 'w') as combined_file:
        print('Downloading appended json file..')
        json.dump(combined_data, combined_file, indent=0)

    # Save the combined single JSON file to a single CSV file
    with open('combined_data.csv', 'w', newline='') as csv_file:
        print('Downloading converted csv file..')
        csv_writer = csv.DictWriter(csv_file, fieldnames=combined_data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(combined_data)

    

process_json_files(data_directory)
