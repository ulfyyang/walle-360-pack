#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)
source ${basepath}/envirnment.sh

#${JIAGUBAO_PATH}/java/bin/java -jar ${JIAGUBAO_PATH}/jiagu.jar -login ${JIAGUBAO_USERNAME} ${JIAGUBAO_PASSWORD}

# 360加固

start_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`

for APK_PATH in `ls ${TEMP}/*`
do
    ${JIAGUBAO_PATH}/java/bin/java -jar ${JIAGUBAO_PATH}/jiagu.jar -jiagu ${APK_PATH} ${TEMP}
done

finish_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`
duration=$(($(($(date +%s -d "$finish_time")-$(date +%s -d "$start_time")))))

echo "加固用时: ${duration}秒"