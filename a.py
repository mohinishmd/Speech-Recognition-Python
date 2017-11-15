a = input();
i = 0;
while i < a:
    n,k =map(int, raw_input().split())
    r = ((k-1)**(n-1))*k
    r = r % 1000000007
    print r
    print '\n'
    i += 1
