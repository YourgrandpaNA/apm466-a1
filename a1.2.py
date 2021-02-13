""" Bootstrapping the yield curve """
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interpolate
import scipy.linalg as la

class BootstrapYieldCurve():

    def __init__(self):
        self.zero_rates = dict()
        self.instruments = dict()

    def add_instrument(self, par, T, coup, price,
                       compounding_freq=2):

        self.instruments[T] = (par, coup, price, compounding_freq)

    def get_zero_rates(self):

        self.__bootstrap_zero_coupons__()
        self.__get_bond_spot_rates__()
        return [self.zero_rates[T] for T in self.get_maturities()]

    def get_maturities(self):

        return sorted(self.instruments.keys())

    def __bootstrap_zero_coupons__(self):

        for T in self.instruments.keys():
            (par, coup, price, freq) = self.instruments[T]
            if coup == 0:
                self.zero_rates[T] = \
                    self.zero_coupon_spot_rate(par, price, T)

    def __get_bond_spot_rates__(self):

        for T in self.get_maturities():
            instrument = self.instruments[T]
            (par, coup, price, freq) = instrument

            if coup != 0:
                self.zero_rates[T] = \
                    self.__calculate_bond_spot_rate__(
                        T, instrument)

    def __calculate_bond_spot_rate__(self, T, bond):
        """ Get spot rate of a bond by bootstrapping
         period = Get input bond's maturity * coupon frequency
         value = Get input bond's price
         coupon = Get coupon per period
         for each time of coupon payments
            Y = calculate the spot rate for zero coupon bond of that time
            X = discounted_coupon calculated using Y
            Value = value minus X
         END FOR
         last_period = time to maturity for this bond
         spot_rate = calculation using bond's fair price, face value, semi-annual coupon rate and maturity with log
         RETURN spot_rate"""
        (par, coup, price, freq) = bond
        periods = T * freq
        value = price
        coupon_per_period = coup / freq

        for i in range(int(periods) - 1):
            t = (i + 1) / float(freq)
            spot_rate = self.zero_rates[t]
            discounted_coupon = coupon_per_period * math.exp(-spot_rate * t)
            value -= discounted_coupon


        last_period = int(periods) / float(freq)
        spot_rate = -math.log(value /
                              (par + coupon_per_period)) / last_period
        return spot_rate



    def zero_coupon_spot_rate(self, par, price, T):

        spot_rate = math.log(par / price) / T
        return spot_rate


def getForward(lst):
    """
    X is an empty list
    Y is 0
    while Y + 3 < number of spot rates from bonds
        find the forward rate using the corresponding bond's spot rate
        add forward rate to X
    RETURN X

    """
    ls = []
    i = 0
    while i + 3 < len(lst):
        f = (math.sqrt(pow(lst[i+3]/2 + 1, 4) / pow(1+lst[1],2)) - 1) * 2
        i += 2
        ls.append(f)
    return ls



def log_return(l):
    i = 0
    ss = []
    while i < len(l):
        ss.append(np.log(l[i+1]) - np.log(l[i]))
        i += 2
    return ss


def get_ordered_list(l):
    i = 0
    final_lst = []
    while i < 4:
        ls = []
        j = 0
        while j < len(l):
            num = l[j][i]
            ls.append(num)
            j += 1
        final_lst.append(ls)
        i += 1
    return final_lst





if __name__ == "__main__":
    yc18 = BootstrapYieldCurve()
    yc18.add_instrument(100, 0.5, 0.75, 100.4, 2)
    yc18.add_instrument(100, 1, 0.5, 100.44, 2)
    yc18.add_instrument(100, 1.5, 0.25, 100.2, 2)
    yc18.add_instrument(100, 2, 0.25, 100.13, 2)
    yc18.add_instrument(100, 2.5, 1.5, 103.13, 2)
    yc18.add_instrument(100, 3., 2.25, 106.21, 2)
    yc18.add_instrument(100, 3.5, 1.5, 104.27, 2)
    yc18.add_instrument(100, 4., 1.25, 103.6, 2)
    yc18.add_instrument(100, 4.5, 0.5, 100.33, 2)
    yc18.add_instrument(100, 5., 0.25, 98.78, 2)

    y1 = yc18.get_zero_rates()
    x1 = yc18.get_maturities()

    yc19 = BootstrapYieldCurve()
    yc19.add_instrument(100, 0.5, 0.75, 100.4, 2)
    yc19.add_instrument(100, 1, 0.5, 100.43, 2)
    yc19.add_instrument(100, 1.5, 0.25, 100.19, 2)
    yc19.add_instrument(100, 2, 0.25, 100.12, 2)
    yc19.add_instrument(100, 2.5, 1.5, 103.14, 2)
    yc19.add_instrument(100, 3., 2.25, 106.21, 2)
    yc19.add_instrument(100, 3.5, 1.5, 104.28, 2)
    yc19.add_instrument(100, 4., 1.25, 103.59, 2)
    yc19.add_instrument(100, 4.5, 0.5, 100.32, 2)
    yc19.add_instrument(100, 5., 0.25, 98.77, 2)
    y2 = yc19.get_zero_rates()
    x2 = yc19.get_maturities()

    yc20 = BootstrapYieldCurve()
    yc20.add_instrument(100, 0.5, 0.75, 100.39, 2)
    yc20.add_instrument(100, 1, 0.5, 100.41, 2)
    yc20.add_instrument(100, 1.5, 0.25, 100.16, 2)
    yc20.add_instrument(100, 2, 0.25, 100.1, 2)
    yc20.add_instrument(100, 2.5, 1.5, 103.1, 2)
    yc20.add_instrument(100, 3., 2.25, 106.17, 2)
    yc20.add_instrument(100, 3.5, 1.5, 104.25, 2)
    yc20.add_instrument(100, 4., 1.25, 103.51, 2)
    yc20.add_instrument(100, 4.5, 0.5, 100.30, 2)
    yc20.add_instrument(100, 5., 0.25, 98.76, 2)
    y3 = yc20.get_zero_rates()
    x3 = yc20.get_maturities()

    yc21 = BootstrapYieldCurve()
    yc21.add_instrument(100, 0.5, 0.75, 100.38, 2)
    yc21.add_instrument(100, 1, 0.5, 100.4, 2)
    yc21.add_instrument(100, 1.5, 0.25, 100.16, 2)
    yc21.add_instrument(100, 2, 0.25, 100.1, 2)
    yc21.add_instrument(100, 2.5, 1.5, 103.09, 2)
    yc21.add_instrument(100, 3., 2.25, 106.15, 2)
    yc21.add_instrument(100, 3.5, 1.5, 104.19, 2)
    yc21.add_instrument(100, 4., 1.25, 103.51, 2)
    yc21.add_instrument(100, 4.5, 0.5, 100.22, 2)
    yc21.add_instrument(100, 5., 0.25, 98.66, 2)
    y4 = yc21.get_zero_rates()
    x4 = yc21.get_maturities()

    yc22 = BootstrapYieldCurve()
    yc22.add_instrument(100, 0.5, 0.75, 100.38, 2)
    yc22.add_instrument(100, 1, 0.5, 100.41, 2)
    yc22.add_instrument(100, 1.5, 0.25, 100.16, 2)
    yc22.add_instrument(100, 2, 0.25, 100.1, 2)
    yc22.add_instrument(100, 2.5, 1.5, 103.09, 2)
    yc22.add_instrument(100, 3., 2.25, 106.17, 2)
    yc22.add_instrument(100, 3.5, 1.5, 104.24, 2)
    yc22.add_instrument(100, 4., 1.25, 103.54, 2)
    yc22.add_instrument(100, 4.5, 0.5, 100.27, 2)
    yc22.add_instrument(100, 5., 0.25, 98.71, 2)
    y5 = yc22.get_zero_rates()
    x5 = yc22.get_maturities()

    yc23 = BootstrapYieldCurve()
    yc23.add_instrument(100, 0.5, 0.75, 100.37, 2)
    yc23.add_instrument(100, 1, 0.5, 100.39, 2)
    yc23.add_instrument(100, 1.5, 0.25, 100.14, 2)
    yc23.add_instrument(100, 2, 0.25, 100.08, 2)
    yc23.add_instrument(100, 2.5, 1.5, 103.04, 2)
    yc23.add_instrument(100, 3., 2.25, 106.12, 2)
    yc23.add_instrument(100, 3.5, 1.5, 104.29, 2)
    yc23.add_instrument(100, 4., 1.25, 103.62, 2)
    yc23.add_instrument(100, 4.5, 0.5, 100.37, 2)
    yc23.add_instrument(100, 5., 0.25, 98.84, 2)
    y6 = yc23.get_zero_rates()
    x6 = yc23.get_maturities()

    yc24 = BootstrapYieldCurve()
    yc24.add_instrument(100, 0.5, 0.75, 100.37, 2)
    yc24.add_instrument(100, 1, 0.5, 100.39, 2)
    yc24.add_instrument(100, 1.5, 0.25, 100.15, 2)
    yc24.add_instrument(100, 2, 0.25, 100.09, 2)
    yc24.add_instrument(100, 2.5, 1.5, 103.06, 2)
    yc24.add_instrument(100, 3., 2.25, 106.18, 2)
    yc24.add_instrument(100, 3.5, 1.5, 104.26, 2)
    yc24.add_instrument(100, 4., 1.25, 103.59, 2)
    yc24.add_instrument(100, 4.5, 0.5, 100.33, 2)
    yc24.add_instrument(100, 5., 0.25, 98.83, 2)
    y7 = yc24.get_zero_rates()
    x7 = yc24.get_maturities()

    yc25 = BootstrapYieldCurve()
    yc25.add_instrument(100, 0.5, 0.75, 100.38, 2)
    yc25.add_instrument(100, 1, 0.5, 100.41, 2)
    yc25.add_instrument(100, 1.5, 0.25, 100.17, 2)
    yc25.add_instrument(100, 2, 0.25, 100.12, 2)
    yc25.add_instrument(100, 2.5, 1.5, 103.1, 2)
    yc25.add_instrument(100, 3., 2.25, 106.22, 2)
    yc25.add_instrument(100, 3.5, 1.5, 104.32, 2)
    yc25.add_instrument(100, 4., 1.25, 103.66, 2)
    yc25.add_instrument(100, 4.5, 0.5, 100.42, 2)
    yc25.add_instrument(100, 5., 0.25, 98.93, 2)
    y8 = yc25.get_zero_rates()
    x8 = yc25.get_maturities()

    yc26 = BootstrapYieldCurve()
    yc26.add_instrument(100, 0.5, 0.75, 100.37, 2)
    yc26.add_instrument(100, 1, 0.5, 100.41, 2)
    yc26.add_instrument(100, 1.5, 0.25, 100.18, 2)
    yc26.add_instrument(100, 2, 0.25, 100.12, 2)
    yc26.add_instrument(100, 2.5, 1.5, 103.08, 2)
    yc26.add_instrument(100, 3., 2.25, 106.19, 2)
    yc26.add_instrument(100, 3.5, 1.5, 104.24, 2)
    yc26.add_instrument(100, 4., 1.25, 103.61, 2)
    yc26.add_instrument(100, 4.5, 0.5, 100.35, 2)
    yc26.add_instrument(100, 5., 0.25, 98.86, 2)
    y9 = yc26.get_zero_rates()
    x9 = yc26.get_maturities()

    yc27 = BootstrapYieldCurve()
    yc27.add_instrument(100, 0.5, 0.75, 100.37, 2)
    yc27.add_instrument(100, 1, 0.5, 100.41, 2)
    yc27.add_instrument(100, 1.5, 0.25, 100.18, 2)
    yc27.add_instrument(100, 2, 0.25, 100.13, 2)
    yc27.add_instrument(100, 2.5, 1.5, 103.06, 2)
    yc27.add_instrument(100, 3., 2.25, 106.18, 2)
    yc27.add_instrument(100, 3.5, 1.5, 104.24, 2)
    yc27.add_instrument(100, 4., 1.25, 103.57, 2)
    yc27.add_instrument(100, 4.5, 0.5, 100.33, 2)
    yc27.add_instrument(100, 5., 0.25, 98.81, 2)
    y10 = yc27.get_zero_rates()
    x10 = yc27.get_maturities()

    yc28 = BootstrapYieldCurve()
    yc28.add_instrument(100, 0.5, 0.75, 100.38, 2)
    yc28.add_instrument(100, 1, 0.5, 100.42, 2)
    yc28.add_instrument(100, 1.5, 0.25, 100.19, 2)
    yc28.add_instrument(100, 2, 0.25, 100.14, 2)
    yc28.add_instrument(100, 2.5, 1.5, 103.09, 2)
    yc28.add_instrument(100, 3., 2.25, 106.21, 2)
    yc28.add_instrument(100, 3.5, 1.5, 104.27, 2)
    yc28.add_instrument(100, 4., 1.25, 103.61, 2)
    yc28.add_instrument(100, 4.5, 0.5, 100.37, 2)
    yc28.add_instrument(100, 5., 0.25, 98.86, 2)
    y11 = yc28.get_zero_rates()
    x11 = yc28.get_maturities()

    new_len = 60
    new_x = np.linspace(0,5, new_len)
    cs1 = interpolate.interp1d(x1,y1, kind = "cubic", fill_value= "extrapolate")(new_x)
    plt.plot(new_x, cs1, color = "g")
    cs2 = interpolate.interp1d(x2, y2, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs2, color="g")
    cs3 = interpolate.interp1d(x3, y3, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs3, color="g")
    cs4 = interpolate.interp1d(x4, y4, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs4, color="g")
    cs5 = interpolate.interp1d(x5, y5, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs5, color="g")
    cs6 = interpolate.interp1d(x6, y6, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs6, color="g")
    cs7 = interpolate.interp1d(x7, y7, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs7, color="g")
    cs8 = interpolate.interp1d(x8, y8, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs8, color="g")
    cs9 = interpolate.interp1d(x9, y9, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs9, color="g")
    cs10 = interpolate.interp1d(x10, y10, kind="cubic", fill_value="extrapolate")(
        new_x)
    plt.plot(new_x, cs10, color="g")

    plt.xticks(np.arange(0,5.5,0.5))
    plt.xlabel("Maturity in Years")
    plt.ylabel("Spot rate")
    plt.title("Spot curves")

    plt.show()

# 4(c)

    a = getForward(y1)
    b = getForward(y2)
    c = getForward(y3)
    d = getForward(y4)
    e = getForward(y5)
    f = getForward(y6)
    g = getForward(y7)
    h = getForward(y8)
    i = getForward(y9)
    j = getForward(y10)



    xx = np.arange(1,5,1)

    new_len = 36
    new_xx = np.linspace(2, 5, new_len)
    a1 = interpolate.interp1d(xx, a, kind="cubic", fill_value= "extrapolate")(new_xx)
    a2 = interpolate.interp1d(xx, b, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a3 = interpolate.interp1d(xx, c, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a4 = interpolate.interp1d(xx, d, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a5 = interpolate.interp1d(xx, e, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a6 = interpolate.interp1d(xx, f, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a7 = interpolate.interp1d(xx, g, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a8 = interpolate.interp1d(xx, h, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a9 = interpolate.interp1d(xx, i, kind="cubic", fill_value="extrapolate")(
        new_xx)
    a10 = interpolate.interp1d(xx, j, kind="cubic", fill_value="extrapolate")(
        new_xx)
    plt.plot(new_xx, a1)
    plt.plot(new_xx, a2)
    plt.plot(new_xx, a3)
    plt.plot(new_xx, a4)
    plt.plot(new_xx, a5)
    plt.plot(new_xx, a6)
    plt.plot(new_xx, a7)
    plt.plot(new_xx, a8)
    plt.plot(new_xx, a9)
    plt.plot(new_xx, a10)
    plt.xlabel("Maturity")
    plt.ylabel("Yield")
    plt.title("Forward curves")
    plt.show()


#5b)
    big_list = [a,b,c,d,e,f,g,h,i,j]
    sss = get_ordered_list(big_list)
    row1 = log_return(sss[0])
    row2 = log_return(sss[1])
    row3 = log_return(sss[2])
    row4 = log_return(sss[3])
    matrx = np.row_stack((row1,row2,row3,row4))
    cov = np.cov(matrx)
    print(cov)

#6
    #print(la.eig(cov))



