- 前置 cdn https 开启，域名已添加
- 配置 域名-类型 cdn apigateway
- 请求获得证书 (第一次获取证书)
- 配置定时任务文件 /python/config.py


``` Bash
# 运行容器
docker run --rm  -itd  \
  -v "$(pwd)/acme":/acme.sh  \
  -v "$(pwd)/python":/python  \
  --env-file "$(pwd)/.env" \
  --net=host \
  --name=acme.sh \
  adddge/acme.sh:1.0 daemon

# 第一次获取证书 申请 ssl 生成文件
docker exec acme.sh --issue --dns dns_tencent -d xxx.xxx.com --standalone -m xxxx@aliyun.com

docker exec acme.sh --issue --dns dns_tencent -d xxx.xxx.com --standalone -m xxxx@aliyun.com

# 容器内
# 配置 /python/config.py 即可
# 定时任务每天执行，acme.sh 自动申请，当天有新的文件生成，python程序自动同步到腾讯云
# 定时任务详情 crontab -e

```