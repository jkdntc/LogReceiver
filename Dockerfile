FROM python:3.6.0-slim

#RUN pip install --upgrade pip
#RUN pip3 install -U setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip3 install japronto -i https://pypi.tuna.tsinghua.edu.cn/simple/
#RUN pip3 install https://github.com/squeaky-pl/japronto/archive/master.zip -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip3 install confluent-kafka[avro] -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY src/*.py /src/

CMD ["python3","/src/LogReceiver.py"]

EXPOSE 8080