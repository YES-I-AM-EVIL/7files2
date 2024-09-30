# Импортируем словарь из cook_book.py
from cook_book import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    """Функция для создания списка покупок по выбранным блюдам и количеству персон."""
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено в кулинарной книге.")
    
    return shop_list

# Пример использования функции
if __name__ == '__main__':
    result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    for ingredient, details in result.items():
        print(f"{ingredient}: {details}")
