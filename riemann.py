import math

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

last_input = ""
def assign_last_input():
    global last_input
    last_input=input()
    while not is_number(last_input):
        print("Please enter in an actual number")
        last_input = input()

print("Enter the lower bound for the approximation")
assign_last_input()
low_bound = float(last_input)

print("Enter the upper bound for the approximation")
assign_last_input()
high_bound = float(last_input)

print("Enter the number of divisious for the approximation")
assign_last_input()
divisions = float(last_input)

#This is bad practice with 3 repeats, but honestly I don't care.

x = low_bound
print("Enter in the function. Note: This must be done in python code, so instead of 5x, enter in 5*x. This is extremely bad practice and will almost definitely result in glitches if you try, but I don't care.")
function = input()
total = 0
while x < high_bound:
    exec(function)
    x += (high_bound - low_bound) / divisions
    total += y * (high_bound - low_bound) / divisions
left_sum = total
print("Left aligned riemann sum: " + str(total))


total = 0
x = high_bound
while x > low_bound:
    exec(function)
    x -= (high_bound - low_bound) / divisions
    total += y * (high_bound - low_bound) / divisions
right_sum = total
print("Right aligned riemann sum: " + str(total))

x = low_bound + ((high_bound - low_bound) / 2)
total = 0
while x < high_bound:
    exec(function)
    x += (high_bound - low_bound) / divisions
    total += y * (high_bound - low_bound) / (divisions - 1)
    print(x)

print("Midpoint aligned riemann sum: " + str(total))

print("Trapezoidala riemann sum: " + str((left_sum + right_sum) / 2))
