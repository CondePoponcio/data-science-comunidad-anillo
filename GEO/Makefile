
extract-%:
        ./psql.sh $(@:extract-%=%)

clean:
        rm -f ./x*
connect:
        psql -U felipe -W -h localhost -d citylog 