import requests 

url = "http://api.weatherapi.com/v1/current.json" #/current.json is the endpoint 
key = "b3b088052d3049cd9ab175737202011"

payload1 = {
    'key': key,
    'q': "San Francisco"
}

payload2 = {
    'key': key,
    'q': "Guangzhou"
}

payload3 = {
    'key': key,
    'q': "-0.33237,8.08318"
}

payload4 = {
    'key': key,
    'q': "53.216.147.194"
}

response = requests.get(url, params=payload4)

# if status == 200 then analyze the data 
# else there's an error 
if response.status_code == requests.codes.ok:
    data = response.json()
else: 
    print("There is an error! Oh no!")

print(data["current"]["wind_dir"])

#San Francisco is N
#Guangzhou is SSE
#Lat: -0.33237, Long: 8.08318 is SSW 
#53.216.147.194 (IP Address) is NW

# data = response.json() >>> dictonary that you can work with 
# response.status_code >>> int with values 200, 300, 400, 401, 404 (200 IS GOOD)
# if status == codes.ok => status == 200

def query(location):
    payload = {
        'key': "KEYGJRGN",
        'q': location
    }
    response = requests.get(url, params=payload)
    if response.status_code == requests.codes.ok:
        response.json()
    else:
        response.text
        response.status_code

locations = ["A", "B", "C", "D"]

for loc in locations:
    query(loc)