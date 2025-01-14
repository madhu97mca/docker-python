FROM python

WORKDIR /myapp

COPY . .

CMD ["python","user_info.py","python","Add.py"]