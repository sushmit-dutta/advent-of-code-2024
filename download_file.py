import requests

day = "3"

# Download Data
sesh_cookie = "53616c7465645f5faac007e3506faa45dbf6da89092241a5d4a847741fbe0decef3cc450693ef48f39fda83f19966e9330db573c90337762b24115c349cf7962"
headers = {"Cookie": f"session={sesh_cookie}"}
url = f"https://adventofcode.com/2024/day/{day}/input"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open(f"day_{day}_input.txt", "w") as file:
        file.write(response.text)
    print("Input file downloaded successfully!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")