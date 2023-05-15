import csv
import json
import requests
from bs4 import BeautifulSoup
import os

# Send a GET request to the URL and parse the HTML content with BeautifulSoup
url = 'https://www.autotrader.com/cars-for-sale/all-cars/riverview-fl?searchRadius=50&zip=33568&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

first_row = True

# Extract the JSON-LD script containing the vehicle information
for json_script in soup.find_all('script', type='application/ld+json'):
    vehicle_data = json.loads(json_script.text)

    print(vehicle_data)

    if 'productionDate' not in vehicle_data or 'manufacturer' not in vehicle_data or 'name' not in vehicle_data or 'model' not in vehicle_data or 'mileageFromOdometer' not in vehicle_data or 'value' not in vehicle_data or 'offers' not in vehicle_data or 'price' not in vehicle_data or 'itemCondition' not in vehicle_data or 'bodyType' not in vehicle_data:
        continue

    print(vehicle_data)

    # Extract the desired attributes from the vehicle_data dictionary
    year = vehicle_data['productionDate']
    make = vehicle_data['manufacturer']['name']
    model = vehicle_data['model']
    mileage = vehicle_data['mileageFromOdometer']['value']
    price = vehicle_data['offers']['price']
    condition = vehicle_data['offers']['itemCondition'].split('/')[-1]
    body_type = vehicle_data['bodyType'][0]
    drive_wheel = vehicle_data['driveWheelConfiguration']
    engine = vehicle_data['vehicleEngine']
    transmission = vehicle_data['vehicleTransmission']
    fuel_type = vehicle_data['fuelType']
    fuel_efficiency = vehicle_data['fuelEfficiency']
    exterior_color = vehicle_data['color']
    interior_color = vehicle_data['vehicleInteriorColor']
    

    # Write the data to a CSV file
    with open('vehicle_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if first_row:
                writer.writerow(['Year', 'Make', 'Model', 'Mileage', 'Price', 'Condition', 'Body Type', 'Drive Wheel',
                                 'Engine', 'Transmission', 'Fuel Type', 'Fuel Efficiency', 'Exterior Color', 'Interior Color'])
                first_row = False
            writer.writerow([year, make, model, mileage, price, condition, body_type, drive_wheel,
                             engine, transmission, fuel_type, fuel_efficiency, exterior_color, interior_color])
    

with open('vehicle_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
print(os.getcwd)