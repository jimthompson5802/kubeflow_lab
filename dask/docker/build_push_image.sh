#!/bin/bash

image_tag=${1:-latest}
image_repository=${2:-dask_image}
docker_file=${3:-Dockerfile_dask}
progress=${4:-auto}

docker build --progress=${progress} \
  -t dsimages/${image_repository}:${image_tag} \
  -f ./${docker_file}  . \
  && docker push dsimages/${image_repository}:${image_tag}
