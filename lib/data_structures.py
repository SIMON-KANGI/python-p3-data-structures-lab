spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
new_dict=list()
def get_names(spicy_foods):
    for item in spicy_foods:
        names=(item["name"])
        new_dict.append(names)
    print(new_dict)
    pass
get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item['heat_level']< 5:
            del item
        else:
            print(item)
        
    pass
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        heat_level="🌶️" * item["heat_level"] 
        print(f'{item["name"]}({item["cuisine"]}) | Heat Level:{heat_level} ')
    pass
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"]== cuisine:
            print(item) 
    pass
get_spicy_food_by_cuisine(spicy_foods, "Thai")

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"] >5:
            heat_level="🌶️" * item["heat_level"] 
            print(f'{item["name"]}({item["cuisine"]}) | Heat Level:{heat_level} ')
    pass
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    foods=len(spicy_foods)
    total=0
    for item in spicy_foods:
        heat=item["heat_level"]
        total+=heat
    average=total/foods
    print(average)
        
    pass
get_average_heat_level(spicy_foods)

spicy_food=dict()
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    pass
create_spicy_food(spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })