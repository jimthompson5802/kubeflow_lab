#!/usr/bin/env python
# coding: utf-8

# # Test of native TF/Keras implementation

# In[1]:


import random
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, LSTM, Dense, SpatialDropout1D, BatchNormalization, Dropout
from tensorflow.keras.metrics import AUC


# ## Global Configs

# In[2]:


RANDOM_SEED = 1919
BATCH_SIZE = 128
SEQUENCE_SIZE = 10
EMBEDDING_SIZE = 30
NUMBER_SAMPLES = 10000


# ## Setup Synthetic Data

# In[3]:


# setup for reproducible data
np.random.seed(13)

#create artificial training data
X = np.random.normal(size = (NUMBER_SAMPLES, SEQUENCE_SIZE, EMBEDDING_SIZE)).astype(np.float32)
y = np.random.binomial(1, 0.3, size = NUMBER_SAMPLES).astype(np.float32)


# In[4]:


print(f'X shape {X.shape}, y shape {y.shape}')


# ## Reproducibility Helper function

# In[5]:


# setup for reproducible training
def set_for_reproducibility():
    # ensure clean setup of TF
    tf.keras.backend.clear_session()

    # set various RNG seed
    np.random.seed(RANDOM_SEED)
    tf.random.set_seed(RANDOM_SEED)
    random.seed(RANDOM_SEED)

    # single-thread execution for reproducibility at the expense of run-time
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)


# ##  test original 3-d Structure

# In[6]:


# setup for reproducible training
set_for_reproducibility()


# In[7]:


# In[ ]:


#build and compile TF model


def nn():
    model_input = Input(shape = (SEQUENCE_SIZE, EMBEDDING_SIZE))
    model_dropout1 = SpatialDropout1D(0.2)(model_input)
    model_lstm = LSTM(100, dropout = 0.2, recurrent_dropout = 0.2)(model_dropout1)
    model_dense1 = Dense(50, activation = 'tanh')(model_lstm)
    model_bn1 = BatchNormalization()(model_dense1)
    model_dropout2 = Dropout(0.2)(model_bn1)
    model_output = Dense(1, activation = 'sigmoid')(model_dropout2)
    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[8]:


# In[ ]:

model = nn()

print('\nBaseline model training')
model.fit(X, y, epochs=5, batch_size=BATCH_SIZE, shuffle=False)


# ## Test conversion to 2-d structure

# In[9]:


# setup for reproducible training
set_for_reproducibility()


# In[10]:


# setup model for 2-d structure


def nn2():
    model_input = Input(shape = (SEQUENCE_SIZE * EMBEDDING_SIZE,))   # altered for 2-d structure
    model_input_unpack = tf.reshape(model_input, (-1, SEQUENCE_SIZE, EMBEDDING_SIZE))  # unpack to 3-d structure
    model_dropout1 = SpatialDropout1D(0.2)(model_input_unpack)
    model_lstm = LSTM(100, dropout = 0.2, recurrent_dropout = 0.2)(model_dropout1)
    model_dense1 = Dense(50, activation = 'tanh')(model_lstm)
    model_bn1 = BatchNormalization()(model_dense1)
    model_dropout2 = Dropout(0.2)(model_bn1)
    model_output = Dense(1, activation = 'sigmoid')(model_dropout2)
    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[11]:


model2 = nn2()

X_2d = X.reshape(-1, SEQUENCE_SIZE * EMBEDDING_SIZE)
print('\n2-d model training')
model2.fit(X_2d, y, epochs=5, batch_size=BATCH_SIZE, shuffle=False)


# ## Compared learned parameters from the two models

# In[12]:


## Compare learned parameters
print('compare baseline model vs 2-d model')
for nn_parameter, nn2_parameter in zip(model.weights, model2.weights):
    print(
        f'{np.allclose(nn_parameter.numpy(), nn2_parameter.numpy())}, '
        f'max diff {np.max(np.abs(nn_parameter.numpy() - nn2_parameter.numpy()))}'
    )


# ## Test 2-d structure with scikeras.KerasClassifer

# In[13]:


from scikeras.wrappers import KerasClassifier


# In[14]:


# setup for reproducible training
set_for_reproducibility()


# In[15]:


# setup model for 2-d structure


def nn_scikeras():
    model_input = Input(shape = (SEQUENCE_SIZE * EMBEDDING_SIZE,))   # altered for 2-d structure
    model_input_unpack = tf.reshape(model_input, (-1, SEQUENCE_SIZE, EMBEDDING_SIZE))  # unpack to 3-d structure
    model_dropout1 = SpatialDropout1D(0.2)(model_input_unpack)
    model_lstm = LSTM(100, dropout = 0.2, recurrent_dropout = 0.2)(model_dropout1)
    model_dense1 = Dense(50, activation = 'tanh')(model_lstm)
    model_bn1 = BatchNormalization()(model_dense1)
    model_dropout2 = Dropout(0.2)(model_bn1)
    model_output = Dense(1, activation = 'sigmoid')(model_dropout2)
    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[16]:


model_scikeras = KerasClassifier(model=nn_scikeras, optimizer='Adam')

X_2d = X.reshape(-1, SEQUENCE_SIZE * EMBEDDING_SIZE)
print('\nscikeras model training')
model_scikeras.fit(X_2d, y, epochs=5, batch_size=BATCH_SIZE, shuffle=False)


# ## Compared learned parameters from the two models

# In[17]:


## Compare learned parameters
print('compare baseline model vs scikeras model')
for nn_parameter, scikeras_parameter in zip(model.weights, model_scikeras.model_.weights):
       print(
        f'{np.allclose(nn_parameter.numpy(), scikeras_parameter.numpy())}, '
        f'max diff {np.max(np.abs(nn_parameter.numpy() - scikeras_parameter.numpy()))}'
    )


# In[ ]:




