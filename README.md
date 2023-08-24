
# OpenSeatsNotifier

A Course Seat Availability Monitor

Originally created for notifying the author about available seats for the 5xx courses offered at ASU.

## Authors

- [@nikitametha](https://nikitametha.com) :)




## Features

- Checks for non reserved available seats at the ASU class search website.
- Originally created for CSE 5xx courses but can be used for any stream!
- Notifies user via email if any courses are available.




## Installation
1) Clone the project 
2) Install requirements

```bash
  pip install -r requirements.txt
```

2) Install latest Chromedriver here:
https://chromedriver.chromium.org/downloads
    
## Usage
In the folder ```OpenSeatsNotifier```
- Make sure you have chrome driver installed in the same folder.
- Change the link at ```driver.get("<link>")``` to the class search link of your stream. (The default is grad CSE courses.)
- <TODO - Add your email at ..>

To run the script
```bash
  python open_seats.py
```

## Roadmap

- Add ability for user to:
    - Choose the exact courses that they want to be notified on.
    - Specify the stream/discipline and level of course (grad, undergrad..)
- Containerize application to deploy script onto multiple systems with ease
- Configure cron jobs in containers for script to run every few minutes - make it as real time as possible.


## Tech Stack

Python, BeautifulSoup4, Selenium, ChromeDriver

