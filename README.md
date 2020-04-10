# pyfilecalltree

Generate call tree from a Python source file without profiling.

## Installation

### Prerequisites

* `graphiz`

### Pip install

```
pip install git+https://git@github.com/boupetch/pyfilecalltree.git
```

## Usage

```
import pyfilecalltree

pyfilecalltree.generate_calltree("source.py","output.png")
```

### Example

```
import pyfilecalltree
import urllib.request

urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/'+
    'geekcomputers/Python/0e04a63eab7cc'+
    '21e605db0d07760e1b4a800c06f/'+
    'bank_managment_system/frontend.py',
    './example.py')
    
pyfilecalltree.generate_calltree("./example.py") 
```
