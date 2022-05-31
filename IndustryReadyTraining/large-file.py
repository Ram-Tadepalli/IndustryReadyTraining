import json
with open("large-file.json", mode='r' , encoding="utf-8") as f:
    s = f.read()
    d = json.loads(s)

    print(d[0])