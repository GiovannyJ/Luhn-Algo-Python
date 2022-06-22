"""
This is an implentation of the Luhn Algorithm which is used to check the validity of the last number in a sequence (used in credit cards)
Credit card number is 16 digits long the last digit is generated from the other 15
Note: for this algorith since the input is an int it cannot account for leading zeros
    the card number does not have to be 16 digits long for this algorith to work"""

def Luhn(cardNum: int) -> bool:
    cardNum = list(map(int, str(cardNum)))
    # check if input is 16 long
    #if len(cardNum) == 16:
    # store/remove last number
    check_num = cardNum[-1]
    remaining_nums = cardNum[0:-1]

    # take every even position and multiply it by 2
    double_even_index = remaining_nums
    for i in range(len(double_even_index)):
        if i%2==1:
            double_even_index[i] = double_even_index[i]*2
        else:
            pass

    # sum digits of ^ and other numbers remaining
    for i in range(len(double_even_index)):
        if double_even_index[i] >= 10:
            double_even_index[i] = 1 + (double_even_index[i] - 10)
        else:
            pass
    sum_of_nums = sum(double_even_index)
    
    # take sum and get remainder when/10
    # take remainer and - 10
    correct_check_num = 10 - (sum_of_nums%10)
    
    # if that new number = last num then card num is good
    if check_num == correct_check_num:
        print("Valid Number")
        return True
    else:
        print(f"The check number:{check_num} is incorrect, correct number:{correct_check_num}")
        return False

# test cases
def tests() -> None:
    #hand calculated first
    assert Luhn(5277029120773864) == True
    assert Luhn(7654002138195525) == True
    assert Luhn(2023803285235092) == False
    assert Luhn(777644) == True

tests()