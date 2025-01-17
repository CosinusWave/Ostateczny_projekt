import json

with open("music_data.json", "r") as f:
    data = json.load(f)

print(data)
x = input("Podaj Album: ")

if x not in data:
    print("error")
else:
    print(f"Artysta: {data[x]['artistName']}")