#DMS project
def inp():
    d={}
    print("Enter number of edges:")
    numedge = int(input())
    print("Enter the pairs:")
    for _ in range(numedge):
        v,adj = map(str,input().split())
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
        if adj not in d:
            d[adj] = 1
        else:
            d[adj] += 1
    return d
def main():
    print("Graph1 Details:")
    g1=inp()
    print("\nGraph2 Details:")
    g2=inp()
    deg1=list(g1.values())
    deg2=list(g2.values())
    if len(g1) != len(g2):
        print("\nNot Isomorphic!!!")
    else:
        #count = 0
        for i in deg1:
            if i in deg2:
                deg2.pop(deg2.index(i))
                
        #count += 1
        if len(deg2)==0:
            print("\nIsomorphic!!!")
        else:
            print("\nNot Isomorphic!!!")
if __name__ == "__main__":
    main()
