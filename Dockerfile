FROM python:3.11

WORKDIR /code

COPY . /code/

#COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#COPY . /code/

CMD ["uvicorn", "src.finshmlserv.main:app", "--host", "0.0.0.0", "--port", "8080"]
