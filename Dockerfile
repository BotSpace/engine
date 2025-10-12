FROM python:3.13-slim

WORKDIR /code


COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]

