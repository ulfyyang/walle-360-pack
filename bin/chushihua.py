#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, shutil
import config

app_release_files = []

# 收集release包
for root, dirs, files in os.walk(config.app_apk_output_path):
    for file_name in files:
        if 'release' in file_name:
            app_release_files.append(os.path.join(root, file_name))

# 拷贝到临时目录
if os.path.exists(config.temp_dir):
    shutil.rmtree(config.temp_dir)
os.mkdir(config.temp_dir)
for release_file in app_release_files:
    shutil.copy(release_file, config.temp_dir)