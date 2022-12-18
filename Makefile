database-cli:
	docker compose exec db psql -U postgres -d datascience -W -h localhost
database-bash:
	docker compose exec db bash
build:
	docker compose build
	docker compose create
	docker compose start
delete:
	docker compose down -v --remove-orphans

rmi:
	docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi --force

upload-csv:
	docker compose cp ./build/workspace/data/ db:/tmp/data