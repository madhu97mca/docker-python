FROM python

WORKDIR /myapp

COPY ./Myapp.py .

COPY ./server.txt .


CMD ["python","Myapp.py"]