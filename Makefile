.PHONY: test
.NOTPARALLEL:
test: 
	python3 -m unittest discover -p "*_test.py"

.PHONY: build
.NOTPARALLEL:
build: test
	docker build . --tag="metrics:latest"

.PHONY: run
run: build
	docker run -p 5500:8080 -d --name=metrics metrics

.PHONY: stop
stop:
	docker container stop metrics
	docker container rm metrics

.PHONY: clean-image
clean-image:
	docker image rm metrics

.PHONY: clean
clean: stop clean-image