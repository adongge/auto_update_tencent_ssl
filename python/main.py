import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ssl.v20191205 import ssl_client, models
from tencentcloud.apigateway.v20180808 import apigateway_client, models as apigateway_models
from config import domains
from datetime import datetime
import os
import time


def del_ssl(certificate_id):
    # 调用acme.sh脚本上传证书
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        SecretId = os.getenv("Tencent_SecretId")
        SecretKey = os.getenv("Tencent_SecretKey")
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ssl.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ssl_client.SslClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DeleteCertificateRequest()
        params = {
            "CertificateId": certificate_id
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DeleteCertificateResponse的实例，与请求对象对应
        resp = client.DeleteCertificate(req)

        # 输出json格式的字符串回包
        print(resp.to_json_string())

        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def get_ssl(search_key):
    # 调用acme.sh脚本上传证书
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        SecretId = os.getenv("Tencent_SecretId")
        SecretKey = os.getenv("Tencent_SecretKey")
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ssl.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ssl_client.SslClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeCertificatesRequest()
        params = {
            "SearchKey": search_key
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeCertificatesResponse的实例，与请求对象对应
        resp = client.DescribeCertificates(req)

        # 输出json格式的字符串回包
        print(resp.to_json_string())

        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def deploy_ssl_cdn(certificate_id, instance_id_list):
    # 调用acme.sh脚本上传证书
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        SecretId = os.getenv("Tencent_SecretId")
        SecretKey = os.getenv("Tencent_SecretKey")
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ssl.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ssl_client.SslClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DeployCertificateInstanceRequest()
        params = {
            "CertificateId": certificate_id,
            "InstanceIdList": instance_id_list,
            "ResourceType": 'cdn'
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个UploadCertificateResponse的实例，与请求对象对应
        resp = client.DeployCertificateInstance(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def upload_ssl(fullchain, private_key):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        SecretId = os.getenv("Tencent_SecretId")
        SecretKey = os.getenv("Tencent_SecretKey")
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ssl.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ssl_client.SslClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.UploadCertificateRequest()
        params = {
            "CertificatePublicKey": fullchain,
            "CertificatePrivateKey": private_key
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个UploadCertificateResponse的实例，与请求对象对应
        resp = client.UploadCertificate(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def modify_sub_domain(modify_params):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        SecretId = os.getenv("Tencent_SecretId")
        SecretKey = os.getenv("Tencent_SecretKey")
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "apigateway.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = apigateway_client.ApigatewayClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = apigateway_models.ModifySubDomainRequest()
        req.from_json_string(json.dumps(modify_params))

        print(['modify domain', modify_params])

        # 返回的resp是一个ModifySubDomainResponse的实例，与请求对象对应
        resp = client.ModifySubDomain(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


if __name__ == '__main__':

    for domain in domains:
        fullchain_path = f'/acme.sh/{domain.get("domain")}/fullchain.cer'
        privkey_path = f'/acme.sh/{domain.get("domain")}/{domain.get("domain")}.key'

        # 判断ssl文件生成时间是否更新
        if os.path.exists(fullchain_path) and os.path.exists(privkey_path):
            # 获取文件最后修改时间
            last_modified = os.path.getmtime(fullchain_path)
            # 获取当前时间
            current_time = time.time()
            # 判断文件是否更新
            print(f'{domain.get("domain")} update {(current_time - last_modified)/86400} days ago')
            if current_time - last_modified > 86400:
                print(f'SSL for {domain.get("domain")} not to update')
                print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} end =============================================== {domain.get("domain")}')
                continue
        else:
            print(f'SSL file is not exists {fullchain_path} or {privkey_path}')
            continue

        # 读取证书和私钥
        with open(fullchain_path, 'r') as f:
            fullchain = f.read()

        with open(privkey_path, 'r') as f:
            privkey = f.read()

        # 证书和私钥
        # print(fullchain)
        # print(privkey)
        if domain.get("type") == 'file':
            # 目录
            if not os.path.exists(f'/python/ssl/{domain.get("domain")}'):
                os.makedirs(f'/python/ssl/{domain.get("domain")}')

            target_fullchain_path = f'/python/ssl/{domain.get("domain")}/fullchain.cer'
            target_privkey_path = f'/python/ssl/{domain.get("domain")}/{domain.get("domain")}.key'
            # 复制文件到指定目录
            with open(target_fullchain_path, 'w') as f:
                f.write(fullchain)
            with open(target_privkey_path, 'w') as f:
                f.write(privkey)
                
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} copy file success {domain.get("domain")}\n')

        if domain.get("type") != 'file':
            old_ssl = get_ssl(domain.get("domain"))
            data = None
            # 上传证书
            # {"CertificateId": "EgkQqUr3", "RepeatCertId": "", "RequestId": "b7e7d9a4-e6fb-4d6a-a228-e521bbe7a669"}
            data = upload_ssl(fullchain, privkey)
            if data:
                CertificateId = data.get('CertificateId')
                if CertificateId is not None:
                    print(f'Uploaded SSL certificate for {domain.get("domain")}')
                    print(f'new CertificateId: {CertificateId}')
                    
                    # 部署证书到指定实例资源 cdn 或 apigateway
                    # cdn
                    if domain.get("type") == 'cdn':
                        deploy_ssl_cdn(CertificateId, [domain.get("domain")])

                    # apigateway
                    if domain.get("type") == 'apigateway':
                        modify_params = {
                            "ServiceId": domain.get("service_id"),
                            "SubDomain": domain.get("domain"),
                            "Protocol": "http&https",
                            "NetType": "OUTER",
                            "IsDefaultMapping": True,
                            "CertificateId": CertificateId
                        }

                        modify_sub_domain(modify_params)

                    if domain.get("type") in ['apigateway', 'cdn']:
                        if old_ssl is not None and len(old_ssl.get('Certificates')) > 0:
                            print(['old delete', old_ssl.get('Certificates')[0].get('CertificateId')])
                            old_certificate_id = old_ssl.get('Certificates')[0].get('CertificateId')
                            del_ssl(old_certificate_id)


        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} end =============================================== {domain.get("domain")}\n')
