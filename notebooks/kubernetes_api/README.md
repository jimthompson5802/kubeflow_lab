# Kubernetes API

Sandbox to test out use of k8s api.

|Notebook|Description|
|--------|-----------|
|`k8s_api_test.ipynb`|Demonstrates basic k8s operations. k8s resources are manipulated with low-level api calls.  This notebook shows how to retrieve k8s object information and creating and deleting a pod.|
|`deployment_service_api_test.ipynb`|Demonstrates higher-level api that manipulates the k8s resource via python dictionary.  The example creates a `Deployment` and `Service` objects.|
|`custom_istio_resource_test.ipynb`|Demonstrates creating and deleting custom istio resources: `VirtualService` and `EnvoyFilter`|