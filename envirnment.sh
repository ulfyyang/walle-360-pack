#!/usr/bin/env bash

# 路径配置
APP_APK_PATH='/home/ulfy/Projects/android-studio/dxMovie-android/app/build/outputs/apk'
JIAGUBAO_PATH='/home/ulfy/Programs/walle-360-pack/360jiagubao_linux_64/jiagu'
TEMP='/home/ulfy/Programs/walle-360-pack/ProtectedApkResignerForWalle/temp'
REWALLE='/home/ulfy/Programs/walle-360-pack/ProtectedApkResignerForWalle'
OUTPUT='/home/ulfy/Programs/walle-360-pack/ProtectedApkResignerForWalle/output'

# 账号配置
#       如果登录提示‘登录失败，获取缓存数据失败。需通过UI启动，进行验证码检测’，可在windows上登录之后将jiagu.db覆盖即可
#       如果通过windows登录后，本脚本不再需要重新登录
JIAGUBAO_USERNAME='15546543905'
JIAGUBAO_PASSWORD='Bet@365365'