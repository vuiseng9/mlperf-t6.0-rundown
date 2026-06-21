import numpy as np

# Time-to-train data
gb200_gpus = np.array([512, 2048, 4096, 8192], dtype=float)
gb200_time = np.array([27.61, 7.84, 4.83, 3.34], dtype=float)

gb300_gpus = np.array([256, 512, 2048, 4096, 8192], dtype=float)
gb300_time = np.array([33.43, 17.52, 5.54, 3.09, 2.02], dtype=float)


def fit_log_linear(name, gpus, time):
    """
    Fit: 
        log(t) = alog(n) + b

    equivalent to:
        t(n) = exp(b) * n^a
        t(n) = cn^a

    return a
    """
    x = np.log(gpus)
    y = np.log(time)

    a, b = np.polyfit(x, y, deg=1)
    return a

def calc_efficiency(a):
    """
    eff = observed speedup / ideal speedup
    ideal doubling speedup means scale from n to 2n

    ideal speedup = 2

    observed speedup = T1/T2 = (cn^a) / (c(2n)^a) = 1 / 2^a
    
    eff = ( 1 / 2^a ) / 2 
        = 2^-a / 2
        = 2^(-a - 1)
    """
    return 2 ** (-a - 1)

gb200_a = fit_log_linear("GB200", gb200_gpus, gb200_time)
gb300_a = fit_log_linear("GB300", gb300_gpus, gb300_time)

print(f"GB200 a: {gb200_a:.4f}, efficiency: {calc_efficiency(gb200_a):.4f}")
print(f"GB300 a: {gb300_a:.4f}, efficiency: {calc_efficiency(gb300_a):.4f}")
