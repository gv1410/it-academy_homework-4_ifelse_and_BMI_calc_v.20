# Домашнее задание. Калькулятор массы тела v.2.0 
# Исполнитель: Холдеев Алексей


cycle = True
database = {}

while cycle:
    user_name = input('Введите ваше имя: ')
    user_sex = input('Введите ваш пол(м/ж): ')
    user_age = int(input('Введите ваш возраст(от 18 до 40): '))
    user_weight = float(input('Введите свой вес (кг): '))
    user_height = float(input('Введите свой рост (см): '))
    



    calc_result = int(user_weight / ((user_height / 100)**2))
    
    database[user_name] = calc_result, user_weight, user_height, user_sex, user_age
    
    question = input('Ввести еще данные?(да/нет ) ')



    if question == 'да':
        cycle = True
    elif question == 'нет':
        cycle = False

        
    
user_request = input('Чьи данные вывести на экран?' + str(database.keys()) + ': ')

user_data = database[user_request]




user_data_calc_result = int(user_data[0])

user_data_weight = int(user_data[1])

user_data_height = int(user_data[2])

user_data_sex = str(user_data[3])

user_data_age = int(user_data[4])




print('\n Индекс массы тела ' + user_request + ' равен: ', user_data_calc_result)
print('20' + ('=' * (user_data_calc_result - 20)) + '|' + ('=' * (50 - user_data_calc_result)) + '50')




if user_data_calc_result < 20 and user_data_sex == 'м' and 18 <= user_data_age >= 40:
    print('Для мужчин в возрасте от 18 до 40 это очень мало!')
elif 20 <= user_data_calc_result <=25 and user_data_sex == 'м' and 18 <= user_data_age <= 40:
    print('Для мужчин в возрасте от 18 до 40 это норма!')
elif 25 < user_data_calc_result <=30 and user_data_sex == 'м' and 18 <= user_data_age <= 40:
    print('Для мужчин в возрасте от 18 до 40 это состояние предожирения!')
elif 30 < user_data_calc_result <=35 and user_data_sex == 'м' and 18 <= user_data_age <= 40:
    print('Для мужчин в возрасте от 18 до 40 это ожирение первой степени!')
elif 35 < user_data_calc_result <=40 and user_data_sex == 'м' and 18 <= user_data_age <= 40:
    print('Для мужчин в возрасте от 18 до 40 это ожирение второй степени!')
elif 40 < user_data_calc_result and user_data_sex == 'м' and 18 <= user_data_age <= 40:
    print('Для мужчин в возрасте от 18 до 40 это ожирение третей степени!')
elif user_data_calc_result < 20 and user_data_sex == 'ж' and 18 <= user_data_age >= 40:
    print('Для женщин в возрасте от 18 до 40 это очень мало!')
elif 20 <= user_data_calc_result <=25 and user_data_sex == 'ж' and 18 <= user_data_age <= 40:
    print('Для женщин в возрасте от 18 до 40 это норма!')
elif 25 < user_data_calc_result <=30 and user_data_sex == 'ж' and 18 <= user_data_age <= 40:
    print('Для женщин в возрасте от 18 до 40 это состояние предожирения!')
elif 30 < user_data_calc_result <=35 and user_data_sex == 'ж' and 18 <= user_data_age <= 40:
    print('Для женщин в возрасте от 18 до 40 это ожирение первой степени!')
elif 35 < user_data_calc_result <=40 and user_data_sex == 'ж' and 18 <= user_data_age <= 40:
    print('Для женщин в возрасте от 18 до 40 это ожирение второй степени!')
elif 40 < user_data_calc_result and user_data_sex == 'ж' and 18 <= user_data_age <= 40:
    print('Для женщин в возрасте от 18 до 40 это ожирение третей степени!')
else:
    print('Что бы получить рекомендацию введите другие данные!!!')