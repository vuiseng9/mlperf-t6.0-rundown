## Details for Llama31_8B on 8xGPUs, x-FP4 recipe

https://github.com/vuiseng9/mlperf-train-v6.0

is a fork of
https://github.com/mlcommons/training_results_v6.0


### 8xGPU Llama31_8B NVFP4/MXFP4
```
* Benchmark Results:
    mlperf-train-v6.0/AMD/results/MI350X_EPYC_9575F_primus/llama31_8b/result_7.txt
    mlperf-train-v6.0/AMD/results/MI355X_EPYC_9575F_primus/llama31_8b/result_9.txt
    mlperf-train-v6.0/Supermicro/results/SYS-A22GA-NBRT-8xB200_SXM/llama31_8b/result_08.txt
    mlperf-train-v6.0/HPE/results/HPE-GB200-ngpu8_ngc25.09/llama31_8b/result_10.txt
    mlperf-train-v6.0/Nebius/results/nebius_b300_n1/llama31_8b/result_06.txt
    mlperf-train-v6.0/HPE/results/HPE-GB300-ngpu8_ngc26.04/llama31_8b/result_7.txt

* Configs:
    mlperf-train-v6.0/AMD/benchmarks/llama31_8b/implementations/MI350X_EPYC_9575F_primus/config_MI350X_1x8x1.sh
    mlperf-train-v6.0/AMD/benchmarks/llama31_8b/implementations/MI355X_EPYC_9575F_primus/config_MI355X_1x8x1.sh
    mlperf-train-v6.0/Supermicro/benchmarks/llama31_8b/implementations/nemo/config_SYS-A22GA-NBRT_1x8x2xtp1pp1cp1_8b_fp4.sh
    mlperf-train-v6.0/HPE/benchmarks/llama31_8b/implementations/nemo_arm_ngc25.09/config_GB200_2x4x2xtp1pp1cp1_8b_fp4.sh
    mlperf-train-v6.0/Nebius/benchmarks/llama31_8b/configs/nebius_b300_n1/config_DGXB300_1x8x2xtp1pp1cp1_8b_fp4.sh
    mlperf-train-v6.0/HPE/benchmarks/llama31_8b/implementations/nemo_arm_ngc26.04/config_GB300_2x4x2xtp1pp1cp1_8b_fp4.sh
```

### Log Comparison Table

| Metric                |  MI350X |  MI355X |   B200 |  GB200 |   B300 |  GB300 |
|-----------------------|--------:|--------:|-------:|-------:|-------:|-------:|
| Precision             |   MXFP4 |   MXFP4 |  NVFP4 |  NVFP4 |  NVFP4 |  NVFP4 |
| Base LR               |    1e-3 |    8e-4 |   4e-4 |   4e-4 | 4.4e-4 |   4e-4 |
| Grad Accum            |       2 |       2 |      1 |      1 |      1 |      1 |
| GBS                   |      32 |      32 |     16 |     16 |     16 |     16 |
| Steps to converge     |    5760 |    5760 |  11520 |  11520 |  10752 |  10752 |
| # Trained Tokens (B)  |    1.51 |    1.51 |   1.51 |   1.51 |   1.41 |   1.41 |
| Avg Step Time (ms)    |     535 |     431 |    415 |    413 |    384 |    330 |
| Time-to-train (mins)  |   109.8 |    86.8 |   83.7 |   79.7 |   72.0 |   63.5 |

