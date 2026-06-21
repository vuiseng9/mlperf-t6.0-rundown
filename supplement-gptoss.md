## GPT-OSS Details

1. Each sample uses a sequence length of 8192 tokens.
2. Parallelism mappings change by large degree when scaling to more gpus, resulting more differences in global batch size, number of steps to converge, total tokens to converge.


| #GPU (GB300)                  |      4 |     8 |    16 |    32 |    72 |   512 |
|:------------------------------|-------:|------:|------:|------:|------:|------:|
| TP                            |      1 |     1 |     1 |     1 |     1 |     2 |
| PP                            |      1 |     1 |     1 |     1 |     1 |     1 |
| CP                            |      1 |     1 |     1 |     1 |     2 |     4 |
| EP                            |      1 |     1 |     1 |     1 |     4 |     8 |
| DP = #GPUs/(TP×PP×CP)         |      4 |     8 |    16 |    32 |    36 |    64 |
| Micro Batch Size (MBS)        |      2 |     3 |     2 |     2 |     1 |     1 |
| Grad Accumulation             |      2 |     1 |     1 |     1 |     1 |     1 |
| Global Batch Size             |     16 |    24 |    32 |    64 |    36 |    64 |
| Steps-to-converge             | 13,056 | 8,704 | 7,168 | 4,608 | 6,138 | 4,608 |
| # trained tokens (B)          |    1.7 |   1.7 |   1.9 |   2.4 |   1.8 |   2.4 |
| Avg step time (ms)            |  697.4 |   490 | 354.1 | 351.7 | 160.7 |    91 |
| Time-to-train (mins)          |  152.7 |  74.1 |  43.2 |  27.9 |  18.3 |   7.4 |


https://github.com/vuiseng9/mlperf-train-v6.0

is a fork of
https://github.com/mlcommons/training_results_v6.0

### GB300 NVL72 (Nvidia Theia/HPE/Dell)
```
* Benchmark Results:
mlperf-train-v6.0/Dell/results/1xXE9712x4GB300/gpt_oss_20b/result_7.txt
mlperf-train-v6.0/HPE/results/HPE-GB300-ngpu8_ngc26.04/gpt_oss_20b/result_8.txt
mlperf-train-v6.0/HPE/results/HPE-GB300-ngpu16_ngc26.04/gpt_oss_20b/result_2.txt
mlperf-train-v6.0/HPE/results/HPE-GB300-ngpu32_ngc26.04/gpt_oss_20b/result_4.txt
mlperf-train-v6.0/NVIDIA/results/theia_ngpu72_ngc26.04_nemo/gpt_oss_20b/result_1.txt
mlperf-train-v6.0/NVIDIA/results/theia_ngpu512_ngc26.04_nemo/gpt_oss_20b/result_3.txt

* Configs:
mlperf-train-v6.0/HPE/benchmarks/gpt_oss_20b/implementations/nemo_arm_ngc26.04/config_GB300_2x4x3xtp1pp1cp1ep1_mxfp8.sh
mlperf-train-v6.0/HPE/benchmarks/gpt_oss_20b/implementations/nemo_arm_ngc26.04/config_GB300_4x4x2xtp1pp1cp1ep1_mxfp8.sh
mlperf-train-v6.0/HPE/benchmarks/gpt_oss_20b/implementations/nemo_arm_ngc26.04/config_GB300_8x4x2xtp1pp1cp1ep1_mxfp8.sh
mlperf-train-v6.0/NVIDIA/benchmarks/gpt_oss_20b/implementations/nemo/config_GB300_18x4x1xtp1pp1cp2ep4_mxfp8.sh
mlperf-train-v6.0/NVIDIA/benchmarks/gpt_oss_20b/implementations/nemo/config_GB300_128x4x1xtp2pp1cp4ep8.sh
```