# Nextflow

[Nextflow](https://www.nextflow.io/) is a workflow manager that co-ordinates multiple steps in a pipeline. Think of it as SLURM but instead of managing multiple jobs likely submitted by multiple users, Nextflow will manage all steps in your pipeline. So instead of running FastQC and waiting for its results to feed to an aligner, you just run the whole pipeline at once.   

[nf.core](https://nf-co.re/) is an open source database of pipelines you can use to do your analysis. We use the RNA-seq pipeline from nf.core for the analysis in the facility. 

Scripts for running the analysis using the Nextflow pipeline are also available in the [`UPSCb-common`](https://github.com/UPSCb/UPSCb-common/tree/master/nextflow) repository. 

>!!! Caution
> Be sure to modify the `.config` and `.json` files to correctly provide the source files that you want to analyse before running the pipeline.