import requests

url = "https://marvelstefan-skliarovv1.p.rapidapi.com/getCharacters"

headers = {
	"X-RapidAPI-Key": "fa496f835cmsh4a81279f7f21920p10ef49jsn3c9d647f0d2c",
	"X-RapidAPI-Host": "Marvelstefan-skliarovV1.p.rapidapi.com"
}

response = requests.post(url, headers=headers)

print(response.json())