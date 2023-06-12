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


# Contribution

[The huggingface repository](https://huggingface.co/datasets/osbm/zenodo) is actually a mirror of the github repository [osbm/zenodo](https://github.com/osbm/huggingface-zenodo-datasets). If you want to open an issue or PR, please do it on the github repository. I chose to do it this way because I wanted to use github actions. Currently only github action is mirroring the repository to huggingface. 😅
