import random

def random_choice():                                      #Функция подбора случайного числа 1 поля
    number1 = random.randint(3,21)
    return number1
    
first_number = random_choice() 
print(f'Введите пароль для числа: {first_number}')    #Вывод на экран числа

def define_password(i):
    passwords = {}
    passwords.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746})
    passwords.update({11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968})
    passwords.update({15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passwords.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
    key = passwords.get(i)
    return key

random_choice()
pair_1 = list(range(1, first_number))
pair_2 = list(range(1, first_number))


pairs_list = []
result = ''
for i in pair_1:
    for j in pair_2:
        num1 = i
        num2 = j
        if num1 >= num2:
            continue
        else:
            check_right = first_number % (num1 + num2)
            if check_right == 0:
                pairs_list.append([num1, num2])
                result = result + str(num1) + str(num2)

print('Пары: ', *pairs_list)
print('Необходимо ввести во вторую вставку пароль: ', result)
if int(result) == define_password(first_number):
    print('Проходите!')

                
