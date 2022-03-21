from concurrent.futures import process
import csv
from itertools import product
from optparse import Values
import db


#################################################################
#                                                               #
#      This file is responsible for cleaning the data only.     #
#                                                               #
#################################################################

file = '../chesterfield1.csv'

#<-------- Extract Data form the CSV and appending it to list -------->

def ExtractData(file):
    fullDataFromCSV = []
    with open(file, 'r') as file:
        
        fieldnames=['date_time','location','Full_Name','orders','amount','payment_type','Card_Details']
        dict_reader = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')

        for item in dict_reader:
            item = dict(item)        
            if 'Card_Details' in item: del item['Card_Details']
            if 'Full_Name' in item: del item['Full_Name']
            if 'payment_type' in item: del item['payment_type']
            else: break
            fullDataFromCSV.append(item)
    return fullDataFromCSV

#<-------- Accesscing the list and splitting each item-------->

processedData = ExtractData(file)

def splittingData(processedData):
    finalProducts = []

    for singleItem in processedData:
        #row
        allOrders = (singleItem['orders'])
        individualorder = allOrders.split(",")
    
        #indivdual item
        for row in individualorder:
            row = row.rsplit("-",1)
            productName = row[0]
            productName = productName.strip()
            productPrice = row[1]
            productPrice = productPrice.replace(" ","")
            alteredProducts = {'product_name': productName,'product_price':productPrice}
            finalProducts.append(alteredProducts)
    
        return(finalProducts)

#<-------- Removing duplicates (comment out if not needed!)-------->

# def removeDuplicates(removeDuplicates):
#     newItems = []
#     for item in removeDuplicates:
#         if item not in newItems:
#             newItems.append(item)
#     return newItems

#<-------- Getting individual branch location-------->


location = ExtractData(file)

def branchLocation(location):
    currentList = []
    newBranchList = []
    for item in location:
        branch = (item['location'])
        currentList.append(branch)
        newBranchList = set(currentList)
    return(newBranchList)



#branchLocation(location)