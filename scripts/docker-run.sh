#!/bin/bash
source scripts/_conf.sh

echo "Running $LOCAL_IMAGE..."

docker run \
    -it \
    --rm \
    --name $CONTAINER_NAME \
    --hostname $CONTAINER_NAME \
    --env PUBLIC_VAR="$PUBLIC_VAR" \
    --env SECRET_VAR="$SECRET_VAR" \
    $LOCAL_IMAGE