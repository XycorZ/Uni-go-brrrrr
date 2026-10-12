# Do not touch this line - It is just there to set up the string list from the input
# string_list will contain a list of strings that have been entered.
string_list = input("Please enter a list of numbers separated by a comma.\ne.g. Citreon,Ford,Audi,Mercedes\n").split(',')
for x in range (0,4):
    print(f"The length of the string {string_list[x]} is {str(len(string_list[x]))}.")


