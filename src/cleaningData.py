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

file = '../chesterfield2.csv'

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
    products =[]
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
            products.append(alteredProducts)

 #if its in final products dont add it

# The strategy is to convert the list of dictionaries to a list of tuples where the tuples contain the
# items of the dictionary. Since the tuples can be hashed, you can remove duplicates using set
# (using a set comprehension here, older python alternative would be set(tuple(d.items()) for d 
# in l)) and, after that, re-create the dictionaries from tuples with dict.
# processedData = ExtractData(file)
# Source: stackoverflow

        seen = set()        
        for item in products:
            t = tuple(sorted(item.items()))
            if t not in seen:
                seen.add(t)
                finalProducts.append(item)
        return finalProducts


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


#print(len(splittingData(processedData))) #<-----779 items
#branchLocation(location)
#print(removeDuplicates(processedData))
#print(splittingData(processedData))
#print(splittingData(processedData))