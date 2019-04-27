#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, shutil, threading, time
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


# 执行360加固

class Dabao360Thread(threading.Thread):
    JIAGU_COMMAND = 'java -jar ' + config.jiagubao_jar_path + ' -jiagu %s ' + config.temp_dir

    def __init__(self, releaseApkPath):
        threading.Thread.__init__(self)
        self.releaseApkPath = releaseApkPath

    def run(self):
        os.system(Dabao360Thread.JIAGU_COMMAND % self.releaseApkPath)
        print(self.releaseApkPath)


for release_apk_file in os.listdir(config.temp_dir):
    time.sleep(5)
    Dabao360Thread(os.path.join(config.temp_dir, release_apk_file)).start()
