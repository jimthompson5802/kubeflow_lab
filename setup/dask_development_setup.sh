# set up for dask-kubernetes development
git clone https://github.com/jimthompson5802/kubeflow_lab \
  && pushd kubeflow_lab/setup \
  && ./set_me_up.sh \
  && git config credential.helper 'cache --timeout=7200' \
  && popd \
  && git clone https://github.com/jimthompson5802/dask-kubernetes \
  && pip install -e dask-kubernetes \
  && pushd dask-kubernetes \
  && git config credential.helper 'cache --timeout=7200' \
  && git checkout enable-kubeflow \
  && popd \
  && git clone https://github.com/jimthompson5802/dask_kubeflow \
  && pushd dask_kubeflow \
  && git config credential.helper 'cache --timeout=7200' \
  && popd

# install for dask jupyterlab extension (assume JL 3+)
pip install dask-labextension


# helper commands to monitor and clean up dask related objects
alias clean_dask='kubectl delete pod -l app=dask \
  && kubectl delete svc -l app=dask \
  && kubectl delete envoyfilter -l app=dask'

alias show_dask='kubectl get pod -l app=dask \
  && kubectl get svc -l app=dask \
  && kubectl get envoyfilter -l app=dask'
