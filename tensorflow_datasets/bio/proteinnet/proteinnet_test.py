# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""ProteinNet dataset tests."""

from tensorflow_datasets.bio.proteinnet.proteinnet import ProteinNet
import tensorflow_datasets.public_api as tfds


class ProteinNetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ProteinNet dataset."""
  DATASET_CLASS = ProteinNet
  SPLITS = {  # Number of fake examples.
      'train_100': 3,
      'test': 4,
      'validation': 2,
  }
  BUILDER_CONFIG_NAMES_TO_TEST = ['casp7']

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls._all_thresholds = ProteinNet.THRESHOLDS
    ProteinNet.THRESHOLDS = [100]

  @classmethod
  def tearDownClass(cls):
    ProteinNet.THRESHOLDS = cls._all_thresholds
    super().tearDownClass()


if __name__ == '__main__':
  tfds.testing.test_main()
