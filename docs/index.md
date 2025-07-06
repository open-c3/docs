<div align="center">
  <a name="readme-top"></a>
  <a><img src="/open-c3-logo.jpeg" alt="Open-C3" width="50" /></a>
   一个开源的 自动化运维 平台 (DevOps)
</div>
<br/>

# Open-C3
---

Open-C3 是一个开源的自动化运维平台，功能包括 CMDB、监控系统、发布系统、工单系统、流程系统 等，同时各子系统之间自动联动。是一个一体化的自动化运维平台。
请查看[用户指南]以获得更多的信息。

[introductory tutorial]: getting-started.md
[用户指南]: user-guide/README.md

<div class="text-center">
<a href="getting-started/" class="btn btn-primary" role="button">快速开始</a>
<a href="user-guide/" class="btn btn-primary" role="button">用户指南</a>
</div>

<div class="pt-2 pb-4 px-4 my-4 bg-body-tertiary rounded-3">
<h2 class="display-4 text-center">特色</h2>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title">功能齐全</h3>
        <p class="card-text">
            Open-C3提供了运维环节中的多个子系统，如CMDB，监控系统、发布系统、工单系统、流程系统等。
            每个子系统功能强大，如CMDB可以管理AWS、华为云、阿里云、腾讯云、Ucloud、Openstack、Vmware、自建机房等资源。
            监控系统可以监控主机、Mysql、Redis、Mongodb、网站入口等。
            发布系统支持传统的主机发布、kubernetes发布、AWS ECS发布 等。
        </p>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title">高度集成</h3>
        <p class="card-text">
            Open-C3提供的多个子系统自动进行联动，比如CMDB中导入云帐号后，可以通过流程系统创建云资源，
            云资源创建后会自动同步到CMDB，同时资源会根据标签自动挂载服务树，挂载服务树后，监控模版会自动生效、发布系统会自动重新对服务树下的资源进行重新分批。
            在如，监控系统中出现的告警，可以一键转成工单，通过工单进行跟进。
        </p>
      </div>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h3 class="card-title">易扩展</h3>
        <p class="card-text">
            系统通过插件的方式进行开发，包括CMDB中的资源同步、资源操作，发布系统的步骤、流程系统的动作都是插件。
        </p>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h3 class="card-title">易维护</h3>
        <p class="card-text">
            系统会高度的向后兼容，可以一键升级到最新版本，系统会自动调整包括数据库表结构，以让系统能安全顺利的升级到最新版本。
        </p>
      </div>
    </div>
  </div>
</div>
</div>
