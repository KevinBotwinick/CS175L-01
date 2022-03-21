#CS-175-L
#Kevin Botwinick
#AverageFromInputFile


def main():
    numbers_file = open('numbers.txt', 'r')

    num1 = float(numbers_file.readline(4))
    num2 = float(numbers_file.readline(8))
    num3 = -99          


    for files in numbers_file:  
        total = num1 + num2 + num3
        x = num1+num2
        y = x+num3
        count = num1 + num2 + num3 
        average = count/3
        print(f'I read in 1 number(s) Current number is: {num1:.2f} Total is: {num1:.2f}')
        print(f'I read in 2 number(s) Current number is: {num2:.2f} Total is: {x:.2f}' )
        print(f'I read in 3 number(s) Current number is: {num3:.2f} Total is: {y:.2f}')
        print(f'Average: {average}')

    numbers_file.close()
if __name__ == '__main__':
    main()
