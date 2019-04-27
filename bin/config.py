# -*- coding: UTF-8 -*-
import os

# 路径配置
app_apk_output_path = '/home/ulfy/Projects/android-studio/dxMovie-android/app/build/outputs/apk'
jiagubao_jar_path = '/home/ulfy/Programs/walle-360-pack/360jiagubao_linux_64/jiagu/jiagu.jar'
walle='/home/ulfy/Programs/walle-360-pack/ProtectedApkResignerForWalle'

temp_dir = os.path.join(walle, 'temp')
output = os.path.join(walle, 'output')

# 账号配置
#       如果登录提示‘登录失败，获取缓存数据失败。需通过UI启动，进行验证码检测’，可在windows上登录之后将jiagu.db覆盖即可
#       如果通过windows登录后，本脚本不再需要重新登录
jiagubao_username='15546543905'
jiagubao_password='Bet@365365'