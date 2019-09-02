class Matrix:

    def __init__(self, m, n, end= " "):
        self.m = m
        self.n = n

    def mul(self):
        res = []

        for i in range(len(self.m)):
            res.append([])
            for j in range(len(self.n[0])):
                res[i].append(0)

        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                res[i][j]=0
                for k in range(len(self.n)):
                    res[i][j]+= self.m[i][k] *  self.n[k][j]
        for  i in range(len(res)):
            for j in range(len(res[0])):
                print(res[i][j], end =" ")
            print()
A = [
        [12,23,42],
        [45,56,77],
        [10,20,30]
    ]

B = [
        [20,56,43], 
        [3,23,90],
        [1, 2, 3]
    ]
obj = Matrix(m=A, n=B)
obj.mul()
print()


