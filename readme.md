# IP Tool

This tool allows you to geolocate IP addresses and store the results in a CSV file. It uses the [ipinfo.io](https://ipinfo.io) API to retrieve the geolocation data.

## Usage

1. Create a CSV file called `ip_addresses.csv` and populate it with the IP addresses you want to get information on.
2. Run the script `iptool.py` and provide your ipinfo.io API key when prompted. If you don't have an API key, you can sign up for a free one on the [ipinfo.io](https://ipinfo.io/signup) website.
3. The script will create a new CSV file called `ip_info.csv` and store the information for each IP address in this file.

## Functionality

The `iptool.py` script performs the following steps:

1. Reads the IP addresses from the `ip_addresses.csv` file.
2. Uses the ipinfo.io API to retrieve the geolocation data for each IP address.
3. Stores the data in a new CSV file called `ip_info.csv`.

## Documentation

The `iptool.py` script requires the following dependencies:

- Python 3.x
- requests library (`pip install requests`)

To use the `iptool.py` script, follow these steps:

1. Clone the repository to your local machine.
2. Install the dependency by running `pip install requests` in the project directory.
3. Create a CSV file called `ip_addresses.csv` and populate it with the IP addresses you want to get information on.
4. Run the script 'iptool.py` by running `python iptool.py` in the project directory.
5. When prompted, enter your ipinfo.io API key. If you don't have an API key, you can sign up for a free one on the [ipinfo.io](https://ipinfo.io/signup) website.
6. The script will create a new CSV file called `ip_info.csv` and store the geolocation data for each IP address in this file.

I am not responsible for actions which lead to legal troubles. This is for educational and informational, law abiding use only.