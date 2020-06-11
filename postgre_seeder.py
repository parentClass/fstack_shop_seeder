# Imports
import csv
import pandas as pd
import numpy as np
import psycopg2
import psycopg2.extras as pextra
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Postgre Seeder
# --> class responsible for seeding postgeSql csv files related
class PostgreSeeder:
    # init
    def __init__(self, file):
        self.file = file
        self.tableColumns = []
        self.multiDimeList = []
        self.df = pd.read_csv(file)
        self.__getColumns()
        self.__getRowsAndBuildMultiDime()
        self.__createDatabase()
    # Retrieve column names of csv file
    def __getColumns(self):
        # Loop through csv columns
        for column in self.df.columns:
            # Appended column name to our table columns list
            self.tableColumns.append(column)
    # Retrieve rows and build the dictionary
    def __getRowsAndBuildMultiDime(self):
        # Loop through csv indexses
        for row in self.df.index:
            # Empty data list
            dataList = []
            # Loop thru table columns
            for column in self.tableColumns:
                # Check if value is none
                if pd.isnull(self.df[column][row]):
                    # Append 0 value
                    dataList.append(np.int64(0).item())
                else:
                    # Appended data row to data list
                    dataList.append(np.int64(self.df[column][row]).item() if isinstance(self.df[column][row], np.int64) else self.df[column][row])
            # Appended the whole list to the multi dime list containing all tuple values
            self.multiDimeList.append(tuple(dataList))
    # Seed process
    def seed(self, table_name):
        try:
            # Create table
            self.__createTables(table_name)
            # Instantiate database
            db = self.__dbInstance('fstack_shop')
            # Build query
            for single_data in self.multiDimeList:
                # Try to execute insert
                try:
                    # Insert execution
                    db.execute("insert into " + table_name + " (" + str(",".join([str(s) for s in self.tableColumns])) + ") values " + str(single_data))
                except psycopg2.Error as e:
                    # Pass by duplicate entry
                    if e.pgcode == "23505":
                        pass
            # Return final message, stating seeding is completed
            return 'Seeding ' + self.file + ' is completed....'
        except Exception as err:
            # Print error
            print(err)
        finally:
            # Close db connection
            db.close()
    # Drop and create database
    def __createDatabase(self):
        try:
            # Instantiate database
            db = self.__dbInstance()
            # Create database
            db.execute('CREATE DATABASE fstack_shop;')
        except psycopg2.errors.ObjectInUse:
            # Catch object in use
            print("Please close postgreSQL connection to the database, database in use error when i'm trying to drop the database....")
        except psycopg2.errors.DuplicateDatabase:
            return True
        except Exception as err:
            # Print error
            print("Failed in creating database....")
        finally:
            # Close db connection
            db.close()
    # Create tables
    def __createTables(self, table):
        try:
            # Instantiate database
            db = self.__dbInstance("fstack_shop")
            # Check table used
            if table == "orders":
                # Orders query table
                return db.execute("drop table if exists orders; create table orders (id serial primary key, created_at timestamp without time zone default (now() at time zone 'Australia/Melbourne'), order_name text not null, customer_id text not null);")
            elif table == "order_items":
                # Order items query table
                return db.execute("drop table if exists order_items; create table order_items (id serial primary key, order_id integer unique, price_per_unit numeric default 0.00, quantity integer default 0, product text);")
            elif table == "deliveries":
                # Deliveries query table
                db.execute("drop table if exists deliveries; create table deliveries (id serial primary key, order_item_id integer unique, delivered_quantity integer);")
            else:
                pass
        except psycopg2.errors.ObjectInUse:
            # Catch object in use
            print("Please close postgreSQL connection to the database, database in use error when i'm trying to drop the tables....")
        except Exception:
            # Print error
            print("Failed in creating tables....")
        finally:
            # Close db connection
            db.close()
    def __dbInstance(self, database_name=None):
        try:
            # Postgre connection
            connection = psycopg2.connect(host="127.0.0.1", user="postgres", password="password") if database_name == None else psycopg2.connect(host="127.0.0.1", database=database_name, user="postgres", password="password")
            # Set connection isolation level
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Connection cursor
            return connection.cursor()
        except:
            # Print error
            print('Database problem....')