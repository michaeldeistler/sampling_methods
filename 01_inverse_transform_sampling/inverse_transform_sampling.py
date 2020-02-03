import numpy as np
import numpy.random

def it_sampling(density, num_samples=100, x_start=-5, x_end=5, x_intervals=1000):
    x_vec    = np.linspace(x_start, x_end, x_intervals)

    density_vals = density.evaluate(point=x_vec)
    cdf_vals = np.cumsum(density_vals)
    cdf_vals = cdf_vals / np.max(cdf_vals)

    base_samples  = np.random.rand(num_samples)
    tiled_cdf     = np.tile(cdf_vals, (num_samples, 1))
    tiled_samples = np.tile(base_samples, (x_intervals, 1))

    dist_func = np.abs(tiled_samples - tiled_cdf.T)
    min_index = np.argmin(dist_func, axis=0)

    samples   = x_vec[min_index]

    return samples