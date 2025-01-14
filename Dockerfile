FROM python

WORKDIR /myapp

COPY ./Add.py .

CMD['python','Add.py']