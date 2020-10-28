M=[[1,2,3],
   [4,5,6],
   [7,8,9]]

diag=[M[i][i] for i in [0,1,2]]
print(diag)

G=(sum(row) for row in M)

print(next(G))
print(next(G))
print(next(G))

print(list(map(sum,M)))

ord_=[ord(x) for x in 'spaam']
print(ord_)