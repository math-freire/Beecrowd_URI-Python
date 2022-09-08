def dec_to_bin(number_to_convert, binary_list):
    while number_to_convert != 0:
        if number_to_convert % 2 == 0:
            binary_list.append(0)
        else:
            binary_list.append(1)
        number_to_convert //= 2


def fill_binary_lists_equally(list1, list2):
    if len(list1) > len(list2):
        missing = len(list1) - len(list2)
        for i in range(0, missing):
            list2.append(0)
    elif len(list1) < len(list2):
        missing = len(list2) - len(list1)
        for i in range(0, missing):
            list1.append(0)


def run_code(x, y):
    x_binaryList = []
    y_binaryList = []

    # Decimal to Binary in a list
    dec_to_bin(x, x_binaryList)
    dec_to_bin(y, y_binaryList)

    # List with the same amount of positions for the binary numbers starting left to right (commented part on function)
    fill_binary_lists_equally(x_binaryList, y_binaryList)

    # print('Antes\n{}\n{}'.format(x_binaryList, y_binaryList))
    binary_res = []
    # Calculates 'Mofiz' binary code
    for i in range(0, len(x_binaryList)):
        if x_binaryList[i] == 1 and y_binaryList[i] == 0 or x_binaryList[i] == 0 and y_binaryList[i] == 1:
            binary_res.append(1)
        else:
            binary_res.append(0)

    # print('Res\n{}'.format(binary_res))
    decimal_res = 0
    for i in range(0, len(binary_res)):
        if binary_res[i] == 1:
            decimal_res += 2 ** i

    # print('Decimal results:', decimal_res)
    print(decimal_res)


# Reading entries from Beecrowd/URI
while True:
    try:
        x, y = map(int, input().split())
        run_code(x, y)
    except EOFError:
        break
