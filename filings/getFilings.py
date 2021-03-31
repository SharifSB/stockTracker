from bs4 import BeautifulSoup
from .models import Company, Filing
from datetime import datetime
import requests
import json
import re


RSSFEEDURL = "https://www.sec.gov/Archives/edgar/usgaap.rss.xml"

def getFilings(cursor):
    source = requests.get(RSSFEEDURL).text
    soup = BeautifulSoup(source, "lxml")
    count = 0
    myData = soup.findAll('item')
    companies = []
    for elem in myData:    
        formType = elem.find('edgar:formtype').contents
        originalFilingURL = str(elem.find('edgar:xbrlfile'))
        try:
            if (len(formType) > 0 and (formType[0] == "10-K" or formType[0] == "10-Q")):

                obj = {
                "companyName": "companyName",
                "publishDate": "publishDate",
                "cikNumber": "cikNumber",
                "formType": "formType",
                "filingPeriod": "filingPeriod",
                "filingURL": "filingUrl",
                "excelURL": "excelURL",
                "timeCollected": datetime.now()
                }
                arr = [
                { "companyName": elem.find('edgar:companyname').contents }, 
                { "publishDate": elem.find('edgar:filingdate').contents },
                { "cikNumber": elem.find('edgar:ciknumber').contents },
                { "formType": elem.find('edgar:formtype').contents },
                { "filingPeriod": elem.find('edgar:period').contents }]

                for entry in arr:
                    try:
                        myKey = list(entry.keys())[0]
                    except IndexError:
                        continue
                    if (entry[myKey]):
                        value = ""    
                        try:
                            value = entry[myKey][0]
                        except IndexError:
                            continue
                        if (value):
                            obj[myKey] = value 
    
        
                    parsedFile = re.search('(?<=edgar:url=\").*?(?=\")', originalFilingURL)
                    if (parsedFile):
                        try:
                            obj["filingURL"] = parsedFile.group(0)
                            excelURL = re.search('(?:[^/]*/){8}', parsedFile.group(0))
                            obj["excelURL"] = f'{excelURL.group(0)}Financial_Report.xlsx'
                        except IndexError:
                            pass
                try: 
                    filing = Filing.objects.get(companyName=obj.get("companyName"), formType=obj.get("formType"), filingPeriod=obj.get("filingPeriod"))
                except Filing.DoesNotExist:
                    Filing.objects.create(companyName=obj.get("companyName"), publishDate=obj.get("publishDate"), 
                    cikNumber=obj.get("cikNumber"), formType=obj.get("formType"), filingPeriod=obj.get("filingPeriod"), 
                    filingURL=obj.get("filingURL"), excelURL=obj.get("excelURL"), timeCollected=obj.get("timeCollected"))
                    count = count + 1
                companies.append(obj)
        except IndexError:
            continue

    print(f'{count} companies added')
    return companies
       

 

