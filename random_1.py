numOld = 0
def rand(min , max):
    global numOld
    if numOld >= max: numOld = 0
    set_old = {str(x) for x in range(int(numOld)+1)}
    set_old_t = {str(x) for x in range(int(tuple(set_old)[0])) if x < max}
    if len(set_old_t) > 0: set_old_t_2 = int(tuple(set_old_t)[0])
    else: set_old_t_2 = 0
    set_r = {str(x) for x in range(max-set_old_t_2) if x >= min}
    numRand = int(tuple(set_r)[0])
    if len(set_r) > 1: numOld += len(str(numRand))
    else: numOld += int(set_r[1])
    # clear ram
    del set_old, set_old_t , set_old_t_2
    return numRand
def random_range(min, max, repeat):
    mySet = set({}); i = 0
    while i <= repeat: 
        try: mySet.add(rand(min,max)); i += 1
        except: numOld = 0; i += 1
    # clear ram
    del i
    return list(mySet)
myRand = random_range(100,200,100)
print("Trong 100 lần rand được ",len(myRand)," số riêng biệt!")
for x in myRand:
    print(x)
