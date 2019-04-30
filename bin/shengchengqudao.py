#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, shutil
import config

os.chdir(config.walle)

if os.path.exists(config.output):
    shutil.rmtree(config.output)
os.mkdir(config.output)

for apk_file_name in os.listdir(config.temp_dir):
    shutil.copy(os.path.join(config.temp_dir, apk_file_name), os.path.join(config.temp_dir, 'app-release-jiagu.apk'))
    os.system('python ApkResigner.py')
    os.remove(os.path.join(config.temp_dir, 'app-release-jiagu.apk'))

    # 将文件放到对应的文件夹下
    apk_name = apk_file_name.split('-')[1]
    if 'jiagu' in apk_file_name:
        apk_name = apk_name + '_jiagu'
    print(apk_name)
    if not os.path.exists(os.path.join(config.output, apk_name)):
        os.mkdir(os.path.join(config.output, apk_name))
    for jiagu_qudao_apk in [apk for apk in os.listdir(config.output) if 'app-release-jiagu_aligned_signed_' in apk]:
        shutil.move(os.path.join(config.output, jiagu_qudao_apk), os.path.join(config.output, apk_name))
    # 重命名目标文件
    for jiagu_qudao_apk in os.listdir(os.path.join(config.output, apk_name)):
        shutil.move(os.path.join(config.output, apk_name, jiagu_qudao_apk), os.path.join(
            config.output, apk_name, jiagu_qudao_apk.replace('app-release-jiagu_aligned_signed_', '')))
