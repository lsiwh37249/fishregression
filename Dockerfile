FROM python:3.11

WORKDIR /code

COPY src/fishregression/main.py /code/

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#COPY . /code/

CMD ["uvicorn", "src.fishregression.main:app", "--host", "0.0.0.0", "--port", "8080"]
