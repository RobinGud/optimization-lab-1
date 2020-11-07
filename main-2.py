import math

output_file = open("./output/file_two.txt", "w")

def func(x):
    global count
    count += 1
    return (-5*x[0]**5 + 4*x[0]**4 - 12*x[0]**3 + 11*x[0]**2 - 2*x[0] + 1)
    
def func1(x):
    global count
    count += 1
    return (log(x[0]-2,10)**2 + log(10-x[0],10)**2 - x**(0.2))
    
def func2(x):
    global count
    count += 1
    return (-3*sin(0.75*x[0]) + exp -2*x[0]) 
    
def func3(x):
    global count
    count += 1
    return (exp*3*x[0] + 5 *exp -2*x[0]) 
    
def func4(x):
    global count
    count += 1
    return (0.2*log(x[0],10) + (x - 2.3)**2) 

    
def num_gradient(f, x1, x2, h=1e-4):
    der_1 = (f([x1 + h, x2]) - f([x1 - h, x2])) / (2 * h)
    der_2 = (f([x1, x2 + h]) - f([x1, x2 - h])) / (2 * h)
    return [der_1, der_2]

def an_gradient(f, x1, x2):
    der_1 = 2 * (2 * x1**3 - 2 * x1 * x2 + x1 - 1)
    der_2 = 2 * (x2 - x1**2)
    return [der_1, der_2]

def distance_between(x1, x2):
    dist = 0
    for i in range(len(x1)):
        dist += (x2[i] - x1[i])**2
    dist = math.sqrt(dist)
    return dist

def calculate_len(vector):
    length = 0
    for i in vector:
        length += i ** 2
    length = math.sqrt(length)
    return length


def dichotomy_method(f, a, b, x, gradient, eps=1e-4):
    x1_temp = [0, 0]
    x2_temp = [0, 0]
    sigma = eps / 2.0
    mid = (b + a) / 2.0
    while abs(b - a) > eps:
        x1 = mid - sigma
        x2 = mid + sigma
        for i in range(len(x)):
            x1_temp[i] = x[i] - x1 * gradient[i]
            x2_temp[i] = x[i] - x2 * gradient[i]
        if f(x1_temp) < f(x2_temp):
            b = x1
        elif f(x1_temp) > f(x2_temp):
            a = x2
        else:
            a = x1
            b = x2
        mid = (b + a) / 2.0
    return mid

def steepest_descent(f, x, gradient_func, eps=1e-4):
    x_prev = x.copy()
    x_new = [x_prev[0] + (eps * 2), x_prev[1] + (eps * 2)]
    i = 0
    while (abs(f(x_prev) - f(x_new)) > eps ) and (abs(distance_between(x_prev, x_new)) > eps):
        grad = gradient_func(f, x_prev[0], x_prev[1])
        grad_len = calculate_len(grad)
        grad = [grad[0]/grad_len, grad[1]/grad_len]
        h = dichotomy_method(f, 0, 100000, x_prev, grad)
        x_temp = x_new.copy()
        x_new = [x_prev[0] - h * grad[0], x_prev[1] - h * grad[1]]
        x_prev = x_temp
        i += 1
    output_file.write("iterations = " + str(i) + "\n")
    return x_new

count = 0
a = steepest_descent(func, [-0.5, 0.5], an_gradient)
a1 = steepest_descent(func1, [6, 9.9], an_gradient)
a2 = steepest_descent(func2, [0, 2*math.pi], an_gradient)
a3 = steepest_descent(func3, [0, 1], an_gradient)
a4 = steepest_descent(func4, [0.5, 2.5], an_gradient)
output_file.write("coordinates = " + str(a) + "\n")
output_file.write("function value = " + str(func(a)) + "\n")
output_file.write("count of calling function = " + str(count) + "\n")
output_file.write("coordinates = " + str(a1) + "\n")
output_file.write("function value = " + str(func(a1)) + "\n")
output_file.write("coordinates = " + str(a2) + "\n")
output_file.write("function value = " + str(func(a2)) + "\n")
output_file.write("coordinates = " + str(a3) + "\n")
output_file.write("function value = " + str(func(a3)) + "\n")
output_file.write("coordinates = " + str(a4) + "\n")
output_file.write("function value = " + str(func(a4)) + "\n")

