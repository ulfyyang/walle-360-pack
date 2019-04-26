#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)
source ${basepath}/envirnment.sh

# 打包
./gradlew clean
./gradlew assembleRelease

# 删除原有文件并拷贝到临时目录
rm -f ${TEMP}/*
cp `find ${APP_APK_PATH} -name '*release.apk'` ${TEMP}