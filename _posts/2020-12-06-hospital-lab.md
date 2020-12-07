---
#Frontmatter
layout: post
title: Hospital Lab
---

# My Process

### Main Steps I Took
1. Query the server to generte a CSV with raw data.
2. Clean and standarize the data so I can find what I'm looking for: which county in NY state has the most hospital beds per person. This meant that I wanted to convert XHAB to 1HAB for each county, and then I want to find the max value in the beds column of the cleaned CSV. 
3. I then did an analysis of the cleaned CSV as described above to find which county in NY state has the most hospital beds per person.  

### The How & Setbacks
I knew that I had to access the API using similar techniques as the weather API classwork, so I approached this lab with the same techniques. There were two differences: 1) I had to get the "id"th row from the API that was accomplished with my getRow function shown below and 2) I tested the data retreval with the status code 200, which indicates the request has succeeded otherwise it throws an error. Figuring out how to get the "id"th row rather than just inputting a known datapoint like in the weather API took me a minute to figure out, but I eventually got it during class.
```
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
``` 

Now since I could access the data, I wanted to put it into a CSV. However, I realized that the data was plain text and not JSON compared the weather API as the examples show down below. So, I had to create a function I called rewrite to convert the plain text into a list, so then I could start cleaning and analyzing the raw data. This accomplished my main step 1. 

#### AOD API Plain Text 
**https://hm-cs.herokuapp.com/hospital?key=ArtOfDataKEY123&id=126 gave me...**
US,NY,wayne,ACUTE,1000HAB,1.312307,91442,2018

#### Weather API JSON
**http://api.weatherapi.com/v1/current.json?key=b3b088052d3049cd9ab175737202011&q=%22San%20Francisco%22**
{"location":{"name":"San Francisco","region":"California","country":"United States of America","lat":37.78,"lon":-122.42,"tz_id":"America/Los_Angeles","localtime_epoch":1607314656,"localtime":"2020-12-06 20:17"},"current":{"last_updated_epoch":1607313610,"last_updated":"2020-12-06 20:00","temp_c":13.3,"temp_f":55.9,"is_day":0,"condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/night/116.png","code":1003},"wind_mph":0.0,"wind_kph":0.0,"wind_degree":0,"wind_dir":"N","pressure_mb":1023.0,"pressure_in":30.7,"precip_mm":0.0,"precip_in":0.0,"humidity":69,"cloud":50,"feelslike_c":12.8,"feelslike_f":55.0,"vis_km":16.0,"vis_miles":9.0,"uv":1.0,"gust_mph":6.3,"gust_kph":10.1}}
 
 Looking at the raw data CSV, I saw that I had to standardize the data by changing the "measure" from XHAB to 1HAB, which will give how many hospital beds per one person in each corresponding county. I called this function unitize and all I had to do here was divide beds by measure or the X in XHAB. 

 Once I unitized the data, I then saw that the raw CSV had multiple values for each country. I used similar logic here for the iris lab a while ago by using dictionaries. I used the name of the county as the key and then put the corresponding beds value in a list which would be the value of the key in the dictionary. After restructuring the data into a dictionary, I could finally do analysis. I created the summation function to sum all of the beds values for each county, and those values were appended to another list called beds. I tried to use the sum function instead of creating a summation function, but I couldn't figure out a type discrepancy, so I hope to figure this out eventually. I then used the max function on the beds list to find the county with the largest number of beds per person. 

### Results 
I ended up finding that New York county has the most hospital beds per person. Not surprising :( (but I guess this data is from 2018/2019)

### Logistics 
In terms of who I worked with, I worked through code and errors in a breakout room with Alex, David, Lucca, and Ethan on Thursday. I asked Harry questions and checked my final answer for the county with the most hospital beds with him as well. I answered a few of Aidan's questions about creating the csv file.