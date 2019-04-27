# 配置

## 配置根目录下bin/config.py

- app_apk_output_path       AndroidStudio生成release包的output/apk绝对路径
- jiagubao_jar_path         根目录下加固保中的jiagu.jar绝对路径，根据平台选择对应的版本
- walle                     根目录下ProtectedApkResignerForWalle的绝对路径

## 配置根目录下ProtectedApkResignerForWalle/config.py

将签名文件拷贝到config文件夹中，并配置签名信息

- extraChannelFilePath    如果使用额外信息方式打包的配置文件绝对路径
- sdkBuildToolPath        sdk绝对路径

# 运行

1. 通过AndroidStudio打release包
2. 在根目录下bin目录中执行python jiagu360.py加固，相关的包会在ProtectedApkResignerForWalle/temp中
2. 在根目录下bin目录中执行python shengchengqudao.py加入渠道，相关的包会在ProtectedApkResignerForWalle/output中
