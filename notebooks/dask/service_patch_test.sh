#!/bin/bash


kubectl patch svc dask-scheduler --patch \
  '{"spec": {"ports": [{"name": "tcp-dask-scheduler", "port": 8786}]}}'
