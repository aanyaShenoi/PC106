import plotly.express as px
import csv
import numpy as nmpy

def getDataSource(data_path):
    coffee_in_mL = []
    sleep_in_hours = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_mL.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x": coffee_in_mL, "y": sleep_in_hours}

def findCorrelation(data_source):
    correlation = nmpy.corrcoef(data_source["x"], data_source["y"])
    print("correlation between coffee in mililiters vs sleep in hours: \n---> ", correlation[0, 1])

def setup():
    data_path = "data.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()