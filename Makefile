run:
	uv run project

build:
	docker buildx build -t excuser .

up:
	docker run -p 9000:9000 excuser
