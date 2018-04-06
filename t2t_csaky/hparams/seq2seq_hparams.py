from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# tensor2tensor imports
from tensor2tensor.models import lstm
from tensor2tensor.utils import registry



""" Only this works with own_hparams_seq2seq model, so it has to be changed to the appropriate batch size. """
def chatbot_lstm_hparams():
  hparams=chatbot_lstm_batch_256()
  hparams.hidden_size=3072
  return hparams


""" Different batch sizes. """
@registry.register_hparams
def chatbot_lstm_batch_8k():
  hparams = lstm.lstm_seq2seq()

  hparams.clip_grad_norm=0.0
  hparams.shared_embedding_and_softmax_weights=True
  hparams.optimizer="Adafactor"
  hparams.use_fixed_batch_size=True
  hparams.summarize_vars=True

  hparams.symbol_modality_num_shards=10
  hparams.hidden_size=2048
  hparams.num_hidden_layers=2
  hparams.batch_size=8192
  hparams.max_length = 65
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_1():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=1
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_2():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=2
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_512():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=512
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_256():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=256
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_128():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=128
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_64():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=64
  return hparams

@registry.register_hparams
def chatbot_lstm_batch_32():
  hparams = chatbot_lstm_batch_8k()
  hparams.batch_size=32
  return hparams