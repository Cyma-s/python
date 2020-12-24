x = input()
n = int(x)

for i in range(n, -1, -1) :
    if i > 1 :
        print("%d bottles of beer on the wall, %d bottles of beer.\n" %(i, i))
        if i == 2 :
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("Take one down and pass it around, %d bottles of beer on the wall.\n" % (i-1))
        #print("\n")
    elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.\n")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        #print("\n")
    elif i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.\n")
        if n != 1 :
            print("Go to the store and buy some more, %d bottles of beer on the wall." % n)
        elif n == 1 :
            print("Go to the store and buy some more, 1 bottle of beer on the wall.")