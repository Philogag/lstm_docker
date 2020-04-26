FROM python:3.7

WORKDIR /lstm

COPY . ./

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple &&\
    pip3 install -r requirements.txt

ENV FLASK_APP=main.py

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]

