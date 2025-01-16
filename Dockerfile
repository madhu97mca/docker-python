FROM python

WORKDIR /myapp

COPY ./api_demo.py  .




CMD ["python","api_demo.py"]