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
        r = requests.get("http://192.168.10.101/zipper/")
        if (r.status_code == 200):
            print("\n Successful " + str(r))
        else:
            print("Unsuccessful! Error code: " + str(r.status_code))
        r.close()
        header = prog.h
# Test For the Website and the links / URL
class TestGotJPG(unittest.TestCase):
    def test_jpg(self):
        with urllib.request.urlopen("http://192.168.10.101/zipper/") as response:
            html = response.read()
        Image = BeautifulSoup(html, "lxml")
        # Retrieving  arguments
        for link in Image.find_all('a'):
            print(link.get('href'))


if __name__ == '__main__':
    unittest.main()