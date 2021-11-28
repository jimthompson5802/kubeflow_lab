# Notes

## Reproducibility experiment 1
Created Python program from notebook:
```
jupyter nbconvert --to=script TF_native.ipynb
```


Run the Python program:
```
PYTHONHASHSEED=0 TF_DETERMINISTIC_OPS=1 python TF_native.py

# Example output
2021-11-28 03:45:22.325346: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 03:45:22.325408: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 03:45:28.560418: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 03:45:28.560511: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 03:45:28.560642: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 03:45:28.561431: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 9s 60ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 4s 50ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 4s 48ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 4s 51ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 4s 50ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 8s 55ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 7s 87ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 7s 89ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 7s 85ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 7s 84ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs 2-d model
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0

scikeras model training
Epoch 1/5
79/79 [==============================] - 13s 78ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 5s 60ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 4s 50ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 4s 52ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 5s 58ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
True, max diff 0.0
```

There appears to be another source of non-deterministic operation, more research needed.  Another run:
```
2021-11-28 03:50:48.501420: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 03:50:48.501480: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 03:50:53.007633: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 03:50:53.007749: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 03:50:53.007840: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 03:50:53.008351: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 8s 50ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 4s 48ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 4s 53ms/step - loss: 0.6392 - auc: 0.5236
Epoch 4/5
79/79 [==============================] - 4s 56ms/step - loss: 0.6348 - auc: 0.5229
Epoch 5/5
79/79 [==============================] - 4s 50ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 8s 53ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 4s 53ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 4s 50ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 4s 54ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 4s 52ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs 2-d model
False, max diff 0.0013092691078782082
False, max diff 0.0014346316456794739
False, max diff 0.0005831718444824219
False, max diff 0.000274658203125
False, max diff 0.00035981187829747796
False, max diff 0.0001285076141357422
False, max diff 5.672872066497803e-05
False, max diff 0.0003906339406967163
False, max diff 0.0001111254096031189
False, max diff 0.00014284998178482056
True, max diff 5.21540641784668e-07

scikeras model training
Epoch 1/5
79/79 [==============================] - 8s 51ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 4s 48ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 4s 52ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 4s 52ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 4s 49ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
False, max diff 0.0013092691078782082
False, max diff 0.0014346316456794739
False, max diff 0.0005831718444824219
False, max diff 0.000274658203125
False, max diff 0.00035981187829747796
False, max diff 0.0001285076141357422
False, max diff 5.672872066497803e-05
False, max diff 0.0003906339406967163
False, max diff 0.0001111254096031189
False, max diff 0.00014284998178482056
True, max diff 5.21540641784668e-07

```

## Reproducibility Experiment 2

```
jupyter nbconvert --to=script reproducibility_testbed.ipynb 
```


```
jovyan@dask-notebook-0:~/kubeflow_lab/notebooks/tensorflow$ python reproducibility_testbed.py
2021-11-28 17:05:26.310015: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 17:05:26.310077: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 17:05:29.057196: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 17:05:29.057297: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 17:05:29.057359: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 17:05:29.057588: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 4s 28ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 5s 33ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs 2-d model
model weights are equal

scikeras model training
Epoch 1/5
79/79 [==============================] - 4s 30ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
model weights are equal


jovyan@dask-notebook-0:~/kubeflow_lab/notebooks/tensorflow$ python reproducibility_testbed.py
2021-11-28 17:06:15.616610: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 17:06:15.616660: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 17:06:17.321299: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 17:06:17.321356: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 17:06:17.321424: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 17:06:17.321706: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 4s 28ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 30ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 4s 29ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs 2-d model
model weights are equal

scikeras model training
Epoch 1/5
79/79 [==============================] - 4s 29ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
model weights are equal


jovyan@dask-notebook-0:~/kubeflow_lab/notebooks/tensorflow$ python reproducibility_testbed.py
2021-11-28 17:07:05.818906: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 17:07:05.818958: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 17:07:07.415393: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 17:07:07.415457: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 17:07:07.415509: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 17:07:07.415763: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 4s 29ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 4s 29ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6392 - auc: 0.5236
Epoch 4/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs 2-d model
model weights not equal
Equal False, max diff 0.0006087943911552429
Equal False, max diff 0.001051638275384903
Equal False, max diff 0.0004996061325073242
Equal False, max diff 0.00015875522512942553
Equal False, max diff 0.0005196661222726107
Equal False, max diff 7.325410842895508e-05
Equal False, max diff 2.3186206817626953e-05
Equal False, max diff 0.0004026312381029129
Equal False, max diff 5.619227886199951e-05
Equal False, max diff 8.418411016464233e-05
Equal False, max diff 3.159046173095703e-06

scikeras model training
Epoch 1/5
79/79 [==============================] - 4s 28ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
model weights are equal
```

Purposely set `tf.random.set_seed()` to a different value for 2-d model.  Epoch metrics different from the other runs.  max absolute difference much larger.
```

jovyan@dask-notebook-0:~/kubeflow_lab/notebooks/tensorflow$ python reproducibility_testbed.py
2021-11-28 17:16:24.709634: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2021-11-28 17:16:24.709721: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
X shape (10000, 10, 30), y shape (10000,)
2021-11-28 17:16:26.409968: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcuda.so.1'; dlerror: libcuda.so.1: cannot open shared object file: No such file or directory
2021-11-28 17:16:26.410029: W tensorflow/stream_executor/cuda/cuda_driver.cc:269] failed call to cuInit: UNKNOWN ERROR (303)
2021-11-28 17:16:26.410086: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:156] kernel driver does not appear to be running on this host (dask-notebook-0): /proc/driver/nvidia/version does not exist
2021-11-28 17:16:26.410314: I tensorflow/core/platform/cpu_feature_guard.cc:151] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

Baseline model training
Epoch 1/5
79/79 [==============================] - 4s 28ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6259 - auc: 0.5411

2-d model training
Epoch 1/5
79/79 [==============================] - 4s 28ms/step - loss: 0.7305 - auc: 0.4892
Epoch 2/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6604 - auc: 0.5062
Epoch 3/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6485 - auc: 0.5007
Epoch 4/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6324 - auc: 0.5291
Epoch 5/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6295 - auc: 0.5269
compare baseline model vs 2-d model
model weights not equal
Equal False, max diff 0.2948779761791229
Equal False, max diff 0.3463980257511139
Equal False, max diff 0.0653347373008728
Equal False, max diff 0.4193931221961975
Equal False, max diff 0.11848480999469757
Equal False, max diff 0.07981741428375244
Equal False, max diff 0.26063647866249084
Equal False, max diff 0.13439857959747314
Equal False, max diff 0.025381527841091156
Equal False, max diff 0.45664751529693604
Equal False, max diff 0.0018282532691955566

scikeras model training
Epoch 1/5
79/79 [==============================] - 4s 29ms/step - loss: 0.7360 - auc: 0.4954
Epoch 2/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6593 - auc: 0.5064
Epoch 3/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6392 - auc: 0.5235
Epoch 4/5
79/79 [==============================] - 2s 29ms/step - loss: 0.6348 - auc: 0.5230
Epoch 5/5
79/79 [==============================] - 2s 28ms/step - loss: 0.6259 - auc: 0.5411
compare baseline model vs scikeras model
model weights are equal
```