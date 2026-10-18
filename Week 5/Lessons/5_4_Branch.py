def print_list(numbers=None, multiple = 1):
    if numbers is None:
        numbers=[]
    for x in range(0,len(numbers)):    
        numbers[x] = numbers[x]*multiple
        print(f"{numbers[x]}")

if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])
