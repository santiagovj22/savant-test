#!/bin/sh

# Set the database URI
export DATABASE_URL="postgresql://root:toor@localhost:5433/postgres"

echo "\nBefore Migration"
flask db upgrade

echo "\nRunning Migration"
flask db migrate -m "Initial migration"

echo "\nAfter Migration"
flask db upgrade

echo "\nMigration Graph"
flask db history
