# Sampling Methods

This repo implements algorithms to sample from arbitrary probability distribtions.

### Inverse transform sampling

The main idea is to compute the CDF, draw a random number between [0,1], and then determine the point where the CDF crosses the random number.

### Rejection sampling