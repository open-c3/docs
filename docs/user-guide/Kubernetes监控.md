
# 1 Kubernetes监控

简介

KUBERNETES监控部分更多的是统一管理。目前Kubernetes有很多监控方案，包括如果使用的是公有云上的Kubernetes，云上也可以配置对应的监控。但是这个太分散了，我们需要把它聚合到一起。需要在监控看板上看到这些监控告警。

## 1.1 安装和配置

安装kube-prometheus

打开下面github的项目，在Kubernetes集群中安装普罗米修斯的监控套件。

[https://github.com/prometheus-operator/kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)

端口对外开放访问

安装完后，确保安装在集群中的普罗米修斯的端口对外可以访问，Open-C3会通过这个端口把数据汇总到Open-C3服务的普罗米修斯中。

![](file:////Users/feng/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-feng/ksohtml//wps44.jpg) 

如果默认没有对外开放，可以手动添加一个映射：

![](file:////Users/feng/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-feng/ksohtml//wps45.jpg) 

在云监控中配置采集

进到“管理”-> “云监控”页面，点击添加云监控。

![](file:////Users/feng/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-feng/ksohtml//wps46.jpg) 

采集添加后，Open-C3上的普罗米修斯就会把Kubernetes中普罗米修斯的数据实时的同步到Open-C3上。

## 1.2 添加监控策略

![](file:////Users/feng/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-feng/ksohtml//wps47.jpg) 

导入后可以看到监控策略，在该服务树上订阅告警。

## 1.3 监控看板

打开下面目录，导入对应看板：

[https://github.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/kubernetes](https://github.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/kubernetes)

注：国内地址：

[https://gitee.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/kubernetes](https://gitee.com/open-c3/open-c3-guide/tree/main/attachments/monitor/grafana/kubernetes)

![](file:////Users/feng/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-feng/ksohtml//wps48.jpg) 

## 1.4 总结

 Kubernetes 中的应用，Kubernetes会调度使得应用状态是我们期望的样子。这里的监控更多的是监控POD有没有频繁重启、POD运行数量是不是持续没达到预期的数量。