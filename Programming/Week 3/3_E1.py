#0-5=0%
#5-9=10
#9-19=20
#20-49=30
#50-99=40
#100+=50
#99 per can

copies = int(input("Enter number of cans: "))
total = 99*copies

discount=[0,0.1,0.2,0.3,0.4,0.5]

if copies < 5:
    print(f"Your cans give u a {discount[0]*100}& total = {total-total*discount[0]:.2f}")
elif 5<=copies<=9:
    print(f"Your cans give u a {discount[1]*100}& total = {total-total*discount[1]:.2f}")
elif 10<=copies<=19:
    print(f"Your cans give u a {discount[2]*100}& total = {total-total*discount[2]:.2f}")
elif 20<=copies<=29:
    print(f"Your cans give u a {discount[3]*100}& total = {total-total*discount[3]:.2f}")
elif 30<=copies<=49:
    print(f"Your cans give u a {discount[4]*100}& total = {total-total*discount[4]:.2f}")
elif 50<=copies<=99:
    print(f"Your cans give u a {discount[5]*100}& total = {total-total*discount[5]:.2f}")
elif copies<=100:
    print(f"Your cans give u a {discount[6]*100}& total = {total-total*discount[6]:.2f}")
