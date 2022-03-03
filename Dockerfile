FROM python:3

WORKDIR /app

COPY ./src .

RUN pip install psutil
EXPOSE 5500

CMD [ "python3", "./main.py" ]