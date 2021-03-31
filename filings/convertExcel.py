import pandas as pd
import numpy as np
import requests
import json
from .getFilings import getFilings

TESTURL = "https://www.sec.gov/Archives/edgar/data/101295/000117184321001963/Financial_Report.xlsx"

def convertExcel():
    xls = pd.read_excel(TESTURL, sheet_name=None)   
    return str(xls)
