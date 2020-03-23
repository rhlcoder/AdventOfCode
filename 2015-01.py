from utiles import open_txt_asociado

texto = open_txt_asociado()

balance = 0
step = 0
flag = 0

for i in texto:
    if i == '(': balance += 1
    if i == ')': balance -= 1
    
    step += 1
    if balance == -1 and flag== 0:
        print(f'Steps to basement: {step}')
        flag = 1


print(f'Final balance: {balance}')
