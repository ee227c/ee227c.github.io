# assumes ee227c environment is set up

import autograd.numpy as np
from autograd import grad
import matplotlib
matplotlib.use('Agg')
# flake8: noqa pylint: disable=wrong-import-position
import matplotlib.pyplot as plt

# https://blogs.princeton.edu/imabandit/2013/04/01/acceleratedgradientdescent/


def gd(x0, beta, df, steps):
    xs = [x0]
    x = x0
    for _ in range(steps):
        x = x - df(x) / beta
        xs.append(x)
    return xs


def nesterov(x0, beta, df, steps):
    xs = [x0]
    x = y = x0
    # l, g are lambda, gamma from the post ; ll, gg are the next iterates
    l = 1
    for _ in range(steps):
        ll = (1 + np.sqrt(1 + 4 * l * l)) / 2
        g = (1 - l) / ll
        l = ll
        yy = x - df(x) / beta
        x = (1 - g) * yy + g * y
        y = yy
        xs.append(x)
    return xs


beta = 1


def f(x):
    chain_laplacian = np.square(x[:-1] - x[1:]).sum()
    chain_laplacian += x[0] ** 2
    chain_laplacian += x[-1] ** 2
    chain_laplacian *= beta / 8
    return chain_laplacian - x[0] * beta / 4


df = grad(f)
n = 100
delta = 0.1


def sample_ball():
    v = np.random.randn(n)
    v /= np.linalg.norm(v)
    return v


def noisy_df(x):
    return sample_ball() * delta + df(x)


its = 100
samples = 100
gd_xs = gd(np.zeros(n), beta, df, its)
ad_xs = nesterov(np.zeros(n), beta, df, its)
xopt = np.ones(n) - (1 + np.arange(n)) / (n + 1)
gd_fs = [f(x) - f(xopt) for x in gd_xs]
ad_fs = [f(x) - f(xopt) for x in ad_xs]


def resample(gen):

    total = 0
    for _ in range(samples):
        total += np.array([f(x) - f(xopt) for x in gen()])
    return total / samples


noisy_gd_fs = resample(lambda: gd(np.zeros(n), beta, noisy_df, its))
noisy_ad_fs = resample(lambda: nesterov(np.zeros(n), beta, noisy_df, its))


plt.semilogy(gd_fs, label='gd', color='r')
plt.semilogy(ad_fs, label='nag', color='b')
plt.semilogy(noisy_gd_fs, label='noisy gd', color='r', ls='--')
plt.semilogy(noisy_ad_fs, label='noisy nag', color='b', ls='--')
plt.title('suboptimality (dimension = {}, noise = {}, trials = {})'
          .format(n, delta, samples))
plt.xlabel('iterate')
plt.legend(loc='best')
plt.savefig('figures/nag-noise.pdf', format='pdf', bbox_inches='tight')

print('generated plot in figures/nag-noise.pdf')
