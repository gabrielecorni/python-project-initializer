#!/bin/bash
source scripts/_conf.sh

echo "Cleaning $LOCAL_IMAGE..."
docker rmi -f $LOCAL_IMAGE

echo "Cleaning $REMOTE_IMAGE..."
docker rmi -f $REMOTE_IMAGE

echo "Success"