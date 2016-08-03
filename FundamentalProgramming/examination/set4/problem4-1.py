def max4in5(a, b, c, d, e):
    def max2in5(a, b, c, d, e): 
        if a < b:
            a, b = b, a
        if b < c:
            b, c = c, b
        if c < d:
            c, d = d, c
        if d < e:
            d, e = e, d
        if a < b: 
            a, b = b, a
        if b < c: 
            b, c = c, b
        if c < d:
            c, d = d, c
        return d
    return -max2in5(-a, -b, -c, -d, -e)
print max4in5(1, 4, 10, 14, 20)