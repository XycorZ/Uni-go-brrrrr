def odd_test(x):
    if x%2!=0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(odd_test(3))     # should output True
    print(odd_test(8))     # should output False

