ended = False
avg = 0
count = 0
while not ended:
    val = float(input("Enter a number: "))
    if(val==0):
        if (avg ==0):
            print("No numbers")
            break
        else:    
            print(f"Avg: {avg/count}")
            ended = True
    else:
        avg+=val
        count+=1

