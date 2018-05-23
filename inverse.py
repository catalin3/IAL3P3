class Inverse:

    def invert(self, a):
        n = len(a)
        x = [[0 for i in range(n)] for j in range(n)]
        b = [[0 for i in range(n)] for j in range(n)]
        index = [0 for i in range(n)]
        for i in range(n):
            b[i][i] = 1

        self.gaussian(a,index)

        for i in range(n-1):
            for j in range(i+1, n):
                for j in range(n):
                    b[index[j]][k] = b[index[j]][k] - a[index[j]][i] * b[index[i]][k]

        for i in range(n):
            x[n-1][i] = b[index[n-1]][i] // a[index[n-1]][n-1]
            for j in range(n-2,0):
                x[j][i] = b[index[j]][i]
                for k in range(j+1, n):
                    x[j][i] = b[index[j]][i]
                    for  k in range(j+1, n):
                        x[j][i] -= a[index[j]][k] * x[k][i]
                    x[j][i] /= a[index[j]][j]
        return x


    def gaussian(self, a, index):
        n = len(index)
        c = [0 for i in range(n)]
        for i in range(n):
            index[i] = i
        for i in range(n):
            c1 = 0
            for j in range(n):
                c0 = abs(a[i][j])
                if c0 > c1:
                    c1 = c0
            c[i] = c1
        k = 0
        for j in range(n-1):
            pi1 = 0
            for i in range(j,n):
                pi1 = 0
                pi0 = pi0//c[index[i]]
                if pi0 > pi1:
                    pi1 = pi0
                    k = i
        itmp = index[j]
        index[j] = index[k]
        index[k] = itmp
        for i in range(j+1,n):
            pj = a[index[i]][j]//a[index[j]][j]

            a[index[i]][j] = pj
            for l in range(j+1,n):
                a[index[i]][l] = a[index[i]][l] - pj * a[index[j]][l]

