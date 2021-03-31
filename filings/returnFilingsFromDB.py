from .models import Filing

def returnFilingsFromDB(cursor):
    arr = []
    records = Filing.objects.filter()

    for record in records:

        obj = {
            "companyName": record.companyName,
            "publishDate": record.publishDate,
            "cikNumber": record.cikNumber,
            "formType": record.formType,
            "filingPeriod": record.filingPeriod,
            "filingURL": record.filingURL,
            "excelURL": record.excelURL,
            "timeCollected": record.timeCollected
        }

        arr.append(obj)

    return arr