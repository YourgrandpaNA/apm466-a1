4a)
y = c(0.06,0.09,0.12,0.18,0.26,0.23,0.3,0.36,0.43,0.49)
y19th = c(0.06, 0.1, 0.12, 0.19, 0.25, 0.23, 0.3, 0.36, 0.43, 0.5)
y20th = c(0.08, 0.12, 0.14,0.2, 0.27, 0.24, 0.31, 0.38, 0.43, 0.5)
y21th = c(0.1, 0.13, 0.14, 0.2, 0.27, 0.25, 0.32, 0.38, 0.45, 0.52)
y22th = c(0.1, 0.12, 0.14, 0.2, 0.27, 0.24, 0.31, 0.38, 0.44, 0.51)
y23th = c(0.12, 0.14, 0.16 , 0.15, 0.29, 0.26, 0.3, 0.36, 0.42, 0.48)
y24th = c(0.12, 0.14, 0.15, 0.2, 0.28,0.24, 0.3, 0.36, 0.43, 0.48)
y25th = c(0.1, 0.12, 0.14, 0.19, 0.27, 0.22, 0.29, 0.35, 0.41, 0.46)
y26th = c(0.12, 0.12, 0.13, 0.19, 0.28, 0.23, 0.31, 0.36, 0.42, 0.48)
y27th = c(0.12, 0.12, 0.13, 0.18, 0.28,0.24, 0.31, 0.37, 0.43, 0.49)
y28th = c(0.1, 0.11, 0.12, 0.18, 0.27,0.23, 0.3, 0.36, 0.42, 0.48)
x = c(6,12,18,24,30,36,42,48,52,58)

plot(x, y,type = "b", xaxt = "n" , xlab = "Months to Maturity")
lines(x, y19th , type = "b")
lines(x, y20th, type = "b")
lines(x, y21th, type = "b")
lines(x, y22th, type = "b")
lines(x, y23th, type = "b")
lines(x, y24th, type = "b")
lines(x, y25th, type = "b")
lines(x, y26th, type = "b")
lines(x, y27th, type = "b")
lines(x, y28th, type = "b")
axis(1, at=seq(6,64, by = 6))


