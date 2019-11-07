USER = $(shell docker info | sed '/Username:/!d;s/.* //')
TAG = $(shell git describe --abbrev=0)
IMAGE_NAME = irishrail-logger

# Building
build-image:
	docker build -t $(USER)/$(IMAGE_NAME) --rm .

build-image-tag:
	docker build -t $(USER)/$(IMAGE_NAME):$(TAG) --rm .

# Pushing
push-image:
	docker push $(USER)/$(IMAGE_NAME)

push-image-tag:
	docker push $(USER)/$(IMAGE_NAME):$(TAG)

# Running
run-image:
	docker run -itd --net=host --env-file=.env --name=ir-logger-instance $(USER)/$(IMAGE_NAME)

run-image-tag:
	docker run -itd --net=host --env-file=.env --name=ir-logger-instance $(USER)/$(IMAGE_NAME):$(TAG)

# Testing
test-image: build-image run-image
