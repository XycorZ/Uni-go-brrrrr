speed = float(input("Miles per hours: "))
hours = int(input("Hours travelled  "))

if (hours<0):
    print("Error: Suck Yur Mum")
elif (speed<0):
    print("Error: Suck Yur Mum more")
else:
    print("Hour | Distance")
    print("--------------------------")
    for x in range (0,hours+1):
        print(f"{x}    | {speed * x}")