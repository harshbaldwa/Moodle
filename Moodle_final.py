import requests
import os
from bs4 import BeautifulSoup
import pync
from apscheduler.schedulers.blocking import BlockingScheduler

payload = {
    "username": "",
    "password": ""
}

moodlelogin = "https://moodle.iitb.ac.in/login/index.php"

session = requests.Session()
session.post(moodlelogin, data=payload)

def download(link,path):
    r = session.get(link["href"])
    with open(path+link.text+"."+r.url.split(".")[-1], "wb") as pdf:
        pdf.write(r.content)
        pdf.close()

def ae223():
    n = True
    r = session.get("https://moodle.iitb.ac.in/course/resources.php?id=7510")
    html = BeautifulSoup(r.text, "html.parser")

    lastTag = html.findAll('td', {"class": "cell c1"})
    for i in range(1,6):
        if n:
            a = lastTag[-i].find('a')
            if "/" in a.text:
                pass
            elif "Tutorial" in a.text:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE223/Tutorials/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title = "AE223")
                    n=False
                    break
                else:
                    download(a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE223/Tutorials/")
                    pync.notify(a.text+" Downloaded", title="AE223")
            else:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE223/Lectures/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE223")
                    n = False
                    break
                else:
                    download(a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE223/Lectures/")
                    pync.notify(a.text+" Downloaded", title = "AE223")

def ae225():
    n = True
    r = session.get("https://moodle.iitb.ac.in/course/resources.php?id=7511")
    html = BeautifulSoup(r.text, "html.parser")

    lastTag = html.findAll('td', {"class": "cell c1"})
    for i in range(1,6):
        if n:
            a = lastTag[-i].find('a')
            if "Tutorial" in a.text:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Tutorials/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE225")
                    n = False
                    break
                else:
                    download(
                        a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Tutorials/")
                    pync.notify(a.text+" Downloaded", title="AE225")
            elif "Quiz" in a.text: 
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Quiz/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE225")
                    n = False
                    break
                else:
                    download(
                        a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Quiz/")
                    pync.notify(a.text+" Downloaded", title="AE225")
            elif "HW" in a.text:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/HW/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE225")
                    n = False
                    break
                else:
                    download(
                        a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/HW/")
                    pync.notify(a.text+" Downloaded", title="AE225")
            else:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Lectures/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE225")
                    n = False
                    break
                else:
                    download(a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE225/Lectures/")
                    pync.notify(a.text+" Downloaded", title="AE225")

def ae227():
    n = True
    r = session.get("https://moodle.iitb.ac.in/course/resources.php?id=7512")
    html = BeautifulSoup(r.text, "html.parser")

    lastTag = html.findAll('td', {"class": "cell c1"})
    for i in range(1,6):
        if n:
            a = lastTag[-i].find('a')
            if "/" in a.text:
                pass
            elif "HW" in a.text:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE227/HW/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE227")
                    n = False
                    break
                else:
                    download(
                        a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE227/HW/")
                    pync.notify(a.text+" Downloaded", title="AE227")
            else:
                if os.path.isfile("/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE227/Lectures/"+a.text+".pdf"):
                    #pync.notify('Nothing new here', title="AE227")
                    n = False
                    break
                else:
                    download(
                        a, "/Users/vicky/Library/Mobile Documents/com~apple~CloudDocs/Studies/AE227/Lectures/")
                    pync.notify(a.text+" Downloaded", title="AE227")

def ae227hw():
    r = session.get("https://moodle.iitb.ac.in/mod/assign/index.php?id=7512")
    html= BeautifulSoup(r.text, "html.parser")
    lastTag = html.findAll('tr')[-1]
    a = lastTag.find('a')
    b = lastTag.find('td',{"class": "cell c4 lastcol"})
    c = lastTag.find('td',{"class": "cell c3"})
    if b.text != "-":
        if c.text == "Submitted for grading": 
            pync.notify(a.text+" - "+b.text, title = "AE227 Assignment Marks")
    else:
        if c.text != "Submitted for grading":
            pync.notify(a.text+" uploaded", title = "AE227 New Assignment")

ae223()
ae225()
ae227()
ae227hw()
# scheduler = BlockingScheduler()
# scheduler.add_job(ae223, 'interval', hours=1)
# scheduler.start()
