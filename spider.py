from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getcontent(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,'html.parser')
        content=bsObj.body
    except AttributeError as e:
        return None
    return content
def getdate(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,'html.parser')
        date=bsObj.findAll("span",{"class":"posted-date"})
    except AttributeError as e:
        return None
    return date
def gettitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,'html.parser')
        title=bsObj.findAll("h2",{"class":"entry-title"})
    except AttributeError as e:
        return None
    return title
def getsummary(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,'html.parser')
        summary=bsObj.findAll("div",{"class":"entry-summary"})
    except AttributeError as e:
        return None
    return summary
def getauthor(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj=BeautifulSoup(html,'html.parser')
        author=bsObj.findAll("span",{"class":"entry-author"})
    except AttributeError as e:
        return None
    return author
content = getcontent("https://blog.snowstar.org/")
author=getauthor("https://blog.snowstar.org/")
date=getdate("https://blog.snowstar.org/")
title=gettitle("https://blog.snowstar.org/")
summary=getsummary("https://blog.snowstar.org/")
if title == None:
    print("title could not be found")
else:
    print(title)
    with open('C:/work/data.txt','a') as f:
        f.write(title)
if author == None:
    print("author could not be found")
else:
    print(author)
    with open('C:/work/data.txt','a') as f:
        f.write(author)
if date == None:
    print("date could not be found")
else:
    print(date)
    with open('C:/work/data.txt','a') as f:
        f.write(date)
if summary == None:
    print("summary could not be found")
else:
    print(summary)
    with open('C:/work/data.txt','a') as f:
        f.write(summary)
