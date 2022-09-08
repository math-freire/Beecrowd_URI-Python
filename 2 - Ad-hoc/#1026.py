def dec_to_bin(number_to_convert, binary_list):
    while number_to_convert != 0:
        if number_to_convert % 2 == 0:
            binary_list.append(0)
        elif number_to_convert % 2 != 0:
            binary_list.append(1)
        number_to_convert //= 2


def fill_binary_list(binary_list):
    missing = 32 - len(binary_list)
    for i in range(0, missing):
        binary_list.append(0)
    #  binary_list.reverse()


def run_code(x, y):
    x_binaryList = []
    y_binaryList = []

    # Decimal to Binary in a list
    dec_to_bin(x, x_binaryList)
    dec_to_bin(y, y_binaryList)

    # List with 32 positions of the binary number starting left to right (commented part on function)
    fill_binary_list(x_binaryList)
    fill_binary_list(y_binaryList)

    # print('Antes\n{}\n{}'.format(x_binaryList, y_binaryList))

    # Creates a list for keeping the binary results and fills it with 0 (zeros)
    binary_res = []
    fill_binary_list(binary_res)

    # Calculates 'Mofiz' binary code
    for i in range(0, 32):
        if x_binaryList[i] == 1 and y_binaryList[i] == 1:
            binary_res[i] = 0
        elif x_binaryList[i] == 1 and y_binaryList[i] == 0 or x_binaryList[i] == 0 and y_binaryList[i] == 1:
            binary_res[i] = 1
        # If it's 0 and 0, nothing changes.

    # print('Res\n{}'.format(binary_res))
    decimal_res = 0

    for i in range(0, 32):
        if binary_res[i] == 1:
            decimal_res += pow(2, i)

    # print('Decimal results:', decimal_res)
    print(decimal_res)


# Reading entries from Beecrowd/URI
while True:
    try:
        x, y = map(int, input().split())
        run_code(x, y)
    except EOFError:
        break
