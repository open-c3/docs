# docs

本项为open-c3的官网地址，发布在https://open-c3.github.io 和 https://www.open-c3.online

项目的markdown文件使用Obsidian进行编辑，使用Mkdocs生成目标html文件。

## Obsidian

```
Obisidian 把本项目的docs目录作为一个项目进行编辑。

配置注意： 把 “文件与链接” 中的附件路径， 选择“指定的附件文件夹”的“attachments”。

在编辑Markdown文件的文件的过程中，可以直接粘贴图片，也可以直接用WPS打开word文件往Markdown中粘贴。
如果有如上两个操作需要执行./fix.sh 进行文件修复。
fix.sh 会把WPS文件中的图片复制到项目的附件目录中。会修复粘贴到markdown中的图片名称和路径。

```

## Mkdocs

```
执行./serve.sh可以在本地启动服务。实时查看和调试。

```

## 发布

### 发布到github和官网

```
执行./deploy.sh 进行发布。

发布到国内官网的过程中，国内网络访问不了github，需要在发布之后在国内官网的机器上执行fix-assets.sh进行路径修复（deploy.sh自动调用）。
因为有的图片是来之与github的issue，这样图片有加速功能。但是国内访问不了，修复过程会把图片下载到本地路径，同时修复html中的路径。

```

### 发布到Open-C3的项目的代码中的book中

```
在发布代码过程中，需要把fix-assets.sh和fix-assets-book.sh放到项目目标项目中。
在Open-C3对book打包的时候，需要执行这两个脚本。
这两个脚本会修复github issus中的图片问题，同时会修复因为book是放在 /book/ 路径导致访问资源路径不对的问题。
```

# 关于文件路径修复问题

为什么不写相对的路径？ 这样就不需要修复文件路径了。

```
1. Obsidian 和 Mkdocs 对文件路径的深度定义不一致。 比如定义了一个文件 /foo/bar.md , 在mkdos生成的html，路径可能/foo/bar/，导致不能使用统一的相对对路径 。
2. 在Obsidian中粘贴图片。或者粘贴work文档的内容，图片附件的路径是固定的，不会因为文件目录路径深度不一样的到特殊处理， 也就是Obsidian不识别文件路径深度。

[粘贴一个图片，Obsidian总是只显示图片的名称，没有任何路径，粘贴word文档的内容，总是一个绝对路径]

为了解决上面的问题，目前图片资源的访问都使用 “/” 开头的绝对路径。

js、css之类的怎么办？

对于js、css等，因为完全是由Obsidian控制的，它会根据能生成正确的路径 比如js， 在不同的文件是，可能是 js/xxx.js ../js/xxx.js ../../js/xxx.js，所以不存在这样的问题。

```
