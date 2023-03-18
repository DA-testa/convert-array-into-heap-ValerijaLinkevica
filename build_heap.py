# python3
import math


def build_heap(data):
    swaps = []
    size = len(data)
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)

    depth = int(math.log((size + 1), 2))

    swaps = []
    index = size - 1

    for j in range(size):
        index = size - j - 1

        if index == 0:
            break

        value = data[index]

        for i in range(depth):
            parent_index = (index - 1)//2
            parent_value = data[parent_index]

            if value < parent_value:
                temp = parent_value
                data[parent_index] = value
                data[index] = temp
            else:
                break

            pair = parent_index, index

            swaps.append(pair)

            index = parent_index

    # print(indexes)

    # for i in range(size):
    #     value = data[index - 1]

    #     parent_index = (index - 1)//2
    #     parent_value = data[parent_index]

    #     if value < parent_value:

    #         swap = parent_index, index

    #         a = data[index]
    #         b = data[parent_index]
    #         data[parent_index] = a
    #         data[index] = b

    #         swaps.append(swap)

    #     index = parent_index


    # for i in enumerate(data):
    #     print(data)
    #     index = size - i[0] - 1
    #     value = data[index - 1]

    #     parent_index = (index - 1)//2
    #     parent_value = data[parent_index]

    #     if value < parent_value:

    #         swap = parent_index, index

    #         a = data[index]
    #         b = data[parent_index]
    #         data[parent_index] = a
    #         data[index] = b

    #         swaps.append(swap)

            #for x in reversed(range(depth)):

    # print("\n", data, "\n")


    return swaps


def main():

    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file

    choice = input()

    if "F" in choice:
        filename = input()

        if "a" in filename:
            return("Incorrect file name")

        useFile = 'tests/' + filename
        file1 = open(useFile, 'r')
        lines = file1.readlines()

        n = int(lines[0])
        data = list(map(int, lines[1].split()))

    elif "I" in choice:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # swap_amount = len(swaps)
    # print(swap_amount)


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
