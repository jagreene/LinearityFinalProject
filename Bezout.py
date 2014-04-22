def bezout(a, b):
    """
    Bezout coefficients (u,v) of (a,b) as:

        a * u + b * v = gcd(a,b)

    Result is the tuple: (u, v, gcd(a,b)). Examples:

    >>> bezout(2*3, 3*5)
    (-2, 1, 3)
    >>> bezout(65539, 2147483648)
    (477211307, -14564, 1)
    """
    u0, u1 = 1, 0
    v0, v1 = 0, 1

    while 1:
        q, r = divmod(a, b)

        u0, u1 = u1, u0 - q*u1
        v0, v1 = v1, v0 - q*v1

        if r != 0:
            a = b
            b = r
        else:
            break
    return (u0, v0, b)