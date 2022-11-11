# Usage: use only for the local docker compose development env and make sure the database imgae is up and running

# Set database configurations
export CT_DB_USERNAME=ct_admin
export CT_DB_NAME=geoconnections
export PGPASSWORD=wowimsosecure

cat ./db/2020-08-15_init-db.sql | psql -h localhost -U $CT_DB_USERNAME -d $CT_DB_NAME

cat ./db/udaconnect_public_person.sql | psql -h localhost -U $CT_DB_USERNAME -d $CT_DB_NAME

cat ./db/udaconnect_public_location.sql | psql -h localhost -U $CT_DB_USERNAME -d $CT_DB_NAME
