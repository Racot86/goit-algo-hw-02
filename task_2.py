'''
Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає
всі його символи до двосторонньої черги (deque з модуля collections в Python),
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок
паліндромом. Програма повинна правильно враховувати як рядки з парною,
так і з непарною кількістю символів, а також бути нечутливою до регістру та
пробілів.
'''
from collections import deque

def revere_method(expression):
    if expression != "":
        d_exp_rev = deque(expression)
        d_exp_rev.reverse()
        s_exp_rev = "".join(d_exp_rev)
        if expression.lower() == s_exp_rev.lower():
            print("Reverse method: This expression is polindrom")
            return True
        else:
            print("Reverse method: This expression is NOT a polindrom")
            return False

def compare_method(expression):
    if len(expression)> 0:
        d_exp = deque(expression)
        no_of_cycles = 0
        
        if len(expression)%2 == 0:
            no_of_cycles = int(len(d_exp)/2)
        else:
            no_of_cycles = int((len(d_exp) + 1)/2) - 1
        
        match = 1
        for i in range(0, no_of_cycles):
            c_r = d_exp.pop()
            c_l = d_exp.popleft()
            if c_l.lower() != c_r.lower():
                match = 0
        if match == 1:
            print('Compare method: This expresson is polindrom')
            return True
        else:
            print('Compare method: This expresson is NOT a polindrom')
            return False

expression = input('Enter expression: ')
#expression  = "tEneT tenet"
revere_method(expression)
compare_method(expression)    