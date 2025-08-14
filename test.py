def calculate_discount(billAmount):
    sumEven = 0
    sumOdd = 0
    
    for digitChar in str(billAmount):
        digit = int(digitChar)
        
        if digit % 2 == 0:
            # sumEven += digit
            sumEven = sumEven+digit
        else:
            sumOdd += digit
    
    discount = sumEven * sumOdd
    return discount
billAmount = int(input("Enter the total bill amount: "))
discount = calculate_discount(billAmount)
print("Discount amount:", discount)


