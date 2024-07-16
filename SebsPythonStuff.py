import requests
from dataclasses import asdict
from StableDiffusionModel import StableDiffusionModel

listOfPrompts = [["an elf, holding a sword"], ["a man, holding an axe"]]
# Step 2: Define the API endpoint URL
url = "http://0.0.0.0:7861/sdapi/v1/txt2img"

for prompt in listOfPrompts:
    
    model = StableDiffusionModel()
    model.update(prompt=prompt[0])
    print(prompt[0])

    modelData = asdict(model);

    # Step 3: Make the GET request
    response = requests.post(url, json=modelData)

    # Step 4: Check the response status
    if response.status_code == 200:
        # Step 5: Extract and print the response data
        data = response.json()
    else:
        print("Failed to retrieve data", response.status_code)