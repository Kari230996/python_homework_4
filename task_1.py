'''
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''


def end_with_s(str_):

    if str_.endswith('s') and len(str_) > 1:
        new_str_ = str_[:-1]
        list_without_s.append(new_str_)
        return None

    
    else:
        return str_


str_1 = 'kanguroo'
str_2 = 'cars'
str_3 = 'koala'
str_4 = 'pinguins'
str_5 = 'snickers'

list_without_s = []


end_with_s(str_1)
end_with_s(str_2)
end_with_s(str_3)
end_with_s(str_4)
end_with_s(str_5)

print(list_without_s)





        
    
    
print(end_with_s(str_4))
