number0 = [['*', '*', '*'], ['*', ' ', '*'], ['*', ' ', '*'], ['*', ' ', '*'], ['*', '*', '*']]
number1 = [[' ', '*'], ['*', '*'], [' ', '*'], [' ', '*'], [' ', '*']]
number2 = [['*', '*', '*', ], [' ', ' ', '*'], ['*', '*', '*'], ['*', ' ', ' '], ['*', '*', '*']]
number3 = [['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']]
number4 = [['*', ' ', '*'], ['*', ' ', '*'], ['*', '*', '*'], [' ', ' ', '*'], [' ', ' ', '*']]
number5 = [['*', '*', '*', ], ['*', ' ', ' '], ['*', '*', '*'], [' ', ' ', '*'], ['*', '*', '*']]
number6 = [['*', '*', '*', ], ['*', ' ', ' '], ['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
number7 = [['*', '*', '*', ], [' ', ' ', '*'], [' ', '*', ' '], [' ', '*', ' '], [' ', '*', ' '], ]
number8 = [['*', '*', '*', ], ['*', ' ', '*', ], ['*', '*', '*', ], ['*', ' ', '*', ], ['*', '*', '*', ]]
number9 = [['*', '*', '*', ], ['*', ' ', '*', ], ['*', '*', '*', ], [' ', ' ', '*', ], ['*', '*', '*', ]]

numbers = [number0, number1, number2, number3, number4, number5, number6, number7, number8, number9]


def EnterNum() -> str:
    num = input("Enter number in range 0 - 9999: ")
    while not num.isdigit():
        num = input("U entered not a digit. Enter number in range 0 - 9999: ")
    return num


def PrintNum(n: str):
    for i in range(5):
        if len(n) == 1:
            print(*numbers[int(n[0])][i], end='   ')
        elif len(n) == 2:
            print(*numbers[int(n[0])][i], end='   ')
            print(*numbers[int(n[1])][i])
        elif len(n) == 3:
            print(*numbers[int(n[0])][i], end='   ')
            print(*numbers[int(n[1])][i], end='   ')
            print(*numbers[int(n[2])][i])
        elif len(n) == 4:
            print(*numbers[int(n[0])][i], end='   ')
            print(*numbers[int(n[1])][i], end='   ')
            print(*numbers[int(n[2])][i], end='   ')
            print(*numbers[int(n[3])][i])


def ChangeSymb(ch: str):
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            for k in range(len(numbers[i][j])):
                if numbers[i][j][k] != ' ':
                    numbers[i][j][k] = ch


def main():
      num = EnterNum()
      PrintNum(num)
      continue_flag = True
      while continue_flag:
          question = input("Do u like to continue? (Y/n): ")
          if question.lower() == 'y':
              num = EnterNum()
              symb = input('Enter symbol: ')[0]
              ChangeSymb(symb)
              PrintNum(num)
          else:
              continue_flag = False


if __name__ == '__main__':
    main()
