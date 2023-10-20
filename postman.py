import json
file=open("response.json",encoding="UTF-8")
lines=json.load(file)
print(lines)
for i in range(200):
    print(lines[i]["id"])
    print(lines[i]["title"])
    print(lines[i]["completed"])
    print("")