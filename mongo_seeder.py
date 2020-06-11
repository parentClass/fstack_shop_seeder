# Import
import csv
from pymongo import MongoClient
import pandas as pd
import numpy as np

# Mongo client
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false')

# Database
db = client.fstack_shop

# Mongo Seeder
# --> class responsible for seeding mongo csv files related
class MongoSeeder:
    # init
    def __init__(self, file):
        self.file = file
        self.tableColumns = []
        self.dataList = []
        self.df = pd.read_csv(file)
        self.__getColumns()
        self.__getRowsAndBuildDict()
    # Retrieve column names of csv file
    def __getColumns(self):
        # Loop through csv columns
        for column in self.df.columns:
            # Appended column name to our table columns list
            self.tableColumns.append(column)
    # Retrieve rows and build the dictionary
    def __getRowsAndBuildDict(self):
        # Loop through csv indexses
        for row in self.df.index:
            # Empty dict
            obj = {}
            # Loop through table columns
            for column in self.tableColumns:
                # Assign value to dict with specific key
                obj[column] = np.int64(self.df[column][row]).item() if isinstance(self.df[column][row], np.int64) else self.df[column][row]
            # Append dict to data list
            self.dataList.append(obj)
    # Seed process
    def seed(self, collection_name):
        # Drop collection
        db.drop_collection(collection_name)
        # Loop through data list containing dict
        for data in self.dataList:
            # Check if data not none
            if data != None:
                # Insert to collection
                result = db[collection_name].insert_one(data)
        return 'Seeding ' + self.file + ' is completed....'
