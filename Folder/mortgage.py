### mortgage.py

# taking inputs
prin = int(input('Principal Loan Amount: '))
apr = float(input('Annual Interest Rate: '))
loan_term = int(input('Loan term (years): '))

# calculating monthly interest and number of payments
mnth_intrst = apr/12 
num_pymnt = loan_term * 12

# payment formula
payment = (prin * mnth_intrst * (1+mnth_intrst)**num_pymnt)/((1+mnth_intrst)**num_pymnt - 1)

print('Monthly Payment: ', str(round(payment,2)))