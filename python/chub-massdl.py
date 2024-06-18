import requests

list = """
username/id
username/id
username/id
""".strip().splitlines()

print(list)

for i in list:
 url = f"https://avatars.charhub.io/avatars/{i}/chara_card_v2.png"
 fn = i.replace("/", "_") + ".card.png"
 r = requests.get(url).content
 with open(fn, 'w') as f:
  f.write(r)