#!/usr/bin/env python
from rasa.nlu.featurizers.dense_featurizer.lm_featurizer import LanguageModelFeaturizer
from transformers import (
  BertTokenizerFast,
  TFAlbertModel,
)

import logging

logger = logging.getLogger(__name__)

class AlbertFeaturizer(LanguageModelFeaturizer):
    def _load_model_instance(self, skip_model_load: bool) -> None:
        self.model_weights = 'ckiplab/albert-tiny-chinese'
        self.max_model_sequence_length = 512
        self.tokenizer = BertTokenizerFast.from_pretrained(self.model_weights)
        self.model = TFAlbertModel.from_pretrained(self.model_weights, from_pt=True)
        #self.model.trainable = False

        self.pad_token_id = self.tokenizer.unk_token_id
