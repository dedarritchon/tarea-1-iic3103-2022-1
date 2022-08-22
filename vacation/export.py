
from typing import List
from collections import OrderedDict
import json

csv_export_folder = 'exports/csv'
json_export_folder = 'exports/json'

def to_json(items):
    return json.dumps({m.id: m.serialize() for m in items}, indent=2, sort_keys=True, ensure_ascii=False)

def export_course(courses: List[Course]):

    ingredients_template = OrderedDict({i.id: 0 for i in ingredients})
    course_id = courses[0].course_type
    counter = 1
    csv = f"course_id;name;description;" + ';'.join([k for k in ingredients_template.keys()]) + '\n'
    for c in sorted(courses, key=lambda c: c.name):
        ingredients_count = ingredients_template.copy()
        for i in c.ingredients:
            ingredients_count[i.id] += i.quantity
        csv += f"{c.id};{course_id}_{counter};{c.name}; " + ';'.join([str(k) for k in ingredients_count.values()]) + '\n'
        counter += 1

    with open(f'{csv_export_folder}/{course_id}.csv', 'w') as file:
        file.write(csv)
    
    course_json = to_json(courses)
    with open(f'{json_export_folder}/{course_id}.json', 'w') as file:
        file.write(course_json)


def run_export(number):

    ingredients_csv = "ingredient_id;name;description;price;size;expiration\n"
    counter = 1
    for i in sorted(ingredients, key=lambda i: i.name):
        ingredients_csv += f'{i.id};ingredient_{counter};{i.name};{i.price};{i.size};{i.expiration}\n'
        counter += 1

    with open(f'{csv_export_folder}/ingredients.csv', 'w') as file:
        file.write(ingredients_csv)
    
    ingredients_json = to_json(ingredients)

    with open(f'{json_export_folder}/ingredients.json', 'w') as file:
        file.write(ingredients_json)

    courses = [appetizers, soups, dishes, desserts, beverages]
    for c in courses:
        export_course(c)

    trays = generate_trays(courses, number)

    trays_csv = f"Tray_id;name;description;" + ';'.join([k[0].course_type for k in courses]) + '\n'
    counter = 1
    for m in sorted(trays, key=lambda m: m.name):
        trays_csv += f"{m.id};tray_{counter};{m.name};{m.appetizer.id};{m.soup.id};{m.dish.id};{m.dessert.id};{m.beverage.id}\n"
        counter += 1
    with open(f'{csv_export_folder}/trays.csv', 'w') as file:
        file.write(trays_csv)
    
    trays_json = to_json(trays)

    with open(f'{json_export_folder}/trays.json', 'w') as file:
        file.write(trays_json)

if __name__ == '__main__':
    run_export(2)
