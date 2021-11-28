# Notes


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