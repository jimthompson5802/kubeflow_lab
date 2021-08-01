#!/bin/bash

set -xe


MODEL_SERVICE_NAME="sklearn-irisv2"
MODEL_SERVICE_IP_ADDR=$(kubectl get svc -l serving.kubeflow.org/inferenceservice=${MODEL_SERVICE_NAME},networking.internal.knative.dev/serviceType=Private -o jsonpath='{.items[0].spec.clusterIP}')
MODEL_SERVICE_PORT=$(kubectl get svc -l serving.kubeflow.org/inferenceservice=${MODEL_SERVICE_NAME},networking.internal.knative.dev/serviceType=Private -o jsonpath='{.items[0].spec.ports[0].port}')

INPUT_PATH=@./iris-input.json
curl -v -k -L \
    -H "kubeflow-userid: user" \
	http://${MODEL_SERVICE_IP_ADDR}:${MODEL_SERVICE_PORT}/v2/models/${MODEL_SERVICE_NAME}/infer -d ${INPUT_PATH}
