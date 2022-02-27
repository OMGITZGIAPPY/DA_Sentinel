# Unit Test Case
import unittest
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import RequestnHeader as prog

# Test For Status & For Header
class TestStatus(unittest.TestCase):
    def test_Status(self):
        # Website URL
        r = requests.get("http://192.168.10.101/zipper/") # The URL where the request will be getting from
        # Print Message when successful or Unsuccessful
        if (r.status_code == 200):
            print("\nSuccessful " + str(r)) # Output Successful + print code number
        else:
            print("Unsuccessful! Error code: " + str(r.status_code)) # Output Unsuccessful + print error code number
        header = prog.h # Shows the header
        print("\n******")
# Test For the Website and the links / URL
class TestGotJPG(unittest.TestCase):
    print("\n*****")
    def test_jpg(self):
        # So i can request and access the website
        with urllib.request.urlopen("http://192.168.10.101/zipper/") as response:
            html = response.read()
        Image = BeautifulSoup(html, "lxml") # Parsing the Url as lxml
        # Retrieving Links arguments Only
        for link in Image.find_all('a'): # All the Links
            print(link.get('href')) #Printing out all the link collected

# To run Unittest
if __name__ == '__main__':
    print("\n*****")
    unittest.main()