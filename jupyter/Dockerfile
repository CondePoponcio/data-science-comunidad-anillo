FROM jupyterlab:3.2.0-spark-3.2.0

RUN apt update

RUN python -m pip install --upgrade pip

RUN pip install psycopg2-binary sqlalchemy pyarrow numpy pandas==1.4.4 koala shapely
