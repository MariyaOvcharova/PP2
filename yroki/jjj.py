import json

car = {
    "make": "audi", 
    "model": "TT", 
    "year": 2005
}

# car_json = json.dumps(car)

import json

car_jS = '{"make": "Subaru", "model": "Impreza", "year": 1995}'

carrs = json.loads(car_jS)
print(carrs)
