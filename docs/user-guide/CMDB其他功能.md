
# 1. CMDB其他功能

## 1.1 历史全局搜索

CMDB会定时备份全量数据，我们可以选择在某个历史时间中查看和搜索CMDB中的资源。但是如果我们得到一个ip，比如 10.10.10.10，我们想查询这个ip是否在CMDB中曾经出现过，就可以通过历史全局搜索功能进行搜索。

![](/attachments/Pasted_image_20251206174049.png)


![](/attachments/Pasted_image_20251206174106.png)

![](/attachments/Pasted_image_20251206175124.png)

## 1.2 资源配置变更提醒

成本优化过程中，有时候我们需要关注资源的配置变更。 比如有的云资源会动态升级。为了让我们关注到这个事件。 OPEN-C3会每5分钟检测异常资源配置的变动情况。如果有资源升级配置或者降低配置了，会通知 open-c3-fee 这个用户。 下面以open-c3-fee配置飞书为例。

1.2.1 配置用户 open-c3-fee

![](/attachments/Pasted_image_20251206230918.png)


1.2.2 当资源发生升配或者降配时，会通知  open-c3-fee 用户。下面是open-c3-fee在资源变动时收到的飞书消息。

![](/attachments/Pasted_image_20251206232102.png)

## 1.3 证书过期通知

ssl-certificate-expired-notify 任务会每天检查cmdb中的证书是否将要过期，如果发现即将过期的证书通知告警组@cmdb_notify_ssl_expired