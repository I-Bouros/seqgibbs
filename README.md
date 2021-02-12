# seqgibbs
![Run Unit Tests on multiple python versions](https://github.com/I-Bouros/seqgibbs/workflows/Run%20Unit%20Tests%20on%20multiple%20python%20versions/badge.svg)
![Run Unit Tests on multiple OS](https://github.com/I-Bouros/seqgibbs/workflows/Run%20Unit%20Tests%20on%20multiple%20OS/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/seqgibbs/badge/?version=latest)](https://seqgibbs.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/I-Bouros/seqgibbs/branch/main/graph/badge.svg?token=eo5z2634Nw)](https://codecov.io/gh/I-Bouros/seqgibbs)

An implementation of two Sequential Gibbs Sampling algorithms - Systematic Scan and Random Scan.

## References
[1] Wikipedia contributors. (2020, December 6). [Gibbs sampling](https://en.wikipedia.org/w/index.php?title=Gibbs_sampling&oldid=992631521). In Wikipedia, The Free Encyclopedia. Retrieved 10:36, February 12, 2021 

[2] Deligiannidis, G. (2016). [Advanced Simulation - Lecture 5](https://www.stats.ox.ac.uk/~deligian/pdf/sc5/slides/L5.pdf). Department of Statistics, University of Oxford.

[3] Whitley, N. (2008). Lectures 6 & 7: [The Gibbs Sampler](https://www.webpages.uidaho.edu/~stevel/565/U.%20Bristol/folien45.pdf). Department of Mathematics, University of Bristol.

## Installation procedure
***
One way to install the module is to download the repositiory to your machine of choice and type the following commands in the terminal. 
```bash
git clone https://github.com/I-Bouros/seqgibbs.git
cd ../path/to/the/file
```

A different method to install this is using `pip`:

```bash
pip install -i https://test.pypi.org/simple/ seqgibbs==0.0.1
```

## Usage

```python
import seqgibbs

# create a unidimensional sampler sampling from a normal distribution with parameters wrapped by 'fun'
seqgibbs.OneDimSampler(scipy.stats.norm.rvs, fun)

# create Systematic Scan Gibbs sampler for bidimensional data, starting at the default position (origin)
seqgibbs.SysGibbsAlgo(num_dim=2, initial_state=np.array([0, 0]))

# create Random Scan Gibbs sampler for bidimensional data, starting at the default position (origin)
# with the first coordinate twice as likely to update compared to the first.
seqgibbs.RandGibbsAlgo(num_dim=2, initial_state=np.array([0, 0]), new_probs=np.array([2, 1]))
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)