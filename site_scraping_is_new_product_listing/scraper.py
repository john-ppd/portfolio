from bs4 import BeautifulSoup  # Importing BeautifulSoup for web scraping
from requests import get  # Importing 'get' method from requests for making HTTP requests
import re  # Importing 're' for regular expressions
import time  # Importing 'time' for time-related operations
import random  # Importing 'random' for generating random numbers
import tweepy  # Importing 'tweepy' for Twitter API handling

tweetpy_auth_code = ('', '')  # Tuple to store Twitter authentication codes
access_token_code = ('', '')  # Tuple to store access token for Twitter API
message_to_user_id = 777777777  # User ID to whom messages will be sent (replace with the actual user ID)

url = [
    'https://www.mint.ca/store/buy/new-releases_coins-cat410002',  # List of URLs to scrape
    'https://www.boringcompany.com/'
]

# Initializing various lists and variables for data storage and comparison
list1 = []  # Placeholder list for scraped data
list_start = []  # List to store start indices of specific words
list_end = []  # List to store end indices of specific words
final_list = []  # List to store extracted data from 'list1'
final_list_boring = []  # List to store specific extracted data from 'list1'
startup_final_list = []  # Placeholder for the initial state of 'final_list'
list_difference = []  # List to store the difference between 'final_list' and 'startup_final_list'
first_run = True  # Variable to track if it's the first run
times_run = 0  # Variable to track the number of times the code runs

# Function to send a direct message on Twitter using Tweepy
def tweet_it(message):
    global startup_final_list
    auth = tweepy.OAuthHandler(tweetpy_auth_code[0], tweetpy_auth_code[1])
    auth.set_access_token(access_token_code[0], access_token_code[1])
    api = tweepy.API(auth)
    api.send_direct_message(message_to_user_id, message)
    startup_final_list = final_list.copy()

# Functions to find indices of specific words within a string and append their positions to lists
def find_all_index_start(list_index, find_word):
    sentence = str(list1[list_index])
    word = str(find_word)
    for match in re.finditer(word, sentence):
        list_start.append(int(match.end()))  # Gets end coordinate of 'find_word'

def find_all_index_end(list_index, find_word):
    sentence = str(list1[list_index])
    word = str(find_word)
    for match in re.finditer(word, sentence):
        list_end.append(int(match.end()))

# Function to extract substrings from 'list1' based on indices obtained earlier and store them in 'final_list'
def scan_through_ranges(list_index):
    for i in range(int(len(list_start))):
        search_string = str(list1[list_index])
        if list_index == 0:
            final_list.append(search_string[list_start[i] + 1:list_end[i] - 7:1])
        elif list_index == 1:
            final_list_boring.append(search_string[list_start[i]:list_end[i] - 4:1])
            final_list.append(search_string[list_start[i]:list_end[i] - 4:1])

# Function to assign the initial list and send a live notification tweet if it's the first run
def assign_starting_list():
    global first_run
    global startup_final_list
    if first_run:
        tweet_it("We are live :)")  # Sending a tweet to indicate the code is live
        startup_final_list = final_list.copy()  # Copying 'final_list' to 'startup_final_list'
        first_run = False  # Updating the 'first_run' flag to False indicating subsequent runs


def run():
    # Iterate through the URLs in the 'url' list
    for i in range(len(url)):
        # Retrieve the web page content using the 'get' method
        page = get(url[i])
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page.text, 'lxml')

        # Check for specific conditions based on the index 'i'
        if i == 0:  # For the first URL
            # Extract elements with the class "imgResult" and add them to 'list1'
            list1.append(soup.findAll(class_="imgResult"))
            # Find indices of specific words and store them in 'list_start' and 'list_end'
            find_all_index_start(i, 'title')
            find_all_index_end(i, ' width=')
            # Scan through ranges and extract substrings based on indices
            scan_through_ranges(i)
        elif i == 1:  # For the second URL
            # Clear 'list_start' and 'list_end'
            list_start.clear()
            list_end.clear()
            # Extract anchor tags ("a" elements) and add them to 'list1'
            list1.append(soup.findAll("a"))
            # Find indices of specific words in the new 'list1'
            find_all_index_start(i, '<a href=\"/')
            find_all_index_end(i, '</a>')
            # Clean up discrepancies in indices and scan through ranges
            for j in range(int(len(list_start))):
                if list_start[j] > list_end[j]:
                    list_end.pop(j)
            scan_through_ranges(i)
            # Assign the initial list if it's the first run
            assign_starting_list()


def clear_and_compare_lists():
    # Global variables for comparison and tracking
    global first_run
    global list_difference
    # Calculate the lengths of 'startup_final_list' and 'final_list'
    starting_list_length = int(len(startup_final_list))
    new_list_length = int(len(final_list))
    print(starting_list_length)
    print(new_list_length)

    # Compare lengths to identify differences
    if starting_list_length < new_list_length:
        # Append differences to 'list_difference' for further action
        list_difference.append(str([item for item in final_list if item not in startup_final_list]))
        print(list_difference[:])
        # Check and send notifications for new items
        if len(list_difference) > 0:
            if len(list_difference[0]) > 2:
                print("new item2! sending notification")
                tweet_it(str(list_difference[:]))

                # Send email

                # Set start list = final_list.copy()


    elif starting_list_length > new_list_length:
        # Identify differences in the opposite direction
        list_difference.append(str([item for item in startup_final_list if item not in final_list]))

        print(list_difference[:])
        print("startup > final")
        if len(list_difference) > 0:
            if len(list_difference[0]) > 2:
                print("new item3! sending notification")
                tweet_it(str(list_difference[:]))

    else:
        # Check for identical lists and notify if any differences exist
        list_difference.append(str([item for item in final_list if item not in startup_final_list]))
        print(list_difference[:])
        print("startup == final")
        if len(list_difference) > 0:
            print("list length = " + str(len(list_difference[0])))
        if len(list_difference) > 0:
            if len(list_difference[0]) > 2:
                print("new item1! sending notification")
                tweet_it(str(list_difference[:]))

    # Perform list clearing and maintenance if it's not the first run
    if not first_run:
        list1.clear()
        list_start.clear()
        list_end.clear()
        final_list.clear()
        list_difference.append(" ")
        list_difference.clear()


# Continuous loop to execute the defined functions
while True:
    run()  # Execute the 'run' function
    if not first_run:
        clear_and_compare_lists()  # Perform list comparisons and maintenance

    # Display the number of times the loop runs and set a sleep timer
    print("times run = " + str(times_run))
    times_run += 1
    rando = int(random.randint(30, 60))
    print("sleeping for " + str(rando) + " secs")
    time.sleep(rando)  # Sleep for a random duration before continuing the loop

