import csv
import requests

API_KEY = input("Enter your IPinfo API key: ") or None

if not API_KEY:
    print("No API key entered. Exiting...")
    exit()

with open('ip_addresses.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Create a new CSV file to write the IP info to
    with open('ip_info.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write headers for the new CSV file
        writer.writerow(['IP Address', 'Country', 'Region', 'Type', 'Postal', 'Location'])

        # Iterate over the rows in the CSV file
        for row in reader:
            # Get the IP address from the row
            ip_address = row[0]

            # Get the IP info
            url = f'https://ipinfo.io/{ip_address}/json?token={API_KEY}'
            response = requests.get(url)
            data = response.json()

            # Extract the desired data from the response
            country = data.get('country', '')
            region = data.get('region', '')
            org = data.get('org', '')
            postal = data.get('postal', '')
            loc = data.get('loc', '')
           # loc = data.get('timezone', '')

            # Write the IP info to the new CSV file
            writer.writerow([ip_address, country, region, org, postal, loc])

            # Print the IP info to the console
            print(f'IP Address: {ip_address}')
            print(f'Country: {country}')
            print(f'Region: {region}')
           # print(f'region: {city}')
            print(f'Type: {org}')
            print(f'Postal: {postal}')
            print(f'Location: {loc}')
           # print(f'loc: {timezone}')
            print()
