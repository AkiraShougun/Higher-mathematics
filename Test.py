from Analytic_Number_Theory import ANT


def main():
    limiter = int(input("Input the limit: "))
    pi_1mod4 = ANT.arithmetic_progression(limiter,4,1)
    pi_3mod4 = ANT.arithmetic_progression(limiter,4,3)
    pi_2mod4 = ANT.arithmetic_progression(limiter,4,2)
    primes = ANT.prime_list(limiter)

    print(f"Sum of all modulo 4: {len(pi_1mod4)+len(pi_2mod4)+len(pi_3mod4)}")
    print(f"Regular primes: {len(primes)}")

if __name__ == "__main__":
    main()




    


