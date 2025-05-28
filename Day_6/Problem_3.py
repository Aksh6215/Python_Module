def count_prime(m,n):
      count = 0
      for num in range(m, n+1):
            if num > 1:
                  for i in range(2, num):
                        if (num % i) == 0:
                            break
                  else:
                        count += 1
      return count

m = int(input("m = "))
n = int(input("n = "))

prime_count = count_prime(m, n)
print(prime_count)