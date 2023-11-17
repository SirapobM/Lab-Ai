import json
from urllib.request import urlopen as uo

climate = "&climate"

domain = "http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16"

param = [
    "PM25",
    "PM10",
    "O3",
    "CO",
    "NO2",
    "SO2",
    "WS",
    "WD",
    "TEMP",
    "RH",
    "BP",
    "RAIN",
]

print("\nWeather : ", param)
params = []

while True:
    print("Enter 'end' exit , Enter 'all' select all weather.")
    in_param = input(f"Enter your weather : ")
    if in_param.lower() == "end":
        break
    elif in_param.lower() == "all":
        params = param.copy()
        print("Select all.")
        break
    elif in_param.upper() in param:
        params.append(in_param)
        print(f"\nInput value '{params}' ")
    else:
        print(f"Error!!")

print("Your value is : ", in_param)
print("\nWeather information is : 2023-10-01 to 2023-11-06")

sdate = ""
edate = ""
stime = ""
etime = ""

while sdate == "":
    sdate = input("Enter started date (format YYYY-MM-DD): ")

sdate = "&sdate=" + sdate

while stime == "":
    stime = input("Enter started time (format HH): ")

stime = "&stime=" + stime

while edate == "":
    edate = input("Enter ended date (format YYYY-MM-DD): ")

edate = "&edate=" + edate

while etime == "":
    etime = input("Enter ended time (format HH): ")

etime = "&etime=" + etime
link = domain + in_param + sdate + edate + stime + etime
obj = json.load(uo(str(link)))
main_station = obj["stations"][0]["data"]

heading = "|    Date & Time    |"

for head in range(len(params)):
    heading += " " + params[head] + " |"

print(heading)

for count in range(len(main_station)):
    line = ""
    for slot, value in main_station[count].items():
        if slot == "DATETIMEDATA":
            line += "|" + value + "|"
        else:
            tValue = str(value)

            if (tValue == "None") | (tValue == ""):
                tValue = "-"

            line += tValue + "|"

    print(line)
