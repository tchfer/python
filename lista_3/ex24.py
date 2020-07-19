# for c in range(2, 10):
#     m = 0
#     while m <= 10:
#         print("{} x {:2} = {:2}".format(c, m, c*m))
#         m += 1
#     print("-" * 15)

n = 1
while n <= 9:
    n += 1
    r = 0
    while r <= 10:
        print("{:2} X {:2} = {:3}".format(n, r, n * r))
        r +=1
    print()
