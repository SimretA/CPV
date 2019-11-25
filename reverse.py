def reverse(x: int) -> int:
    result = 0
    n_th_place = 10
    high = (2 ** 31) - 1
    low = -(2 ** 31)
    shift = 10
    mult = 1
    print("low ", result > high)
    if x < 0:
        x *= -1
        mult = -1
    while x > 0:
        result = (result * n_th_place) + x % n_th_place
        x = x // n_th_place
        shift *= 10
        print("result ", result," x ", x, " n_th ", n_th_place)
        if (result >= high) or (result <= low):
            return 0
    print("Result is ", result)
    return result*mult



if __name__ == "__main__":
    reverse(1534236469)