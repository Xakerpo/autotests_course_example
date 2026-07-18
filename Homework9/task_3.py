# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt', 'r') as file:
    file_purchases = file.read()
    purchases = file_purchases.split('\n\n')
    sum_purchases = []

    for purchase in purchases:
        numbers = purchase.split('\n')
        sum_of_numbers = sum(int(num) for num in numbers)
        sum_purchases.append(sum_of_numbers)

    most_expensive_purchases = (sorted(sum_purchases, reverse=True)[:3])

three_most_expensive_purchases = sum(most_expensive_purchases)



assert three_most_expensive_purchases == 202346