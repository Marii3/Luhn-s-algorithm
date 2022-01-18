def card(number):
    sum_ = 0
    number_coverted= str(number)
    list_number= list(number_coverted)
    number_len= len(number_coverted)
    while number!=0:
        if number_len > 12 or number < 17:
            if list_number[0] == "4" or list_number[0]== "5" or list_number[0]== "6" or (list_number[0] == "3" and list_number[1] == "7"):
                
                sum_ += number%10
                number = number //10
                step_1= number % 10 * 2
                if step_1 > 9:
                    step_1 = step_1 % 10 + 1
    
                sum_ += step_1
                number = number //10
        
    if sum_ % 10 != 0:
        print("card is not valid")
    else:
        print("card is valid")
        

card(4556737586899855)