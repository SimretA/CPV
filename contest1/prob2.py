if __name__ == '__main__':
    t = eval(input())
    list_of_perm = list()
    list_of_list = list()
    for i in range(t):
        temp = eval(input())
        list_of_perm.append(temp)
        temp = input()
        temp = temp.split(" ")
        list_of_list.append(temp)
    for list1 in list_of_list:

        length = len(list1)

        for i in range(length):
            list1[i] = eval(list1[i])
        result = [0] * length

        for i in range(length):
            beautiful = 1
            if list1[i] == 1:
                result[list1[i]-1] = 1
                break
            if i == 0:
                temp = list1[i: list1[i]]
                temp = sorted(temp)
                print(temp)
                for j in range(len(temp)):
                    if temp[j] != j+1:
                        beautiful= 0
                result[list1[i]-1] = beautiful
            else:
                indx = []
                for j in range(1, list1[i]):
                    indx.append(abs(list1.index(j) - i))
                #print("for ", list1[i], indx)
                indx = sorted(indx)
                for j in range(len(indx)):
                    if indx[j] != j+1:
                        beautiful = 0
                result[list1[i]-1] = beautiful
        print(result)
