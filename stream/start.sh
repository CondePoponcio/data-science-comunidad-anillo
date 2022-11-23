cat ../buses/x*.csv > buses.csv
echo "Merged csv's from buses ..."

cat ../paraderosrutas/x*.csv > paraderosrutas.csv
echo "Merged csv's from paraderosrutas ..."

echo "Init python program. Processing data ..."
python script.py