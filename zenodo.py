"""
Huggingface datasets script for Zenodo dataset.
"""

import json
import os

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
        zenodo_id = self.config.name.split("_")[0]
        filename = self.config.name.split("_")[1]

        url = f"https://zenodo.org/record/{zenodo_id}/files/{filename}"

        data_dir = dl_manager.download([url])
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "filepath": data_dir[0],
                },
            ),
        ]

    def _generate_examples(self, filepath):
        yield 0, {"path": filepath}
