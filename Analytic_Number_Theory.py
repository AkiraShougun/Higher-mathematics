class ANT:
    def prime_list(limit):
        P = [2,3]
        sieve=[False]*(limit+1)
        for x in range(1,int(limit**0.5)+1):
            for y in range(1,int(limit**0.5)+1):
                n=4*x**2+y**2
                if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
                n=3*x**2+y**2
                if n<= limit and n%12==7 : sieve[n] = not sieve[n]
                n=3*x**2-y**2
                if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
        for x in range(5,int(limit**0.5)):
            if sieve[x]:
                for y in range(x**2,limit+1,x**2):
                    sieve[y]=False
        for p in range(5,limit):
            if sieve[p] : P.append(p)
        return P
    def arithmetic_progression(x,q,a):
        li = ANT.prime_list(x)
        residue_class = []
        for p in li:
            if p % q == a:
                residue_class.append(p)
        return residue_class
    













