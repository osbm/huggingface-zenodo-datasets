"""
Huggingface datasets script for Zenodo dataset.
"""

import os
import shutil
import json

import datasets

_DESCRIPTION = """\
This dataset is for downloading a Zenodo dataset without extra packages.
"""


class NewDataset(datasets.GeneratorBasedBuilder):
    """This dataset downloads a zenodo dataset and returns its path."""

    VERSION = datasets.Version("1.1.0")

    def _info(self):
        features = datasets.Features(
            {
                "path": datasets.Value("string"),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
        )

    def _split_generators(self, dl_manager):
        self.zenodo_id = self.config.name.split("_")[0]
        self.filename = self.config.name.split("_")[1]

        url = f"https://zenodo.org/record/{self.zenodo_id}/files/{self.filename}"

        filepath = dl_manager.download([url])[0]        
        shutil.copy(filepath, os.getcwd())
        os.rename(os.path.basename(filepath), self.filename)
        
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": filepath,
                },
            ),
        ]

    def _generate_examples(self):
        yield 0, {"path": filepath}
