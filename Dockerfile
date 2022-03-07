FROM python:3

ENV NAMESPACE="" \
	SERVICE=""

WORKDIR /app

COPY ./src .

RUN pip install psutil
EXPOSE 8080

CMD [ "python3", "main.py" ]