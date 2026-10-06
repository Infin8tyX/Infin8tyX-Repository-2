""" def spaces(n, y, t):
        occupied = 0
        for i in range(n):
                if y[i] == "C" and t[i] =="C":
                        occupied = occupied+1
                        return occupied
spaces(5, "CC..C", ".CC..")
 """
 #wizard assessment example
def wizard(owner, N, duels):
    last_owner = owner
    # number of times wand changes
    changes = 0
    # check 1 single battle
    print(duels[0][0])
    for i in range(N):
        if owner == duels[i][0]:
           owner = duels[i][0]
        changes += 1
        print(owner)


        wizard("A", 3, ["BA", "CB"])