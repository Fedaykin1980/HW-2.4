cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break
        persons = int(f.readline().strip())
        cook_book[dish_name] = []
        ingridients_line = f.readline().strip()
        while ingridients_line:
            ingredients = ingridients_line.split(" | ")
            ingredients_dict = {"ingridient_name": ingredients[0], "quantity": int(ingredients[1]), "measure": ingredients[2]}
            cook_book[dish_name].append(ingredients_dict)
            ingridients_line = f.readline().strip()

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)