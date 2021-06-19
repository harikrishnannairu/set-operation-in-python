if __name__ == '__main__':
    m=int(input())
    sm=set(map(int,input().split()))
    n=int(input())
    sn=set(map(int,input().split()))
    union=set()
    intersection=set()
    union=sm.union(sn)
    intersection=sm.intersection(sn)
    r=union.difference(intersection)
    sr=sorted(list(r))
    for i in sr:
        print(i)
