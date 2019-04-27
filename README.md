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

1. 在AndroidStudio中clean打release包
2. 在根目录下bin目录中执行python jiagu360.py加固，相关的包会在ProtectedApkResignerForWalle/temp中
3. 在根目录下bin目录中执行python shengchengqudao.py加入渠道，相关的包会在ProtectedApkResignerForWalle/output中

> 注意：有的时候下载进度一直是0，这有可能时360程序的错误，应当关注加固的包的体积是否在一直增加，网速是否一直在走来确认是否加固失败