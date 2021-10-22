# HTTPS



HTTP缺点

1. 通信不加密，使用明文，内容可能被窃听
2. 不验证通信方的身份，因此有可能遭遇伪装
3. 无法证明报文的完整性，因为有可能遭到篡改

> `POST`提交的数据是放在报文主体里看不到的，但是可以通过抓包工具窃取到内容

## 通信加密

HTTPS

- HTTP+SSL
  - SSL：Secure Socket Layer 安全套接字层
    - 用SSL建议安全通信线路（对整个通信线路加密）
    - HTTP Secure/HTTP over SSL

- HTTP+TLS
  - TLS：Transport Layer Security 安全传输层协议
  - TLS是SSL的升级版本

> 还有一种方法是对HTTP报文主体进行加密，但是没有对通信线路进行整个加密，还是不安全
>
> HTTP先与SSL通信，SSL再和TCP通信

## 证书

证书由值得信任的第三方机构颁发

## 中间人攻击

MITM：Man-in-the-Middle attack

- 请求或响应在传输途中，被攻击者拦截并篡改内容



**HTTPS = HTTP+加密+认证+完整性保护**

## 交换密钥

公开密钥加密：Public-key-cryptography