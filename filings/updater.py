from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .getFilings import getFilings
from . import connectDB

connection = connectDB.returnConnection()
cursor = connection.cursor()
def myFunc():
    return getFilings(cursor)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(myFunc, 'interval', minutes=1)
    scheduler.start()