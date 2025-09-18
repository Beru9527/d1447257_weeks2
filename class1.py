a = float(input("請輸入第一個數字："))
b = float(input("請輸入第二個數字："))
print("\n[Results of Two Numbers]")
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "×", b, "=", a * b)

if b != 0:
    print(a, "÷", b, "=", a / b)
else:
    print(a, "÷", b, "= Cannot divide by zero")
print("\n[三數平均值]")
x = float(input("請輸入第一個數字:"))
y = float(input("請輸入第二個數字："))
z = float(input("請輸入第三個數字："))

average = (x + y + z) / 3
print(f"三數平均值為{average}")