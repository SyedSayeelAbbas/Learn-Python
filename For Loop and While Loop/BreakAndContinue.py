lst = [1,2,3,4,5,6,7,8,9,10]
i = 0

while i < 10:
    if i == 8:   # check this first
        print("I am Breaking the loop")
        break

    if lst[i] == (i + 1):
        i += 1
        continue
    
    i += 1
