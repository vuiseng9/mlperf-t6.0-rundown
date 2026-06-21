## Details for DeepSeek-v3

1. Each sample uses a sequence length of 4,096 tokens.
2. Most runs converged to the target within 45–49 optimizer steps, corresponding to roughly 3B training tokens.
3. This is largely a strong-scaling case: the global tokens per optimizer step, GBS × SeqLen, are kept approximately constant while the GPU count increases.
4. Instead of calculating scaling efficiency for every pair of data points, we fit log-linear for respectively for GB200 and GB300. We use the fitted coefficient to calculate the overall scaling efficiency as follows.

    We fit time-to-train with a log-linear model:

    $$
    \log(t) = a \log(n) + b
    $$

    This is equivalent to a power-law form:

    $$
    t(n) = \exp(b) \cdot n^a
    $$

    or:

    $$
    t(n) = c n^a
    $$

    where: 
    - $n$: number of GPUs
    - $t(n)$: time-to-train
    - $a$: fitted scaling exponent
    - $c = \exp(b)$

    For GPU doubling, from $n$ to $2n$ gpus:

    $$
    t(n) = c n^a
    $$

    $$
    t(2n) = c(2n)^a
    $$

    Observed/Predicted speedup:

    $$
    \text{speedup} = \frac{t(n)}{t(2n)}
    $$

    $$
    = \frac{c n^a}{c(2n)^a}
    $$

    $$
    = \frac{1}{2^a}
    $$

    Ideal speedup for doubling GPUs is:

    $$
    2
    $$

    So scaling efficiency per GPU doubling is:

    $$
    \text{efficiency}
    = \frac{\text{observed speedup}}{\text{ideal speedup}}
    $$

    $$
    = \frac{1 / 2^a}{2}
    $$

    $$
    = 2^{-a - 1}
    $$

5. [Coded](./assets/dsv3_fit_loglinear.py) the above fit, **GB200 lands at 85.45% scaling efficiency**, while **GB300 reaches 88.16%**.

|                             |                |                |                |                |                |
|-----------------------------|---------------:|---------------:|---------------:|---------------:|---------------:|
| **#GPU (GB200)**            |                |            512 |           2048 |           4096 |           8192 |
| # Node                      |                |            128 |            512 |           1024 |           2048 |
| TP / PP / EP / CP           |                | 2 / 4 / 32 / 1 | 2 / 4 / 32 / 1 | 2 / 4 / 32 / 1 | 2 / 4 / 32 / 1 |
| Global Batch Size (GBS)     |                |         15,360 |         15,360 |         16,384 |         16,384 |
| # Trained Tokens            |                |         3.020B |         3.083B |         3.154B |         3.020B |
| Gradient Accum. Steps       |                |            240 |             60 |             32 |             16 |
| Micro Batch Size (MBS)      |                |             64 |            256 |            512 |           1024 |
| Steps-to-converge           |                |             48 |             49 |             47 |             45 |
| Avg Step Time (s)           |                |          33.34 |           9.03 |           5.54 |           3.54 |
| Time-to-train (mins)        |                |          27.61 |           7.84 |           4.83 |           3.34 |
|                             |                |                |                |                |                |
| **#GPU (GB300)**            |            256 |            512 |           2048 |           4096 |           8192 |
| # Node                      |            128 |            128 |            512 |           1024 |           2048 |
| TP / PP / EP / CP           | 1 / 4 / 32 / 1 | 1 / 4 / 32 / 1 | 1 / 4 / 32 / 1 | 1 / 4 / 32 / 1 | 1 / 4 / 32 / 1 |
| Global Batch Size (GBS)     |         15,360 |         15,360 |         16,384 |         16,384 |         16,384 |
| # Trained Tokens            |         3.083B |         3.083B |         3.154B |         3.020B |         3.020B |
| Gradient Accum. Steps       |            240 |            120 |             32 |             16 |              8 |
| Micro Batch Size (MBS)      |             64 |            128 |            512 |           1024 |           2048 |
| Steps-to-converge           |             49 |             49 |             47 |             45 |             45 |
| Avg Step Time (s)           |          39.51 |          20.21 |           7.11 |           3.32 |           1.91 |
| Time-to-train (mins)        |          33.43 |          17.52 |           5.54 |           3.09 |           2.02 |


**Note: MBS here is a total over all DP. TODO: figure out in-flight #MBS per DP.**


https://github.com/vuiseng9/mlperf-train-v6.0

is a fork of
https://github.com/mlcommons/training_results_v6.0

### GB200 NVL72 (tyche-hsg)
```
* Benchmark Results:
    mlperf-train-v6.0/NVIDIA/results/
        tyche-hsg_ngpu512_ngc26.04_nemo/deepseekv3_671b/result_2.txt
        tyche-hsg_ngpu2048_ngc26.04_nemo/deepseekv3_671b/result_1.txt
        tyche-hsg_ngpu4096_ngc26.04_nemo/deepseekv3_671b/result_0.txt
        tyche-hsg_ngpu8192_ngc26.04_nemo/deepseekv3_671b/result_1.txt

* Configs:
    mlperf-train-v6.0/NVIDIA/benchmarks/deepseekv3_671b/implementations
        tyche-hsg_ngpu512_ngc26.04_nemo/config_GB200_128x4x240xtp2pp4ep32cp1_mxfp8_full_cg.sh
        tyche-hsg_ngpu2048_ngc26.04_nemo/config_GB200_512x4x60xtp2pp4ep32cp1_mxfp8_full_cg.sh
        tyche-hsg_ngpu4096_ngc26.04_nemo/config_GB200_1024x4x32xtp2pp4ep32cp1_mxfp8_full_cg.sh
        tyche-hsg_ngpu8192_ngc26.04_nemo/config_GB200_2048x4x16xtp2pp4ep32cp1_mxfp8_full_cg.sh
```

### GB300 NVL72 (theia, coreweave)
```
* Benchmark Results:
    mlperf-train-v6.0/NVIDIA/results/
        theia_ngpu256_ngc26.04_nemo/deepseekv3_671b/result_1.txt
        theia_ngpu512_ngc26.04_nemo/deepseekv3_671b/result_2.txt
    mlperf-train-v6.0/CoreWeave/results/
        CoreWeave_GB300_512x4/deepseekv3_671b/result_2.txt
        CoreWeave_GB300_1024x4/deepseekv3_671b/result_0.txt
        CoreWeave_GB300_2048x4/deepseekv3_671b/result_1.txt

* Configs:
    mlperf-train-v6.0/NVIDIA/benchmarks/deepseekv3_671b/implementations/
        theia_ngpu256_ngc26.04_nemo/config_GB300_64x4x240xtp1pp4ep32cp1_mxfp8_full_cg.sh
        theia_ngpu512_ngc26.04_nemo/config_GB300_128x4x120xtp1pp4ep32cp1_mxfp8_full_cg.sh
    mlperf-train-v6.0/CoreWeave/benchmarks/deepseekv3_671b/implementations/
        CoreWeave_GB300_512x4/config_GB300_512x4x32xtp1pp4ep32cp1_mxfp8_full_cg.sh
        CoreWeave_GB300_1024x4/config_GB300_1024x4x16xtp1pp4ep32cp1_mxfp8_full_cg.sh
        CoreWeave_GB300_2048x4/config_GB300_2048x4x8xtp1pp4ep32cp1_mxfp8_full_cg.sh
```