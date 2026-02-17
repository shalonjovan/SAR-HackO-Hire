#!/bin/bash

echo "Starting PostgreSQL service..."
sudo systemctl start postgresql

echo "Running setup script..."
sudo -u postgres psql -f setup_db.sql

echo "Database setup complete."
