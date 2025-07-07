
# 1 ping监控


在企业环境中，我们需要监控监控网络的延迟和丢包情况。

## 1.1 配置
---


### 配置/源

**配****置**

源是发起ping的主机节点。

在 src 目录下，存放源主机分组，每个文件是一个分组，文件每行是个ip或者域名

例子:
```
[root@open-c3]# ls src
cloud-aws-afs
cloud-huawei-open-c3
[root@open-c3]# cat src/cloud-huawei-open-c3
openc3-fping
[root@open-c3]# cat src/cloud-aws-afs
10.10.10.111
10.10.10.112
```

在源机器上启动容器

```
docker run -d --restart=always -p 9605:9605 --name openc3-fping joaorua/fping-exporter fping-exporter --fping=/usr/sbin/fping -c 10
```


ACL

开放访问权限，让Open-C3机器访问源机器的9605端口

---

### 配置/目标

目标

目标是要ping的对象，放在dst目录下，每个文件是一个分组。格式和源一样

配置/采集

配置采集

```
conf.yml配置着需要采集的任务，是个yaml格式
key是src中源的名称
valus 是个数组，数组中的元素是目标的名称，或者一个正则表达式匹配目标中的名称。
      特殊情况，当value是 '*' 时表示所有目标组

例子:
# cat conf.yml
cloud-huawei-open-c3:       [ '/country/', '/website/', '/cloud/', '/workplace/' ]
cloud-ucloud-ng:            [ '/country/', '/website/' ]
cloud-huawei-afs:           [ '/cloud/' ]
cloud-aws-afs:              [ '/country/' ]
cloud-aliyun-frankfurt:     '*'
```

配置/生成普罗米修斯配置

生成普罗米修斯配置文件

到容器中该目录下执行 ./make.sh 命令

## 1.2 导入看板

打开下面目录，导入对应看板：

[https://github.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/fping](https://github.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/fping)

注：国内地址：

[https://gitee.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/fping](https://gitee.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/fping)

![](/attachments/20250706223400_wps51.jpg) 
Ping监控在分组起名的时候，用“-”号分隔。 第一个段为分组。

## 1.3 总结

该ping监控可以监控到全局的网络延迟和丢包情况。但是有个弊端，如果Open-C3到源机器丢包严重，可能会采集不到数据。如果有这个担忧可以在源机器上安装kuma程序进行补充监控。

```sh
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```
