import statistics as stat

def main():
    global num_list
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg_temp = calc_average()
    min_max = find_min_max()
    sorted_temp = sort_temperature()
    median_temp = calc_median_temperature()

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    global numbers
    print("get_user_input")
    numbers = input('Numbers: ')
    list1 = numbers.split(", ")
    listFloat = list(map(float, list1))

    return listFloat

def calc_average():
    print("calc_average")
    avg = sum(num_list) / len(num_list)
    print ("Average: " + str(avg))
    return avg

def find_min_max():
    print("find_min_max")
    numlist = map(float, num_list)
    min_val = min(numlist)
    numlist = map(float, num_list)
    max_val = max(numlist)
    print("Min: " + str(min_val) + " Max: " + str(max_val))
    return numlist
    
def sort_temperature():
    print("sort_temperature")
    num_list.sort()
    print("In Ascending Order: " + str(num_list))
    return num_list

def calc_median_temperature():
    print("calc_median_temperature")
    median_num = stat.median(num_list)
    print("Median: " + str(median_num))
    return median_num

if __name__ == '__main__':
        main()
