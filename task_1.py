"""
Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок:
програма має автоматично генерувати нові заявки (ідентифіковані унікальним
номером або іншими даними), додавати їх до черги, а потім послідовно видаляти
з черги для "обробки", імітуючи таким чином роботу сервісного центру.
"""

from queue import Queue
from random import randint


order_queue = Queue()
order_no = 1

def generate_request(no):
    global order_no
    for i in range(0,no):
        order_queue.put(f'order {order_no}')
        order_no += 1
    print("  Order list:")
    print(order_queue.queue)

def process_request():
    print("  Processing orders:")
    while order_queue.empty() == False:
        processing_order = order_queue.get()
        print(f"order '{processing_order}' procesed")
        if order_queue.empty():
            print("  All orders competed!")

exit = 'n'
while exit == 'n':
    generate_request(randint(1,10))
    process_request()
    exit = input("Office closed?(y/n) ")
print(f"Office performance: {order_no-1} orders processed today")
