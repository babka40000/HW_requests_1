import requests

base_path = "https://superheroapi.com/api/2619421814940190/"

super_heroes = ["Hulk", "Captain America", "Thanos"]

max_intelligence = 0
max_intelligence_name = ""

for hero in super_heroes:
    search_path = f"{base_path}search/{hero}"
    response_json = requests.get(search_path).json()
    if int(response_json["results"][0]["powerstats"]["intelligence"]) > max_intelligence:
        max_intelligence = int(response_json["results"][0]["powerstats"]["intelligence"])
        max_intelligence_name = hero

print(f"Самый умный супергерой - {max_intelligence_name}. Значение ума - {max_intelligence}")