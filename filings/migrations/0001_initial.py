# Generated by Django 3.1.7 on 2021-03-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=1000)),
                ('latestFilingType', models.CharField(max_length=10)),
                ('executives', models.JSONField()),
                ('businessDescription', models.CharField(max_length=100000)),
                ('lastFilingDate', models.DateField()),
                ('lastFilingQuarter', models.CharField(max_length=20)),
                ('nextFilingDate', models.DateField()),
                ('historicalPrice', models.JSONField()),
                ('openPrice', models.FloatField()),
                ('closePrice', models.FloatField()),
                ('positiveCatalysts', models.JSONField()),
                ('negativeCatalysts', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Filing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filer', models.CharField(max_length=250)),
                ('formType', models.CharField(max_length=10)),
                ('publishDate', models.DateField()),
                ('filingYear', models.DateField()),
                ('filingQuarter', models.CharField(max_length=10)),
                ('excelLink', models.CharField(max_length=1000)),
                ('filingLink', models.CharField(max_length=1000)),
                ('financialJson', models.JSONField()),
                ('concensusForecast', models.JSONField()),
            ],
        ),
    ]
