import requests
from bs4 import BeautifulSoup
from plyer import notification
import schedule
import time
from datetime import datetime

LEETCODE_USERNAME = "your_username"

def check_streak():