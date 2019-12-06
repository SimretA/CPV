if __name__ == '__main__':
    lis = ["a", "b", "c"]
    # print(ord("a"))
    #print((2)%3)
    t = eval(input())
    strings = list()

    for i in range(t):
        temp = input()
        strings.append(temp)
    for string in strings:
        if len(string) <= 1 and string != "?":
            print(string)
        list_of_str = list(string)
        for i in range(len(list_of_str)):

            if i == 0 and list_of_str[i] == "?":
                if len(list_of_str) == 1:
                    next_str = 0
                elif list_of_str[i + 1] == "?":
                    next_str = 0
                else:
                    next_str = ((ord(list_of_str[i + 1]) + 1) - 97) % 3
                list_of_str[i] = lis[next_str]
            elif i < len(list_of_str) - 1 and list_of_str[i] != "?" and list_of_str[i] == list_of_str[i + 1]:
                print(-1)
                break
            elif list_of_str[i] == "?":
                next_str = ((ord(list_of_str[i - 1]) + 1) - 97) % 3
                if list_of_str[((i + 1) - len(list_of_str)) % len(list_of_str)] == lis[next_str]:
                    next_str = ((ord(list_of_str[i - 1]) + 2) - 97) % 3
                    if list_of_str[i - 1] == lis[next_str]:
                        print(-1)
                        break
                    else:
                        list_of_str[i] = lis[next_str]
                else:
                    list_of_str[i] = lis[next_str]
            if i == len(list_of_str) - 1:
                str1 = ""
                print(str1.join(list_of_str))
