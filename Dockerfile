FROM python:3.8.12-slim-buster
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /home/workspace
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir  -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
                                 -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt

COPY . .

CMD ["python","main.py"]