print(*[i**2 for i in range(1, int(input())+1)], sep='\n')

palindromes = [c for c in range(100,1001) if str(c)[0]==str(c)[-1]]

print(palindromes)