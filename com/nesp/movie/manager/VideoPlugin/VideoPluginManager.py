#  Copyright (c) 2020  NESP Technology Corporation. All rights reserved.
#
#    This program is free software; you can redistribute it and/or modify it
#    under the terms and conditions of the GNU General Public License,
#    version 2, as published by the Free Software Foundation.
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License.See the License for the specific language governing permissions and
#    limitations under the License.
#
#    If you have any questions or if you find a bug,
#    please contact the author by email or ask for Issues.
#
#    Author:JinZhaolu <1756404649@qq.com>

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/26 7:50
Project: FishMovieManagerTools
Description:
"""
import os
from os import path
from com.nesp.movie.manager.VideoPlugin.utils import PluginUtils
import json


class VideoPluginManager:

    def __init__(self, root_path, plugin_index_file_name):
        self.rootPath = root_path
        self.pluginIndexFileName = plugin_index_file_name
        self.pluginIndexFilePath = path.join(self.rootPath, self.pluginIndexFileName)
        self.pluginPackageDirPath = path.join(self.rootPath, "pluginPackages")

    def __getVideoInfoPath(self, video_plugin_info1):
        return path.join(self.rootPath, video_plugin_info1.name).join(".json")

    def addVideoPlugin(self, video_plugin_info):
        """
        :param video_plugin_info: VideoPluginInfo
        :return:
        """
        video_plugin_index_file = open(self.pluginIndexFilePath)
        plugin_info_path = self.__getVideoInfoPath(self, video_plugin_info)
        video_plugin_info_file = open(plugin_info_path)

        if path.exists(path.abspath(plugin_info_path)):
            try:
                os.remove(plugin_info_path)
            except Exception:
                print("failed to delete plugin info file\n")

        if not path.exists(self.pluginIndexFilePath):
            video_plugin_index = PluginUtils.videoPluginInfo2VideoPluginIndex(video_plugin_info)
            try:
                video_plugin_info_file.write(json.dumps(video_plugin_info))
                video_plugin_index_file.write([video_plugin_index])
            except IOError:
                print("Raise IOError when write file")
        else:
            video_plugin_index_list = json.loads(video_plugin_index_file.read())
            video_plugin_index = PluginUtils.videoPluginInfo2VideoPluginIndex(video_plugin_info)

            # If there are duplicate IDs, delete the old ones first
            video_plugin_index_list = [video_plugin_index_list[i] for i in range(len(video_plugin_index_list)) if
                                       (video_plugin_index_list[i].name != video_plugin_index.name)]

            # Add new VideoPluginIndex
            video_plugin_index_list.append(video_plugin_index)
            try:
                video_plugin_info_file.write(json.dumps(video_plugin_info))
                video_plugin_index_file.write(json.dumps(video_plugin_index_list))
            except IOError:
                print("Raise IOError when write file")

        try:
            video_plugin_index_file.close()
            video_plugin_info_file.close()
        except IOError:
            print("Raise IOError when file closed")

    def deleteVideoPlugin(self, video_plugin_info):
        video_plugin_index_file = open(self.pluginIndexFilePath)
        video_plugin_info_path = self.__getVideoInfoPath(self, video_plugin_info)

        if path.exists(self.pluginIndexFilePath):
            try:
                video_plugin_index_list = json.loads(video_plugin_index_file.read())

                # remove from index
                video_plugin_index_list = [video_plugin_index_list[i] for i in range(len(video_plugin_index_list)) if
                                           (video_plugin_index_list[i].name != video_plugin_info.name)]
                video_plugin_index_file.write(json.dumps(video_plugin_index_list))
                video_plugin_index_file.close()

                # delete video plugin info file
                if path.exists(video_plugin_info_path):
                    os.remove(video_plugin_info_path)
            except IOError:
                print("delete video plugin file:%s failed!" % {video_plugin_info.name})
