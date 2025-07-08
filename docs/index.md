<div align="center" style="padding: 2rem 1rem; background: linear-gradient(to right, #1e3c72, #2a5298); color: white; border-radius: 12px; margin-bottom: 2rem;">
  <img src="/images/open-c3-logo.jpeg" alt="Open-C3 Logo" width="80" style="border-radius: 8px; margin-bottom: 1rem;" />
  <h1 style="margin: 0.5rem 0;">Open‑C3：开源一体化自动化运维平台</h1>
  <p style="font-size: 1.1rem; max-width: 600px; margin: auto;">
    集成 CMDB、监控、发布、流程、工单五大核心系统，支持多云环境，助力 DevOps 高效落地。
  </p>

  <!-- GitHub Star 按钮 -->
  <div style="margin-top: 1rem;">
    <iframe src="https://ghbtns.com/github-btn.html?user=open-c3&repo=open-c3&type=star&count=true&size=large"
      frameborder="0" scrolling="0" width="160" height="30" title="GitHub Star"></iframe>
  </div>

  <!-- CTA 文案 -->
  <p style="margin-top: 0.5rem;">👉 喜欢这个项目？点击上方按钮给我们一个 ⭐ Star 吧！</p>
</div>


Open-C3 是一个开源的自动化运维平台，包括 CMDB、监控系统、发布系统、工单系统、流程系统 等，同时各子系统之间相互联动。是一个一体化的自动化运维平台。
请查看[用户指南]以获得更多的信息。

[introductory tutorial]: getting-started.md
[用户指南]: user-guide/README.md

<div class="text-center">
<a href="getting-started/" class="btn btn-primary" role="button">快速开始</a>
<a href="user-guide/" class="btn btn-primary" role="button">用户指南</a>
</div>

---
<div class="pt-2 pb-4 px-4 my-4 bg-body-tertiary rounded-3">
<h2 class="display-8 text-center">✨ 平台特色</h2>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title">功能齐全</h3>
        <p class="card-text">
            Open-C3提供了运维环节中的多个子系统，如CMDB，监控系统、发布系统、工单系统、流程系统等。
            子系统功能强大，如CMDB可以管理AWS、华为云、阿里云、腾讯云、Ucloud、Openstack、Vmware、自建机房等资源。
            监控系统可以监控主机、Mysql、Redis、Mongodb、网站入口等。
            发布系统支持传统的主机发布、kubernetes发布、AWS ECS发布等。
        </p>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <h3 class="card-title">高度集成</h3>
        <p class="card-text">
            Open-C3提供的子系统自动联动，比如CMDB中导入云帐号后，可以通过流程系统创建云资源，
            云资源创建后会自动同步到CMDB，同时资源会根据标签自动挂到服务树上，挂树资源使监控模版自动生效、同时发布系统会自动重新对服务树上的资源进行重新分批。
            再如，监控系统中出现的告警，可以一键转成工单，通过工单进行跟进。
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
            系统通过插件的方式进行开发，包括CMDB中的资源同步、资源操作，发布系统的步骤、流程系统的动作都是插件。使得系统级易扩展。
        </p>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-body">
        <h3 class="card-title">易维护</h3>
        <p class="card-text">
            系统会高度的向后兼容，可以一键升级到最新版本，系统会自动调整如数据库表结构，使得系统能安全顺利升级到最新版本。
        </p>
      </div>
    </div>
  </div>
</div>
</div>

---
<div class="pt-2 pb-4 px-4 my-4 bg-body-tertiary rounded-3">
<h2 class="display-8 text-center"> 🚀 系统功能截图</h2>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/c3070a34-f1e4-42a9-b240-79056909e00b" alt="Open-C3 CMDB 首页"/>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/15aff287-4cf1-4eed-8567-65567020df07" alt="Open-C3 CMDB 查看单个资源详情"/>
      </div>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/ac21234e-71ec-49b3-9dd5-c02cf85ed1d8" alt="Open-C3 监控"/>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/45ba808d-6d89-4aac-b09b-cc6fef4bad33" alt="Open-C3 监控"/>
      </div>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/1d52a93f-6b12-46df-ba1c-cad46ea66793" alt="Open-C3 监控"/>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/e3f50373-115b-42f4-86a3-9bd5afa085b7" alt="Open-C3 监控"/>
      </div>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/584b374f-b3e0-4321-a5a6-96c7be3eeea1" alt="Open-C3 CICD"/>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/2bc1a7c2-07d9-4cf8-aa35-7e507cee5ef0" alt="Open-C3 CICD"   />
      </div>
    </div>
  </div>
</div>


<div class="row">
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/fd5a7401-0c4c-4218-b12a-905a59360423" alt="Open-C3 菜单"/>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card mb-4">
      <div class="card-body">
        <img src= "https://github.com/user-attachments/assets/9292eb7a-bba6-4477-af75-8c99f57af410" alt="Open-C3 工单"/>
      </div>
    </div>
  </div>
</div>

</div>


---

## 🙌 欢迎参与贡献

我们欢迎任何形式的贡献，包括但不限于：

- 提交 issue 或建议

- 改进文档

- 提交代码 PR

- 分享你的使用经验

👉 请参考 [贡献指南](/about/欢迎参与贡献/) 开始参与！
