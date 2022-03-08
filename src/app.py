import csv

with open('../chesterfield1.csv', 'r') as file:

    fullDataFromCSV = []

    fieldnames=['Date/Time','Location','Full_Name','Order','Amount','Payment_Type','Card_Details']
    dict_reader = csv.DictReader(file, fieldnames = fieldnames, delimiter=',')

    for item in dict_reader:
        item = dict(item)        
        if 'Card_Details' in item:
            del item['Card_Details']
        if 'Full_Name' in item:
            del item['Full_Name']
        else:
            break
        fullDataFromCSV.append(item)
    print(fullDataFromCSV)    
        

