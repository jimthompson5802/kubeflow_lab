#!/usr/bin/env python
# coding: utf-8

# # Testbed for reproducibility in TF

# In[39]:


import random
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, LSTM, Dense, SpatialDropout1D, BatchNormalization, Dropout
from tensorflow.keras.metrics import AUC


# ## Global Configs

# In[40]:


RANDOM_SEED = 1919
BATCH_SIZE = 128
SEQUENCE_SIZE = 10
EMBEDDING_SIZE = 30
NUMBER_SAMPLES = 10000
SHUFFLE_INPUT = False


# ## Setup Synthetic Data

# In[41]:


# setup for reproducible data
np.random.seed(13)

#create artificial training data
X = np.random.normal(size = (NUMBER_SAMPLES, SEQUENCE_SIZE, EMBEDDING_SIZE)).astype(np.float32)
y = np.random.binomial(1, 0.3, size = NUMBER_SAMPLES).astype(np.float32)


# In[42]:


print(f'X shape {X.shape}, y shape {y.shape}')


# ## Helper functions

# In[43]:


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


# In[44]:


# build neural network
def build_core_network(model_input):
    hidden = SpatialDropout1D(0.2)(model_input)
    hidden = LSTM(100, dropout = 0.2, recurrent_dropout = 0.2)(hidden)
    hidden = Dense(50, activation = 'tanh')(hidden)
    hidden = BatchNormalization()(hidden)
    hidden = Dropout(0.2)(hidden)
    hidden = Dense(1, activation = 'sigmoid')(hidden)
    return hidden
    


# In[45]:


# check for equal model weights
def compare_model_weights(model1_weights, model2_weights):
    ## Compare learned parameters
    equal_flags = []
    max_diffs = []
    for w1, w2 in zip(model1_weights, model2_weights):
        equal_flags.append(np.allclose(w1.numpy(), w2.numpy()))
        max_diffs.append(np.max(np.abs(w1.numpy() - w2.numpy())))
    try:    
        assert all(equal_flags)
        print('model weights are equal')
    except AssertionError:
        print('model weights not equal')
        for b, d in zip(equal_flags, max_diffs):
            print(f'Equal {b}, max diff {d}')


# ##  test original 3-d Structure

# In[46]:


# setup for reproducible training
set_for_reproducibility()


# In[47]:


# In[ ]:


#build and compile TF model


def nn():
    model_input = Input(shape = (SEQUENCE_SIZE, EMBEDDING_SIZE))
    
    model_output = build_core_network(model_input)
    
    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[48]:


# In[ ]:

model = nn()

print('\nBaseline model training')
model.fit(X, y, epochs=5, batch_size=BATCH_SIZE, shuffle=SHUFFLE_INPUT)


# ## Test conversion to 2-d structure

# In[49]:


# setup for reproducible training
set_for_reproducibility()


# In[50]:


# setup model for 2-d structure
def nn_2d():
    model_input = Input(shape = (SEQUENCE_SIZE * EMBEDDING_SIZE,))   # altered for 2-d structure
    hidden = tf.reshape(model_input, (-1, SEQUENCE_SIZE, EMBEDDING_SIZE))  # unpack to 3-d structure
    
    model_output = build_core_network(hidden)

    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[51]:


model2 = nn_2d()

X_2d = X.reshape(-1, SEQUENCE_SIZE * EMBEDDING_SIZE)
print('\n2-d model training')
model2.fit(X_2d, y, epochs=5, batch_size=BATCH_SIZE, shuffle=SHUFFLE_INPUT)


# ## Compared learned parameters from the two models

# In[52]:


## Compare learned parameters
print('compare baseline model vs 2-d model')
compare_model_weights(model.weights, model2.weights)


# ## Test 2-d structure with scikeras.KerasClassifer

# In[53]:


from scikeras.wrappers import KerasClassifier


# In[54]:


# setup for reproducible training
set_for_reproducibility()


# In[55]:


# setup model for 2-d structure
def nn_scikeras():
    model_input = Input(shape = (SEQUENCE_SIZE * EMBEDDING_SIZE,))   # altered for 2-d structure
    hidden = tf.reshape(model_input, (-1, SEQUENCE_SIZE, EMBEDDING_SIZE))  # unpack to 3-d structure
    
    model_output = build_core_network(hidden)

    model = Model(model_input, model_output)
    model.compile(loss = 'binary_crossentropy', optimizer = 'Adam', metrics = [AUC()])
    
    return model


# In[56]:


model_scikeras = KerasClassifier(model=nn_scikeras, optimizer='Adam')

X_2d = X.reshape(-1, SEQUENCE_SIZE * EMBEDDING_SIZE)
print('\nscikeras model training')
model_scikeras.fit(X_2d, y, epochs=5, batch_size=BATCH_SIZE, shuffle=SHUFFLE_INPUT)


# ## Compared learned parameters from the two models

# In[57]:


## Compare learned parameters
print('compare baseline model vs scikeras model')
compare_model_weights(model.weights, model_scikeras.model_.weights)


# In[ ]:




