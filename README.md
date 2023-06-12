---
pretty_name: Download Zenodo Dataset files
---

# Download zenodo dataset files using huggingface datasets

You can download a specific file from the Zenodo dataset using the following code:

Zenodo id : 5172018
File name : FDB-17-fragmentset.smi.gz

```python
from datasets import load_dataset
load_dataset("osbm/zenodo", "5172018_FDB-17-fragmentset.smi.gz")
```

This command will also copy the file into your current directory so that you can use it directly.

Here is an example notebook: https://gist.github.com/osbm/35a499f5756df22de30be20463aa6331
