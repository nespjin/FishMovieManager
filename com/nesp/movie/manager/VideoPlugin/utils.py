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
Time: Created 2020/4/26 0:53
Project: FishMovieManagerTools
Description:
"""
from com.nesp.movie.manager.VideoPlugin.entity import VideoPluginIndex


class PluginUtils:
    """Utils for Plugin"""
    @staticmethod
    def videoPluginInfo2VideoPluginIndex(video_plugin_info):
        """ Convert VideoPluginInfo to VideoPluginIndex
        :param video_plugin_info: VideoPluginInfo
        :return: VideoPluginIndex
        """
        video_plugin_index = VideoPluginIndex()
        video_plugin_index.author = video_plugin_info.author
        video_plugin_index.introShort = video_plugin_info.introShort
        video_plugin_index.updateTime = video_plugin_info.updateTime
        video_plugin_index.supports = video_plugin_info.supports
        video_plugin_index.name = video_plugin_info.name
        video_plugin_index.tags = video_plugin_info.tags
        video_plugin_index.vipCode = video_plugin_info.vipCode
        video_plugin_index.verCode = video_plugin_info.verCode
        video_plugin_index.engineVerCode = video_plugin_info.engineVerCode
