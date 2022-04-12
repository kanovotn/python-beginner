# Find number palindrome
def isNumberPalindrome(number):
    num = number
    reverseNum = 0
    
    while num > 0:
        remainder = num % 10
        reverseNum = (reverseNum * 10) + remainder
        num = num // 10
    
    if number == reverseNum:
        return f"Number {number} is palindrome!"
    else:
        return f"Number {number } is not palindrome!"

def oddAndEvenInList(list1, list2):
    result_list = []

    [ result_list.append(item) for item in list1 if item % 2 != 0 ]
    [ result_list.append(item) for item in list2 if item % 2 == 0 ]
    return "".join(str(result_list))

def calculateIncomeTax(income):
    totalTax = 0
    firstTax = 10000
    secondTax = 10000
    
    # First range - zero tax
    if income - firstTax <= 0:
        return 0
    
    # Second range - 10%
    if income - (firstTax + secondTax) <= 0:
        return (income - firstTax) * 0.1
    
    # Third range - 20%
    return (secondTax * 0.1) + ((income - firstTax - secondTax) * 0.2)
    
def multiplicationTable(limit):
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            print(i * j, end=" ")
        print("")

def halfPyramidDownward(size):
    for i in range(size):
        for j in range(size - i):
            print("*", end=" ")
        print("")

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = base * result
        num = num - 1
    return f"{base} raises to power of {exp}: {result}"

print(isNumberPalindrome(454))
print(isNumberPalindrome(13467))
print(oddAndEvenInList([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))
print(calculateIncomeTax(25000))
multiplicationTable(10)
halfPyramidDownward(5)
print(exponent(2, 5))
