# Examples for running the seqgibbs module

Gibbs Algorithm is a sampling algorithm for multidimensional data. It invariably assumes that at all times one or a block of dimensions are updated according to a probability distribution which depends only on the values of the other dimensions of the state at that sampling time. 

There are two ways in which an update of the state:
- update each block of the dimensions in a particular order, at each update using the update dimensions of the state (*the Systematic Scan regime*)
- randomly choose which block of dimensions to update, keeping all others fixed (*the Random Scan regime*).

As of yet, the ``seqgibbs`` module covers only algorithms working with blocks of dimensions-to-update of size 1. This means that if at the current step in the algorithm we aim to update the jth dimension we do it according to the following formula:

```math::
X_{j}^{(t)} \sim \pi_{X_{j}|X_{j}}(\cdot|X_{1}^{(t)}, \dots , X_{j-1}^{(t)}, X_{j+1}^{(t-1)},\dots X_{d}^{(t-1)})
```

Due to this feature, the Gibbs algorithms can also be viewed as a particular instances of one-at-a-time Metropolis-Hastings routine for sampling. Also, under particular conditions (known as *positivity condition*), it can be proven that the chain of samples we obtain via this class of algorithms admit as their invariant distribution the target distribution from which we want to sample, i.e. if we run our sampler for long enough, the draws will resemble those from our distribution of choice.

Of course, this type of algorithm is only possible and feasible to implement when it is possible to sample from the partial conditional distributions $`\pi\_{X\_{j}|X\_{-j}`$ with realtive more ease than for the target $`\pi`$. If this is not the case, then it is recommended to use other methods for sampling.

Here are some Jupyter Notebook examples of the different functionalities offered by the seqgibbs module:

- [Case studies, good and bad, for running the Systematic Scan Gibbs Sampler](https://nbviewer.jupyter.org/github/SABS-R3-Epidemiology/branchpro/blob/main/branchpro/examples/branchpro-first-notebook.ipynb)

- [Case studies, good and bad, for running the Random Scan Gibbs Sampler](https://nbviewer.jupyter.org/github/SABS-R3-Epidemiology/branchpro/blob/main/branchpro/examples/french-flu-data.ipynb)

- [Comparison analysis of performance of Systematic vs Random Scan Gibbs Sampler](https://nbviewer.jupyter.org/github/SABS-R3-Epidemiology/branchpro/blob/main/branchpro/examples/french-flu-data.ipynb)