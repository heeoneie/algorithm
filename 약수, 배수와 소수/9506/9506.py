while True:
    n = int(input())
    if n == -1:
        break
    num = []
    for i in range(1,n+1):
        if n%i == 0:
            num.append(i)
    num.sort()
    num.remove(n)
    if sum(num) == n:
        string = ''
        for i in num:
            string = string +' '+str(i) +' +' #6 = 1 + 2 + 3
        string = string[:-1]
        print(str(n)+' ='+string)
    else:
        print(str(n)+" is NOT perfect.")
