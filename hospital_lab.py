import requests
import csv

url = "https://hm-cs.herokuapp.com"
endpoint = "/hospital"
key = "ArtOfDataKEY123"


#pull a given row number from the API
def getRow(id):
    payload = {
        'key': key,
        'id': str(id)
    }   
    response = requests.get(url + endpoint, params=payload)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print("Error :(")

#rewriting plain text into a list 
def rewrite(string):
    line = []
    index = 0
    for i in range(0, len(string)):
        if string[i:i+1] == ",":
            line.append(string[index:i])
            index = i+1
    line.append(string[index:])
    return line

#getting the data from the API and writing it into a csv I called hospital_raw.csv
with open('hospital_raw.csv', 'w', newline = '') as f:
    writing = csv.writer(f)
    for i in range(0,135):
        string = getRow(i)
        row = rewrite(string)
        writing.writerow(row)

#standardizing measurements by changing measure to 1HAB and adjusting beds accordingly
def standardize(list):
    measure = int(list[4][:len(list[4])-3])
    list[5] = float(list[5])/measure
    list[4] = "1HAB"
    return list
        
#geting all the standardized data and writing it into hospital_lab.csv which will be ready for analysis     
with open('hospital_lab.csv', 'w', newline = '') as f:
    writing = csv.writer(f)
    writing.writerow(rewrite(getRow(0)))
    for i in range(1,135):
        string = getRow(i)
        row = rewrite(string)
        standardized_row = standardize(row)
        writing.writerow(standardized_row)

#open hospital_lab.csv, organizing data by county (no matter the bed type), creating a dictionary for each country
counties = {}
with open("hospital_lab.csv", "r") as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        county = row[2]
        if county not in counties:
            counties[county] = []
        counties[county].append(row[5])

#creating to sum list
def summation(list):
    a = 0
    for i in list:
        a = a + float(i)
    return a

#creating a list with the sum of beds per person for each county
beds = []
for i in counties:
    a = summation(counties[i])
    counties[i].append(a)
    beds.append(a)


#finding the number max out of beds and print the result 
maximum = max(beds)
county = ""
for i in counties:
    if counties[i][len(counties[i])-1] == maximum:
        county = i

print("County with the most hospital beds per person: " + county)  