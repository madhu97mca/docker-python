FROM python

WORKDIR /myapp

COPY ./Add.py .

CMD ["python","user_info.py","python","Add.py"]