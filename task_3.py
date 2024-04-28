"""
Завдання 3 (необов'язкове завдання)

Напишіть програму, яка читає рядок з послідовністю символів-розділювачів,
наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли
розділювачі симетричні, несиметричні, наприклад ( ( ( ) , або коли
розділювачі різних видів стоять у парі, як-от ( }.

( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
( 23 ( 2 - 3);: Несиметрично
( 11 }: Несиметрично

"""


rules = {"{":"}",
        "[":"]",
        "(":")"
        }

def check_syntaxis(exp, rules):
    stack = []
    for i in exp:
        if i in rules.keys():
            stack.append(i)
        elif i in rules.values():
            if len(stack) > 0 and rules[stack[-1]] == i:
                stack.pop()
            else:
                print(f"  SYNTAX_ERROR: Wrong closing bracket: must be '{rules[stack[-1]]}' but found '{i}'")
    if len(stack) == 0:
        print('  SUCCESS: Syntax is valid')
        return True
    else:
        print(f"  SYNTAX_ERROR: Missing closing brackets for '{', '.join(stack)}'")
        return False

    
exp_1 = '( ){[ 1 ]( 1 + 3 )( ){ }}'
exp_2 = '( 23 ( 2 - 3);'
exp_3 = '( 11 }'
print(f'Syntax check for "{exp_1}"')
check_syntaxis(exp_1,rules)
print(f'Syntax check for "{exp_2}"')
check_syntaxis(exp_2,rules)
print(f'Syntax check for "{exp_3}"')
check_syntaxis(exp_3,rules)
