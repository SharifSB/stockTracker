from bs4 import BeautifulSoup
import requests
import json
import re
from .smartDict import smartDict

def analyzeStatements(companyName, companyURL):

    rawFiling = requests.get(BASEURL).text
    soup = BeautifulSoup(rawFiling, "lxml")
    arr = []
    rawText = soup.findAll(text=True)

    for elem in blah:
        target = smartDict(elem, companyName)
        if (target):
            arr.append(elem)        

    return str(arr)
        