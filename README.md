### Quick Rundown of MLPerf v6.0 Training
— 2026/06/18 

MLPerf Training v6.0 was released on June 16, 2026. MLCommons and participating companies have already published their own highlights, results, and platform narratives. This rundown is not meant to re-summarize those announcements. Instead, it adds analysis on the parts I care about as an observer:
* The new MoE pretraining workloads, *DeepSeek-v3 (671B)* and *GPT-OSS (20B)*, including notable optimization choices and configs.
* Scaling efficiency across GB200 and GB300 platforms. MI Instinct does not yet have enough data points for scaling analysis, but kudos for its first training submissions across MI300X, MI325X, and MI350X.
* New AMD MXFP4 recipe submissions, enabling direct MXFP4 vs NVFP4 comparisons on 8-GPU Llama 3.1 8B across B200, B300, GB200, GB300, MI350X, and MI355X.

Links:
* [v6.0 Release][v6-rl-mlcommons] by MLCommons, Supplemental Discussion [pdf][v6-supplement]
* [Result Dashboard][v6-tableau], [Submitters' code][gh-results]
* Nvidia: [blog][nv-blog], [tech dive][nv-tech]
* AMD: [blog][amd-blog], [tech dive][amd-tech], [tutorials][amd-repro]
* [Coreweave][cw-blog], [Nebius][nbs-blog], [Lambda][lmbd-blog], [Azure][azure-blog]
* [My rundown][vs9-t5.1] on previous v5.1 (Nov'25)

---

### DeepSeek-v3 (671B)
<img src="assets/scaling-dsv3.svg" width="600" style="height:auto;">
*To add notes*

---

### GPT-OSS (20B)
<img src="assets/scaling-gptoss.png" width="600" style="height:auto;">
*To add notes*
---

### MXFP4 vs NVFP4 (Llama3.1 8B on 8 x GPUs)
<img src="assets/fp4-across-8xgpu.png" width="600" style="height:auto;">
*To add notes*

<!--  -->

[v6-rl-mlcommons]: https://mlcommons.org/2026/06/mlperf-training-v6-0-results/
[v6-supplement]: https://mlcommons.org/wp-content/uploads/2026/06/MLPerf-Training-v6.0-Supplemental-Discussion-UNDER-EMBARGO-UNTIL-6_16_26-8_00-AM-PT-1.pdf
[v6-tableau]: https://mlcommons.org/benchmarks/training/
[gh-results]: https://github.com/mlcommons/training_results_v6.0

[nv-blog]: https://blogs.nvidia.com/blog/blackwell-mlperf-training-6-0/
[nv-tech]: https://developer.nvidia.com/blog/nvidia-blackwell-tops-mlperf-training-6-0-with-industry-leading-scale-and-performance/

[amd-blog]: https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-training-6-0-results.html
[amd-tech]: https://rocm.blogs.amd.com/artificial-intelligence/mlperf-training-v6.0/README.html
[amd-repro]: https://rocm.blogs.amd.com/artificial-intelligence/mlperf-training6.0-repro/README.html
[amd-mxfp4-paper]: https://arxiv.org/abs/2605.09825

[cw-blog]: https://www.coreweave.com/blog/coreweave-trains-deepseek-v3-in-two-minutes
[nbs-blog]: https://nebius.com/blog/posts/mlperf-training-v6-0-results
[lmbd-blog]: https://lambda.ai/blog/mlperf-training-v6.0-lambda-delivers-fastest-llm-training
[azure-blog]: https://techcommunity.microsoft.com/blog/azurehighperformancecomputingblog/azure-sets-a-new-performance-record-for-llm-training-benchmark-at-extreme-scale/4523077

[vs9-t5.1]: https://github.com/vuiseng9/mlperf-t5.1-rundown

[ref-gpt-oss]: https://mlcommons.org/2026/05/gpt-oss-moe-training6
[ref-dsv3]: https://mlcommons.org/2026/05/deepseek-v3-training-v6-0


