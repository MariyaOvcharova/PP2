def  solve(numheads, numlegs):
    numheads = numheads * 2
    numlegs = numlegs

    ovtsa = int((numlegs - numheads)/2)
    cura = int(numheads - ovtsa)
    print(ovtsa, cura)

solve(int(input()), int(input()))
