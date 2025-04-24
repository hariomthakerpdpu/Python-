a = 20
b = 10

# 1. Add
print("Addition:", a + b)

# 2. Subtract
print("Subtraction:", a - b)

# 3. Multiply
print("Multiplication:", a * b)

# 4. Divide
print("Division:", a / b)

# 5. All operations
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)


#6. Convert Hours into Minutes
python
Copy
Edit
hours = 2
minutes = hours * 60
print("Minutes:", minutes)


#7. Convert Minutes into Hours
python
Copy
Edit
minutes = 120
hours = minutes / 60
print("Hours:", hours)


#8. Dollars to Rupees (1$ = 48 Rs)
python
Copy
Edit
dollars = 10
rupees = dollars * 48
print("Rupees:", rupees)


#9. Rupees to Dollars (1$ = 48 Rs)
python
Copy
Edit
rupees = 480
dollars = rupees / 48
print("Dollars:", dollars)


#10. Dollars to Pounds via Rs (1$ = 48 Rs, 1 Pound = 70 Rs)
python
Copy
Edit
dollars = 10
rupees = dollars * 48
pounds = rupees / 70
print("Pounds:", pounds)


#11. Grams to Kilograms
python
Copy
Edit
grams = 1000
kg = grams / 1000
print("Kilograms:", kg)


#12. Kilograms to Grams
python
Copy
Edit
kg = 1.5
grams = kg * 1000
print("Grams:", grams)


#13. Bytes to KB, MB, GB
python
Copy
Edit
bytes_val = 1048576  # 1 MB
kb = bytes_val / 1024
mb = kb / 1024
gb = mb / 1024
print("KB:", kb)
print("MB:", mb)
print("GB:", gb)


#14. Celsius to Fahrenheit
python
Copy
Edit
c = 37
f = (9/5) * c + 32
print("Fahrenheit:", f)
15. Fahrenheit to Celsius
python
Copy
Edit
f = 98.6
c = (5/9) * (f - 32)
print("Celsius:", c)


#16. Calculate Simple Interest (I = P * R * N / 100)
python
Copy
Edit
P = 1000
R = 5
N = 2
interest = (P * R * N) / 100
print("Interest:", interest)


#17. Area & Perimeter of Square
python
Copy
Edit
L = 5
area = L ** 2
perimeter = 4 * L
print("Area:", area)
print("Perimeter:", perimeter)


#18. Area & Perimeter of Rectangle
python
Copy
Edit
L = 6
B = 3
area = L * B
perimeter = 2 * (L + B)
print("Area:", area)
print("Perimeter:", perimeter)


#19. Area of Circle (A = 22/7 * r^2)
python
Copy
Edit
r = 7
area = (22 / 7) * r * r
print("Area of circle:", area)


#20. Area of Triangle (A = H * B / 2)
python
Copy
Edit
H = 10
B = 5
area = (H * B) / 2
print("Area of triangle:", area)


#21. Net Salary (Gross + 10% Allowance – 3% Deduction)
python
Copy
Edit
gross_salary = 50000
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)


#22. Net Sales (Gross Sales – 10% Discount)
python
Copy
Edit
gross_sales = 100000
discount = 0.10 * gross_sales
net_sales = gross_sales - discount
print("Net Sales:", net_sales)


#23. Total and Average of 3 Subjects
python
Copy
Edit
sub1 = 80
sub2 = 75
sub3 = 85
total = sub1 + sub2 + sub3
average = total / 3
print("Total:", total)
print("Average:", average)

#24. Swap Two Values
python
Copy
Edit
a = 10
b = 20
a, b = b, a
print("After swap: a =", a, ", b =", b)
