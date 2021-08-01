# Test Results for serving.kubeflow.org/v1beta1 with endpoint protocol v2

```
(base) jovyan@first-notebook-0:~/kubeflow_lab/kfserving/v2api_test$ ./curl_rest_api.sh; echo
+ MODEL_SERVICE_NAME=sklearn-irisv2
++ kubectl get svc -l serving.kubeflow.org/inferenceservice=sklearn-irisv2,networking.internal.knative.dev/serviceType=Private -o 'jsonpath={.items[0].spec.clusterIP}'
+ MODEL_SERVICE_IP_ADDR=10.43.241.94
++ kubectl get svc -l serving.kubeflow.org/inferenceservice=sklearn-irisv2,networking.internal.knative.dev/serviceType=Private -o 'jsonpath={.items[0].spec.ports[0].port}'
+ MODEL_SERVICE_PORT=80
+ INPUT_PATH=@./iris-input.json
+ curl -v -k -L -H 'kubeflow-userid: user' http://10.43.241.94:80/v2/models/sklearn-irisv2/infer -d @./iris-input.json
*   Trying 10.43.241.94:80...
* TCP_NODELAY set
* Connected to 10.43.241.94 (10.43.241.94) port 80 (#0)
> POST /v2/models/sklearn-irisv2/infer HTTP/1.1
> Host: 10.43.241.94
> User-Agent: curl/7.68.0
> Accept: */*
> kubeflow-userid: user
> Content-Length: 178
> Content-Type: application/x-www-form-urlencoded
> 
* upload completely sent off: 178 out of 178 bytes
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< content-length: 206
< content-type: application/json
< date: Sun, 01 Aug 2021 22:01:37 GMT
< server: envoy
< x-envoy-upstream-service-time: 11
< 
* Connection #0 to host 10.43.241.94 left intact
{"model_name":"sklearn-irisv2","model_version":null,"id":"92932085-22a1-4988-8037-16b036740bbf","parameters":null,"outputs":[{"name":"predict","shape":[2],"datatype":"FP32","parameters":null,"data":[1,2]}]}
```