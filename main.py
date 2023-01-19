#funtion to tell if there is a m (for a million) or k for 1000 then covert into said number
def check_if_m_or_k(num):
    millon = "m"
    Millon = "M"
    thos = "k"
    Thos = "K"
    if millon in num or Millon in num:
        num = num[:-1]
        num = float(num)
        num = num * 1_000_000
    elif Thos in num or thos in num:
        num = num[:-1]
        num = float(num)
        num = num * 1_000
    else:
        num = float(num)
    return num



#runs the full calculator
while True:
    op = input("Please Enter a operator(*,+,%,-) or exit to stop : ")
    if op == "exit":
        break
    num1 = (input("what is your first number: "))
    num2 = (input("what is your second number: "))
    num1 = check_if_m_or_k(num1)
    num2 = check_if_m_or_k(num2)


    if op == "+":
        ans = num1 + num2
        print("your answer in ", ans)
    elif op == "-":
        ans = num1 - num2
        print("your answer in ", ans)
    elif op == "*":
        ans = num1 * num2
        print("your answer in ", ans)
    elif op == "%":
        ans = num1 % num2
        print("your answer in ", ans)
    else:
        print("please enter a valid operation")





