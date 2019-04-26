#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)
source ${basepath}/envirnment.sh

cd ${REWALLE}

for APK_PATH in `ls ${TEMP}/*_jiagu.apk`
do
    # 生成渠道文件
    cp ${APK_PATH} ${TEMP}/app-release-jiagu.apk
    python ApkResigner.py
    rm ${TEMP}/app-release-jiagu.apk
    # 将文件放到对应的文件夹下
    APK_NAME=`echo ${APK_PATH##*/} | cut -d '-' -f2`
    mkdir ${OUTPUT}/${APK_NAME}
    mv ${OUTPUT}/app-release-jiagu_aligned_signed_* ${OUTPUT}/${APK_NAME}
    rename 's/app-release-jiagu_aligned_signed_//g' ${OUTPUT}/${APK_NAME}/*
done