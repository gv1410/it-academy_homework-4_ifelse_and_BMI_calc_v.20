cycle = True



while cycle:
    a_value = int(input('Введите первое значение (Значение А): '))
    b_value = int(input('Введите второе значение (Значение Б): '))
    c_value = int(input('Введите третье значение (Значение С): '))



    # Если нет ни ондого нуля - вывести: "Нет нулевых значений!!! :
    a_value > 0 and b_value > 0 and c_value > 0 and print('Нет нулевых значений!')



    # Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!": 
    value = a_value or b_value or c_value
    value > 0 and print('Первое не нулевое значение: ' + str(value))
    value == 0 and print('Все значения равны нулю!')




    if a_value > (b_value + c_value):       
        print('Первое значение больше чем сумма второго и третьего вывести значение(a - b - c) = ' + str(a_value - b_value - c_value))
    if a_value < (b_value + c_value):
        print('Первое значение меньше чем сумма второго и третьего вывести значение(b + c - a) = ' + str(b_value + c_value - a_value))
    if a_value > 50 and b_value > a_value or c_value > a_value:
        # Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася":
        print('Вася')
    if a_value > 5 or b_value == 7 and c_value == 7:
        # Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя": 
        print('Петя')




    question = input('\n Закончить работу с программой? (да / нет): ')


    if question == 'да':
        cycle = False
    elif question == 'нет':
        cycle = True
        