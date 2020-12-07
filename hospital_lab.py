import requests
import csv

url = "https://hm-cs.herokuapp.com"
endpoint = "/hospital"
key = "ArtOfDataKEY123"


#pull a given row number from the API
def getData(id):
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
    for i in range(0,len(string)):
        if string[i:i+1] == ",":
            line.append(string[index:i])
            index = i+1
    line.append(string[index:])
    return line

#standardize measure by changing measure to 1HAB and adjust beds accordingly
def standardize(list):
    measure = int(list[4][:len(list[4])-3])
    list[5] = float(list[5])/measure
    list[4] = "1HAB"
    return list

#getting the data from the API and writing it into a csv I called hospital_raw.csv
with open('hospital_raw.csv', 'w', newline = '') as f:
    thewriter = csv.writer(f)
    for i in range(0,135):
        string = getData(i)
        row = rewrite(string)
        thewriter.writerow(row)
        
#get all the standardized data and write into hospital_lab.csv       
with open('hospital_lab.csv', 'w', newline = '') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(rewrite(getData(0)))
    for i in range(1,135):
        string = getData(i)
        row = rewrite(string)
        standardized_row = standardize(row)
        thewriter.writerow(standardized_row)


#open hospital_lab.csv
county_list = {}
with open("hospital_lab.csv", "r") as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        #organize data by county, regardless of bed type
        county = row[2]
        #create dictionary for new county
        if county not in county_list:
            county_list[county] = []
        county_list[county].append(row[5])


#create a list with the sum of beds/person for each county
bed_sum = []
for i in county_list:
    s = sum(int(county_list[i]))
    county_list[i].append(s)
    bed_sum.append(s)


#find max and print result
maximum = max(bed_sum)
county = ""
for i in county_list:
    if county_list[i][len(county_list[i])-1] == maximum:
        county = i
print(county + " county has the most hospital beds per person")  