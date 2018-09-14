from random import uniform 

def weighter(lister):
    total = 0.0
    for nums in lister:
        total += nums
    chosen = uniform(0,total)
    count = 0
    wcount = 0
    for weight in lister:
        wcount += weight
        if wcount >= chosen:
            return lister[count]
        else:
            count += 1

tested = [0.5,6.2,10.3]

def tester(lister, trials):
    total = 0.0
    dicto = {}
    for nums in lister:
        total += nums
        dicto[nums] = 0
    for x in range(0,trials):
        dicto[weighter(tested)] += 1
    for y in lister:
        print(str(y) + " : " + str((dicto[y] / (trials) * total)))
    
    

tester(tested, 10000000)
        

    
