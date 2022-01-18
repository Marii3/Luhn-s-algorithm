sum_ = 0
numer = 4388576018402626
while numer != 0:
    sum_ += numer%10

    numer = numer //10
    step_1= numer % 10 * 2
    if step_1 > 9:
        step_1 = step_1 % 10 + 1
    
    sum_ += step_1
    numer = numer //10
    
if sum_ % 10 != 0:
    print("card is not valid")
else:
    print("card is valid")