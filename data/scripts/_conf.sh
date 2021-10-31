# list of configuration env variables to inject into containers

# set public variables
CONTAINER_NAME="my-container-name"
IMAGE_NAME="my-image"
IMAGE_VERS="master-latest"

PUBLIC_VAR="Hello, World!"

# omit private variables 
#   - copy this template 
#   - rename it 
#   - source it
#   - don't put the copy under version control!
REGISTRY_NAME=
REGISTRY_USER=
REGISTRY_PASS=

SECRET_VAR=

# compose image tags
LOCAL_IMAGE="$IMAGE_NAME:$IMAGE_VERS"
REMOTE_IMAGE="$REGISTRY_NAME/$REGISTRY_USER/$LOCAL_IMAGE"