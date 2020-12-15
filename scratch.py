from math import sqrt as sq
from matplotlib import pyplot as plt

def size(h):
    return sq(h[0] ** 2 + h[1] ** 2 + h[2] ** 2 + h[3] ** 2)

def qsquare(h):
    new_0 = h[0] ** 2 - h[1] ** 2 - h[2] ** 2 - h[3] ** 2
    new_1 = 2 * h[0] * h[1]
    new_2 = 2 * h[0] * h[2]
    new_3 = 2 * h[0] * h[3]
    return (new_0,new_1,new_2,new_3)

def main(h,c):
    return tuple(map(lambda i,j: i + j,qsquare(h),c))

def main_recursion(h,n):
    if n == 1:
        return main((0,0,0,0),h)
    else:
        return main(main_recursion(h,n-1),h)

def mandelbrot(h):
    if size(main_recursion(h,9)) <= 1000000:
        return True
    else:
        return False

def man_set(p):
    output_data = []
    input_data = [-1 + n/(2 ** (p - 1)) for n in range(round(2 * 2 ** (p - 1) + 1))]
    for a in input_data:
        for b in input_data:
            for c in input_data:
                for d in input_data:
                    if mandelbrot((a,b,c,d)):
                        output_data.append((b,c,d))
    return output_data

def plot(s):
    x,y,z = [],[],[]
    for i in s:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    ax = plt.axes(projection="3d")
    ax.scatter(x, y, z, color='r')
    ax.set_xlabel('X Axes')
    ax.set_ylabel('Y Axes')
    ax.set_zlabel('Z Axes')
    plt.show()

while True:
    p = eval(input("Enter the precision (1 - 5; the bigger the number, the slower the program runs): "))

    if p in range(1,6):
        try:
            plot(man_set(p))
            print("Done")
        except:
            print("ERROR: Something went wrong. Please try again.")
    else:
        print("ERROR: Invalid input. Please try again.")
