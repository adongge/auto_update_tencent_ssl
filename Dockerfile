FROM neilpang/acme.sh:latest

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories && \
apk add python3 && \
python3 -m ensurepip && \
pip3 install tencentcloud-sdk-python -i https://pypi.tuna.tsinghua.edu.cn/simple

# docker build -t adddge/acme.sh:1.0 .

# 30 1 * * * /python/run.sh >>/python/logs/py_$(date +\%Y\%m).log 2>&1