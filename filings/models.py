from django.db import models
from datetime import datetime
from django import utils


class Company(models.Model):
    name = models.CharField(max_length=250)
    latestFilingType = models.CharField(max_length=10)
    businessDescription = models.CharField(max_length=100000)
    lastFilingDate = models.DateField()
    lastFilingPeriod = models.CharField(max_length=20)


class Filing(models.Model):
    companyName = models.CharField(max_length=250, default="company")
    publishDate = models.CharField(max_length=200, default="today")
    cikNumber = models.CharField(max_length=1000, default="number")
    formType = models.CharField(max_length=10, default="type")
    filingPeriod = models.CharField(max_length=20, default="period")
    filingURL = models.CharField(max_length=1000, default="url")
    excelURL = models.CharField(max_length=1000, default="excel")
    timeCollected = models.TimeField(default=utils.timezone.now)




# class Industry(models.Model):
#     averageStockPrice = models.FloatField()
#     industryPremium = models.FloatField()
#     riskFactors = models.CharField(max_length=10000)
#     positiveCatalysts = models.JSONField()
#     negativeCatalysts = models.JSONField()

# class Economy(models.Model):
#     discountRate = models.FloatField()
#     GDPGrowth = models.FloatField()
#     NewTradeRegulations = models.CharField(max_length=10000)
#     TreasuryYield = models.FloatField()

# class Catalyst(models.Model):
#     eventType = models.CharField(max_length=1000)
#     severityIndex = models.FloatField()
#     industriesAffected = models.JSONField()
#     companyAffected = models.CharField(max_length=1000)
#     dataSource = models.CharField(max_length=1000)

# class Executive(models.Model):
#     name = models.CharField(max_length=500)
#     favorabilityRating = models.FloatField()
#     InfluenceRating = models.FloatField()
#     yearsAsExecutive = models.IntegerField()
#     newComapny = models.BooleanField()
#     isCatalyst = models.BooleanField()