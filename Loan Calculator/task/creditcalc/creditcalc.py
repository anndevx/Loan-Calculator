import math
principal = int(input('Enter the loan principal:'))
print('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:''')
choosing = input()

if choosing == "m":
    numof_monthly_payments = int(input('Enter the monthly payment:'))
    result_m = principal / numof_monthly_payments
    round(result_m)
    if result_m == 1:
        print(f'It will take {result_m} month to repay the loan')
    elif result_m > 1:
        round(result_m)
        print(f'It will take {result_m} months to repay the loan')
elif choosing == "p":
    payments = int(input('Enter the number of months:'))
    result_p = principal / payments
    result = math.ceil(result_p)
    lastpayment = principal - (payments - 1) * result
    if payments % 2 == 0:
        print(f'Your monthly payment = {result}')
    else:
        print(f'Your monthly payment = {result} and the last payment = {lastpayment}.')
    
    
    
    
    
    
    
    
    










