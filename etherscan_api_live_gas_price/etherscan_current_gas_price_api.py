import requests  # Importing the 'requests' library for making HTTP requests
import time  # Importing the 'time' module for handling time-related operations

api_key = 'put_your_api_key_here'  # Replace 'your_api_key' with your actual Etherscan API key

i = 0  # Initializing a variable 'i' to track iterations
#  will run for 24 hours
secondsInDay = 86400  # Setting the total number of seconds in a day (24 hours)

# Loop to run for 24 hours
while i < secondsInDay:
    time.sleep(1.5)  # Pause the program execution for 1.5 seconds
    # Make a GET request to the Etherscan API for gas price information
    response = requests.get(
        url=f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_key}")

    # Extract gas price values from the JSON response
    slow = response.json()["result"]["SafeGasPrice"]
    med = response.json()["result"]["ProposeGasPrice"]
    fast = response.json()["result"]["FastGasPrice"]

    # Store gas prices in a tuple and print it along with the iteration count 'i'
    gas = (slow, med, fast)
    print(gas, " ", i)
    i += 1  # Increment the iteration count for the while loop
