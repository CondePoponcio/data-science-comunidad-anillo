cant=$1
psql -U felipe -W -d citylog -h localhost -f $(pwd)/query1.sql | split -a 6 -l $1 -d --verbose --additional-suffix=.csv