
def measurements():
    x_axis = int(input('What is the first measurement? '))
    y_axis = int(input('What is the second measurement? '))
    def perimeter():
        peri = x_axis + y_axis
        print('The perimeter is ', peri)
    def area():
        fifty_one = x_axis * y_axis
        print('The area is ', fifty_one)

if __name__ == '__main__':
    measurements()