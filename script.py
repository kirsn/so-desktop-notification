from sys import argv
import requests
from bs4 import BeautifulSoup
import pynotify
#import notify2
from time import sleep

def send_message(title, message):
    #notfiy2.init("Init")
    pynotify.init("Init")
    #notice = notify2.Notification(title, message)
    notice = pynotify.Notification(title, message)
    notice.show()
    return

url = "http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % argv[1]
while True:
    r = requests.get(url)
    while r.status_code is not 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("link")
    question = data[2].get('href')
    question = question[question.find('questions') + 19:]
    send_message("Question: ", question)
    sleep(60)
