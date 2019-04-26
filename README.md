# 配置

## 需要配置envirnment.sh中的环境

- APP_APK_PATH              AndroidStudio的apk输出绝对路径
- JIAGUBAO_PATH             加固宝绝对路径
- TEMP                      临时文件夹绝对目录
- REWALLE                   WALLE重新打包的绝对路径
- OUTPUT                    最终输出目录

---------------

- JIAGUBAO_USERNAME       加固宝登录名
- JIAGUBAO_PASSWORD       加固宝登录密码

## config.py中的环境

将签名文件拷贝到config文件夹中，并配置签名信息

- extraChannelFilePath    如果使用额外信息方式打包的配置文件绝对路径
- sdkBuildToolPath        sdk绝对路径

# 运行

在工程根目录下以绝对路径的方式运行dabao.sh && jiagu.sh && shengchengqudao.sh，这些命令需要配置到path路径中。

最终会在output下生成渠道包。


- dabao.sh会生成apk并拷贝到temp临时目录
- jiagu.sh会使用360加固进行加固
- shengchengqudao.sh会写入渠道信息
