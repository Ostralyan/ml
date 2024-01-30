x_train = [0, 2, 20, 1, 3, 23]
y_train = [1, 1, 2, 1, 1, 2]

def cost_function(x_train, y_train, w, b):
    m = len(x_train)

    sum = 0

    for i in range(m):
        f_wb = w * x_train[i] + b
        cost = (f_wb - y_train[i]) ** 2
        sum += cost

    return sum / 2 * m


result = cost_function(x_train, y_train, 0.01, 0)
print(result)
