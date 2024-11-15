# Implementation of Shamir Secret Sharing Scheme

import random
from math import ceil
from decimal import *

global field_size
field_size = 10 ** 5


def reconstructSecret(shares):
    # Combines shares using
    # Lagranges interpolation.
    # Shares is an array of shares
    # being combined
    sums, prod_arr = 0, []

    for j in range(len(shares)):
        xj, yj = shares[j][0], shares[j][1]
        prod = Decimal(1)

        for i in range(len(shares)):
            xi = shares[i][0]
            if i != j: prod *= Decimal(Decimal(xi) / (xi - xj))

        prod *= yj
        sums += Decimal(prod)

    return int(round(Decimal(sums), 0))


def polynom(x, coeff):
    # Evaluates a polynomial in x
    # with coeff being the coefficient
    # list
    return sum([x ** (len(coeff) - i - 1) * coeff[i] for i in range(len(coeff))])


def coeff(t, secret):
    # Randomly generate a coefficient
    # array for a polynomial with
    # degree t-1 whose constant = secret'''
    coeff = [random.randrange(0, field_size) for _ in range(t - 1)]
    coeff.append(secret)

    return coeff


def generateShares(n, m, secret):
    # Split secret using SSS into
    # n shares with threshold m
    cfs = coeff(m, secret)
    shares = []

    for i in range(1, n + 1):
        r = random.randrange(1, field_size)
        shares.append([r, polynom(r, cfs)])

    return shares


# Driver code
if __name__ == '__main__':
    # (3,5) sharing scheme
    t, n = 3, 5
    secret = 1234
    print('Original Secret:', secret)

    # Phase I: Generation of shares
    shares = generateShares(n, t, secret)
    print('\nShares:', *shares)

    # Phase II: Secret Reconstruction
    # Picking t shares randomly for
    # reconstruction
    pool = random.sample(shares, t)
    print('\nCombining shares:', *pool)
    print("Reconstructed secret:", reconstructSecret(pool))
