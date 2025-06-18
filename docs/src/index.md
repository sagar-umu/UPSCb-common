# File for src

# UPSCb-common

This repository is a library of common scripts and templates created to avoid reinventing the wheel then and again.

## CITATION
Please use [![DOI](https://zenodo.org/badge/206072841.svg)](https://zenodo.org/badge/latestdoi/206072841) to cite the use of this repos :-)

## IMPORTANT NOTICE

**2022/12/06** I found a serious bug in the DE template! I have corrected the DE template: <https://github.com/UPSCb/UPSCb-common/tree/master/templates/R>, but please check out your analysis done since 2021/03/05. Sadly, it means that any analysis needs redoing! :disappointed: :disappointed: :disappointed: The issue is that the template used the lfcThreshold when retrieving the DE results (using the DESeq2 results function). What this does, unlike the alpha parameter that sets the FDR threshold to return results, is to change the test that is being done. Instead of comparing for a difference in expression of 0, it tests for a difference in expression at the selected value (+0.5 by default). Results are likely to be quite drastically different!

## Table of Contents

1. [Introduction](../UPSCb-common/Introduction.md)

2. [src](#src)
    - [bash](#bash)
    - [python](#python)
    - [R](#r)
3. [templates](#templates)
    - [bash](#bash)
    - [python](#python)
    - [R](#r)
4. [pipeline](#pipeline)

---

## Structure

There are three important directories:

    |- pipeline
    |- src
      |- bash
      |- R
    |- templates
      |- R

1.  `pipeline` is a directory that contains scripts written (mostly) in bash to be copied into your project and used through a SLURM queueing system.
2.  `src` (source) contains a number of subdirectories sorted by programming language holding a number of utilities
3.  `templates` contains a number of subdirectories sorted by programming language holding a number of templates to be re-used. Most notably it contains examples of data analysis in R (*e.g.* BiologicalQA.R, DifferentialExpression.R, *etc.*) and some bash examples to submit jobs to the queue.

## Frequently used terms/resources

1. **Git**: 
- In technical terms: 'A version control system (VCS) used to track changes to your source code. You can learn more about Git [here](https://missing.csail.mit.edu/2020/version-control/). 
- Learn about Git in not-so tech terms: [here](https://www.reddit.com/r/learnprogramming/comments/pymrss/comment/hey5be7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

2. **Github**: [Website](github.com) that hosts public and private code documented using Git. 

3. **R and R-studio**: One of the most important tools that is used frequently in UPSCb data anlaysis pipelines. If you are not familiar with R, please go through these resources: [swirl](swirlstats.com), [discovR](www.discovr.rocks/discovr)

4. **SLURM**: It is a queueing system meant to ensure the concurrent and fair use of a compute cluster. You can learn more about SLURM and SLURM commands like `sbatch` and `squeue` [here](https://slurm.schedmd.com/quickstart.html)

5. **Video**: Here is a [video](https://www.youtube.com/watch?v=3XMHTixiszE) explaining how we use Git and SLURM at UPSCb. 

6. **Containers**: As the name suggests, containers allow code for target tools/applications to be packaged and isolated (in other words: contained) alongwith their dependecies. In practice, it makes it easy for different users to run the tools consistently regardless of their run environment. A video explaination can be found [here](https://umeauniversity-my.sharepoint.com/personal/edpi0005_ad_umu_se/_layouts/15/stream.aspx?id=%2Fpersonal%2Fedpi0005%5Fad%5Fumu%5Fse%2FDocuments%2Fsummary%5Fserver%5Fintroduction%2Fvideo%5Fapptainer%5Fcontainers%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ee0daaf76%2Dddbf%2D4cb4%2Dbc6c%2Dd8dd2a449b7e)
- More information about the containers and their usage can be found [here](https://github.com/bschiffthaler/kogia)

## Access

1.  Follows the instructions [there](https://youtu.be/hYtIKIIwRss) and our discussions in Slack.

## Setup your project

We use `git` and `SLURM` to ensure reproducible research, here are gists on how to enable that in your projects:

1.  [Git setup](https://gist.github.com/nicolasDelhomme/46a1053d277510b95692318bd1732b6d)
2.  [SLURM usage](https://gist.github.com/nicolasDelhomme/6fbff1e4db3c7ee4b3bb4f710667fd0d)
3.  A [video](https://youtu.be/3XMHTixiszE) of a tech seminar on both (duration \~1h)
4.  A description of our server structure
5.  A video on how to [download data from Novogene](https://youtu.be/A6JcORYs9L0)

## Rules of conduct

# Visulization examples

1.  [Gene Ontology](https://gist.github.com/amnzr/7d859ae127c30e13fef3198c20287da2)

# Templates

Before **re-inventing the wheel**, check the templates directory! A number of useful templates are available there:

1.  `R/empty.R` to initiate an R script with the Rmd header and session info blocks.
2.  `R/BiologicalQA.R` to do the initial Exploratory Data Analysis (EDA) of your RNA-Seq data
3.  `R/DifferentialExpression.R` to perform a Differential Expression (DE) of your data (follows the previous one)
4.  `bash/runTemplate.sh` to prototype script to be run on an HPC (High Perf. Compute) using SLURM (a job manager)

# Useful links

The following link will bring you to a server introduction guide with tips about how to connect to our server, how to run slurm jobs properly and how to use AspSeq.

It also contains a video about how to make apptainer containers if you need to install a software that we currently do not have.

https://umeauniversity-my.sharepoint.com/:f:/r/personal/edpi0005_ad_umu_se/Documents/summary_server_introduction?csf=1&web=1&e=NQW9Gq


# Troubleshooting

## Resolving Issues by yourself

1.  [Rstudio common issues](https://gist.github.com/nicolasDelhomme/5bde1e878b2eaa3def1cced06076b7db)

## Contact us

For UPSC members, ask us to be added to our Slack channel as well as mailing list. These are the two channels we use to communicate about server updates and downtime (as well as other technical issues), but also those we use to discuss projects, provide support, *etc.*
