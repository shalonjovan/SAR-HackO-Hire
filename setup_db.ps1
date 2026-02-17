Write-Host "Running PostgreSQL setup..."

# Change this if your PostgreSQL bin path is different
$psqlPath = "psql"

# If psql is not in PATH, use something like:
# $psqlPath = "C:\Program Files\PostgreSQL\18\bin\psql.exe"

# Run setup script as postgres superuser
& $psqlPath -U postgres -f setup_db.sql

if ($LASTEXITCODE -eq 0) {
    Write-Host "Database setup completed successfully."
} else {
    Write-Host "Database setup failed."
}
