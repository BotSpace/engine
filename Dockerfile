FROM python:3.13-alpine

WORKDIR /code


COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["sh", "./entrypoint.sh"]
