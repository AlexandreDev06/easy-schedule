init:
	cp .env.example .env

install:
	poetry install

migrate:
	docker compose exec -it api alembic upgrade head

downgrade:
	docker compose exec -it api alembic downgrade -1

docker-up:
	docker compose -d up

docker-down:
	docker compose -d down

run:
	poetry run uvicorn app:app

terminal:
	docker compose exec -it api bash

clean:
	rm -rf .venv __pycache__ .pytest_cache .coverage .mypy_cache

add-migration:
	docker compose exec api alembic revision --autogenerate -m "$(name)"

add-lib:
	docker compose exec api poetry add $(name)

format:
	docker compose exec api ruff format

.DEFAULT_GOAL := help

# Help command
help:
	@echo "Available targets:"
	@echo "  init           - Copy .env.example to .env"
	@echo "  install        - Install project dependencies"
	@echo "  migrate        - Apply database migrations"
	@echo "  downgrade      - Revert the last database migration"
	@echo "  docker-up      - Start the Docker containers"
	@echo "  docker-down    - Stop the Docker containers"
	@echo "  run            - Run the application"
	@echo "  terminal       - Open a terminal inside the Docker container"
	@echo "  clean          - Remove temporary files and caches"
	@echo "  add-migration  - Generate a new Alembic migration"
	@echo "  add-lib        - Add a new library to the project"
	@echo "  format         - Format the code using Ruff"
	@echo "  help           - Show this help message"
