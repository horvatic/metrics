FROM python:3

ENV NAMESPACE="" \
	SERVICE=""

WORKDIR /app

COPY ./src .

EXPOSE 8080

CMD [ "python3", "main.py" ]