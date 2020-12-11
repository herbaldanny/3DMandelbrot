import math as m

while True:
    def size(h):
        return m.sqrt(h[0] ** 2 + h[1] ** 2 + h[2] ** 2 + h[3] ** 2)

    def qsquare(h):
        new_0 = h[0] ** 2 - h[1] ** 2 - h[2] ** 2 - h[3] ** 2
        new_1 = 2 * h[0] * h[1]
        new_2 = 2 * h[0] * h[2]
        new_3 = 2 * h[0] * h[3]
        return (new_0,new_1,new_2,new_3)

    def main(h,c):
        return tuple(map(lambda i, j: i + j, qsquare(h), c))

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
                            output_data.append((a,b,c,d))
        return output_data

    p = eval(input("Enter the precision (1 - 5; the bigger the number, the slower the program runs): "))

    if p in range(1,6):
        print(man_set(p))
    else:
        print("ERROR: Invalid input. Please try again.")