'''
3. Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции.
 Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

global COMMISSION_WITHDRAW
global RICH_TAX

def top_up(top_up_input):
    global start_sum
    
    if top_up_input % 50 != 0:
        print('Сумма для пополнения и снятия должна быть кратна 50.')
    else:
        start_sum += top_up_input
        top_up_operations.append(top_up_input)
        print('Ваш баланс составляет:', round(start_sum, 2))


def withdraw(withdraw_input):
    
    global start_sum
    global operation_count
    

    if withdraw_input <= start_sum:
        if withdraw_input % 50 != 0:
            print('Сумма для пополнения и снятия должна быть кратна 50.')
        else:
            operation_count += 1
            if operation_count % 3 == 0:
                start_sum -= withdraw_input * (1 + COMMISSION_WITHDRAW)
            else:
                start_sum -= withdraw_input
            withdraw_operations.append(withdraw_input)
            print('Ваш баланс: ', round(start_sum, 2))
    else:
        print('Недостаточно денег для снятия!')

def exit():
    print('До следующей встречи! :) ')
    
start_sum = 0

COMMISSION_WITHDRAW = 0.015
RICH_TAX = 0.1
operation_count = 0

top_up_operations = []
withdraw_operations = []

while True:
    if start_sum > 5000000:
        start_sum -= RICH_TAX * start_sum
        print('Вы слишком богаты. Позвольте отнять у Вас немного денюшки)')

    operation = int(input('Введите номер для операции 1-пополнить/2-снять/3-выйти: '))

    if operation == 1:
        top_up(top_up_input = int(input('Введите сумму, которую хотите пополнить: ')))

    elif operation == 2:
        withdraw(withdraw_input = int(input('Введите сумму для снятия: ')))

    elif operation == 3:
        exit()
        break

    else:
        print('Введите номер операции!')


print("Операции пополнения:", top_up_operations)
print("Операции снятия:", withdraw_operations)