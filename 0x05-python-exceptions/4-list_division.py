#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor != 0:
                    division_result = dividend / divisor
                else:
                    division_result = 0
            else:
                print("wrong type")
                division_result = 0
        except IndexError:
            print("out of range")
            division_result = 0
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        finally:
            result.append(division_result)
    return result


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
