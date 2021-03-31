import re

def smartDict(rawPhrase, companyName):
    desiredString = ""
    weAreA = re.match(r'We are a .*', rawPhrase, re.IGNORECASE)
    weAreAn = re.match(r'We are an.*', rawPhrase, re.IGNORECASE)
    weAreThe = re.match(r'We are the.*', rawPhrase, re.IGNORECASE)
    weAreThe = re.match(r'We produce.*', rawPhrase, re.IGNORECASE)
    weAreThe = re.match(r'We develop.*', rawPhrase, re.IGNORECASE)
    weAreThe = re.match(r'We provide.*', rawPhrase, re.IGNORECASE)
    fullCompanyName = re.match(rf'{companyName} is.*', rawPhrase, re.IGNORECASE)
    ourComp = re.match(r'Our company produces. *', rawPhrase, re.IGNORECASE)
    ourComp = re.match(r'Our company develops. *', rawPhrase, re.IGNORECASE)
    ourComp = re.match(r'Our company provides. *', rawPhrase, re.IGNORECASE)
    ourGoal = re.match(r'Our goal is. *', rawPhrase, re.IGNORECASE)
    weAreThe = re.match(r'Our product.*', rawPhrase, re.IGNORECASE)
    ourMission = re.match(r'Our Mission. *', rawPhrase, re.IGNORECASE)

    DictIter = [weAreA, weAreAn, weAreThe, weHave, fullCompanyName, ourComp, ourGoal, ourMission]

    for recipe in DictIter:
        if (recipe):
            desiredString = rawPhrase
            break
    return desiredString