file="$(ls | grep x)"

if [ -n "$file" ];
then
        echo "Removing previus CSV Files..."
        make clean
fi
echo "Start extracting data ... "
make extract-$1
df -h
echo "Finish proccess. Goodbye ..."