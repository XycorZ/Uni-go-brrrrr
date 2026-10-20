import sys

def calc_retail_price(whole,mark):
    # remove the following line and write your function here
    mark_decimal = mark/100
    whole = whole * (1+mark_decimal)
    result =  f"The retail price is £{whole:.2f}.\n"
    return result

def main():
    # remove the following line and write your main program here
    wholesale = float(input("Please enter a wholesale cost:\n"))
    markup = float(input("Please enter a markup percentage:\n"))
    calc_retail_price(wholesale,markup)   


# This is needed for the tests. This is now the first bit of code Python will run.
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
    #main() # calls the main function
    
    # uncomment the following lines to test calc_retail_price when you run the program.You will need to comment out main()
    print(calc_retail_price(3.00, 100)) # should print 6.0
    print(calc_retail_price(5.00, 50))# should print 7.5