#!/bin/bash
source scripts/_conf.sh

echo "Building $LOCAL_IMAGE..."

docker build \
    -f docker/Dockerfile \
    -t $LOCAL_IMAGE \
    --build-arg ARG_ONE="foo" \
    --build-arg ARG_TWO="bar" \
    .

echo "Success"