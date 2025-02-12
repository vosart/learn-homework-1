"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sales =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    all_sales, avg_sales = 0, 0
    total_sales_count = 0
    print('Общее количество продаж:')
    for el in sales:
        unit_sale = sum(el["items_sold"])
        all_sales += unit_sale
        print('- {product}: {unit_sale}'.format(product = el["product"], unit_sale = unit_sale))
    print('Среднее количество продаж:')
    for el in sales:
        total_sales = sum(el["items_sold"])
        sales_count = len(el["items_sold"])
        total_sales_count += sales_count
        avg_unit_sale = round(total_sales/sales_count, 2)
        print('- {product}: {avg_unit_sale}'.format(product = el["product"], avg_unit_sale = avg_unit_sale))

    avg_sales = all_sales / total_sales_count         
    print('Суммарное количество продаж всех товаров: ', all_sales)
    print('Среднее количество продаж всех товаров: ', avg_sales)
    
if __name__ == "__main__":
    main()
