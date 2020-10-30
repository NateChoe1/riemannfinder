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

print("Select mode:")
print("(1) Input a function")
print("(2) Input a table")
choice = input()
while choice != "1" and choice != "2":
    print("Please input either 1 or 2")
    choice = input()
if choice == "1":
    print("Enter the number of divisious for the approximation")
    assign_last_input()
    divisions = float(last_input)

    x = low_bound
    print("Enter in the function. Note: This must be done in python code, so instead of 5x, enter in y=5*x.")
    function = input()
    left_sum = 0
    right_sum = 0
    while x <= high_bound:
        exec(function)
        accumulate = y * (high_bound - low_bound) / divisions
        if x != high_bound:
            left_sum += accumulate
        if x != low_bound:
            right_sum += accumulate
    print("Left aligned riemann sum: " + str(left_sum))

    x = low_bound + ((high_bound - low_bound) / 2)
    mid_sum = 0
    while x < high_bound:
        exec(function)
        total += y * (high_bound - low_bound) / (divisions - 1)
        x += (high_bound - low_bound) / divisions
    #this is a bit of duplication, but fixing it would require a lot of work.

    print("Midpoint aligned riemann sum: " + str(mid_sum))
    print("Trapezoidala riemann sum: " + str((left_sum + right_sum) / 2))
else:
    iteration = low_bound
    xvalues = []
    yvalues = []
    while iteration < high_bound:
        print("Enter in an x value")
        xvalues.append(float(input()))
        print("Enter in a y value")
        yvalues.append(float(input()))
        iteration = xvalues[-1]
    lefttotal = 0
    righttotal = 0
    midtotal = 0
    for i in range(0, len(xvalues) - 1):
        lefttotal += yvalues[i] * (xvalues[i + 1] - xvalues[i])
        righttotal += yvalues[i + 1] * (xvalues[i + 1] - xvalues[i])
        if i % 2 == 1 and len(xvalues) % 2 == 1:
            midtotal += yvalues[i] * (xvalues[i + 1] - xvalues[i - 1])
    print("Left aligned riemann sum: " + str(lefttotal))
    print("Right aligned riemann sum: " + str(righttotal))
    print("Midpoint aligned riemann sum: " + str(midtotal))
    print("Trapezoidal riemann sum: " + str((lefttotal + righttotal) / 2))
