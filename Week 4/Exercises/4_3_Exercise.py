ended = False
count = []
while not ended:
    val = float(input("Enter a number: "))
    count.append(val)
    if (val==0):
        if count[0]==0:
            print("No numbers, Suck yer mums")
            ended  = True
        else:
            print(f"largest = {max(count)}")
            ended = True
    else:
        continue

