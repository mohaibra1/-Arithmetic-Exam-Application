import random
n = 0
# write your code here
operation_1 = "simple operations with numbers 2-9"
operation_2 = "integral squares of 11-29"
def calculator(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
        
def square(num):
    return num * num
    
def print_question(inn):
    result = 0
    if inn == 1:
        x = random.randint(2,9)
        y = random.randint(2,9)
        r = random.randint(0,2)
        container = ['+','-','*']
        si = container[r]
        print(f'{x} {si} {y}')
        return calculator(x, y, si)
    elif inn == 2:
        s = random.randint(11,29)
        print(s)
        return square(s)
    
def process_calculator(inn):
    global n
    i = 0
    result = 0
    while i < 5:
        result = print_question(inn)
        while True:   
            try:
                ans = int(input())
                break
            except:
                print('Incorrect format.----')
                continue
        if result == ans:
                print('Right!')
                n += 1
        else:
            print('Wrong!')
            
        i += 1
def save_to_file(name,level):
    operation = operation_1
    if level == 2:
        operation = operation_2
        
    temp = f"{name}: {n}/5 in level {level} ({operation})"
    with open('results.txt', 'a') as file:
        file.write(temp)
        print('The results ae saved in "results.txt"')
        

def process_input():
    print("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29
        """)
    while True:
        try:
            level = int(input())
            if level == 1 or level == 2:
                break
            raise Exception 
        except:
            print('Incorrect format.')
            continue
    process_calculator(level) 
    str_file = f'Your mark is {n}/5'
    print(f'{str_file}. Would you like to save yes or no?')
    ans = input()
    if ans in ['yes', 'YES', 'y', 'Yes']:
        print('What is your name?')
        name = input()
        save_to_file(name, level)
        

process_input()
