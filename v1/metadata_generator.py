#from importlib.metadata import metadata
import json
import os
#from PIL import Image

#  image: `${baseUri}/${_edition}.gif`, (js)

baseUri = 'QmXcreguUf4mo4YPqiwf1VoQq7mTvEDugyM2qnjLLoBqZJ'

def create_metadata( edition: int):
    metadata = {
        'name': f'PrintCLub #{edition}',
        'description': 'Print Club NFT collection',
        'symbol': "PC",
        'image': f'{edition}.png',
        'animation_url': f'{edition}.mp4',
        'edition': edition,
        'attributes': [
            {"trait_type": "EcoFriendly", "value": "100"},
            {"trait_type": "Unique", "value": "1/250"},
        ],
        "collection":{
            "name":"PrintClub",
            "family":"PC    "
        },
        "properties":{
            "files":[
            {
                "uri":"image.png",
                "type":"image/png"
            }
        ],
        "category":"video",
        "creators":[
            {
                "address":"SeHr9EhZRm48Wu6APGnWsxPDha51iYygMPyvXwobHfo",
                "share":100
            }
        ]
        }
    }
    return metadata


for i in range(0,5):
    metadata = create_metadata(i)
    with open(f'{i}.json', 'w', encoding='utf-8') as outfile:json.dump(metadata, outfile, indent=2)