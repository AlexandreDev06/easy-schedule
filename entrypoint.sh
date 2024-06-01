#!/bin/bash

echo "Running Migrations"
alembic upgrade head

echo "Running Server"
uvicorn app:app --reload --host 0.0.0.0