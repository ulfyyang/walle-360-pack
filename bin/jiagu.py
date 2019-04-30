#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, threading, time
import config

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
