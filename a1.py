import scipy.optimize as optimize


def bond_ytm(price, face, maturity, coup, freq=2):

    periods = maturity * freq
    coupon = coup / 100 * face / freq
    dt = [(i + 1) / freq for i in range(int(periods))]
    ytm_func = lambda y: \
        sum([coupon / (1 + y / freq) ** (freq * t) for t in dt]) + \
        face / (1 + y / freq) ** (freq * maturity) - price

    return optimize.newton(ytm_func, 0.05)





if __name__ == "__main__":
    ytm = bond_ytm(100.2, 100, 1.5, 0.25, 2)
    print(ytm)
