FROM python:3.7-alpine

COPY . .

CMD cat samples/sample.txt | python3 app.py