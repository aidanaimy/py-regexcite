# py-regexcite

`py-regexcite` is a simple Python package for string splitting, created for the DSCI 310 course. It provides a wrapper to extract the first element of a split string.

## Installation and Usage

You can install the development version from [TestPyPI](https://test.pypi.org/):

```bash
pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) py-regexcite
```

Once installed, you can use the strsplit1 function:

Python
from py_regexcite import strsplit1

# Extract the first element of a delimited string
result = strsplit1("alfa,bravo,charlie", ",")
print(result) # Output: 'alfa'
License: This project is licensed under the MIT License.
