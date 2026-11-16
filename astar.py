import heapq
start =(1,2,3,
        4,0,6,
        7,8,5)
goal =(1,2,3,
       4,5,6,
       7,8,0)

def h(s):
    d=0
    for i,x in enumerate(s):
        if x!= 0:
            j=goal.index(x)
            d+=abs(i//3 - j//3)+ abs(i%3 -j%3)

    return d

def astar():
    pq = [(h(start),0 ,start,[])]
    visited =set()

    while pq:
        f,g,s,path = heapq.heappop(pq)

        if s in visited:
            continue

        visited.add(s)

        if s == goal :
            print ("moves",path)
            print("Total moves",g)
            return


        z=s.index(0)
        r,c = divmod(z,3)

        for dr, dc, move in [
            (-1,0,"up"), (1,0,"down"), (0,-1,"left"), (0,1,"right")
        ]:
            nr,nc =r+dr, c+dc

            if 0<= nr <3 and 0<= nc <3 :
                nz = nr*3 + nc 
                new = list(s)
                new[z],new[nz]= new[nz],new[z]

                new = tuple(new)

                if new not in visited:
                    heapq.heappush(pq,
                                   (
                                       g+1+h(new)
                                       ,g+1
                                       ,new
                                       ,path+[move]))


        print("no solution is found")  



astar()          



                
