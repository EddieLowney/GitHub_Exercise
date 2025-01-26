### sleep.py

# input
dly_hrs = input('Enter number of hours of sleep per night ')

# calculating values
wkly_hrs = float(dly_hrs) * 7
mnthly_hrs = wkly_hrs * 4.3
days_slept = mnthly_hrs / 24

print('Sleep Stats Computed.')
print('Hours slept per week: ', str(round(wkly_hrs)))
print('Hours slept per month: ', str(round(mnthly_hrs,1)))
print('In a month, you sleep for about ', str(round(days_slept,2)), ' days')