from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getFilings import getFilings
from .analyzeStatements import analyzeStatements
from .convertExcel import convertExcel
from . import connectDB
from .returnFilingsFromDB import returnFilingsFromDB

connection = connectDB.returnConnection()
cursor = connection.cursor()
# Create your views here.



def updateStatements(request):
    statements = analyzeStatements()
    response = JsonResponse(statements, safe=False)
    return response

def sendTest(request):
    excel = convertExcel()
    response = JsonResponse(excel, safe=False)

def getDatabaseFilings(request):
    filings = returnFilingsFromDB(cursor)
    print(filings)
    response = JsonResponse(filings, safe=False)
    return response