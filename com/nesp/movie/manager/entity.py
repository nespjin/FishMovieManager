#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Team: NESP Technology
Author: <a href="mailto:1756404649@qq.com">靳兆鲁 Email:1756404649@qq.com</a>
Time: Created 2020/4/25 23:48
Project: FishMovieManagerTools
Description:
"""
from enum import IntEnum


class PluginVipCode(IntEnum):
    VIP = 1
    FREE = 0


class VideoPluginIndex:
    def __init__(self):
        self.author = ""
        self.introShort = ""
        self.updateTime = ""
        self.supports = []
        self.name = ""
        self.tags = []
        self.vipCode = PluginVipCode.FREE
        self.verCode = -1
        self.verName = ""
        self.engineVerCode = -1


class VideoPluginInfo:
    def __init__(self):
        """Video plugin index"""
        self.author = ""
        self.introShort = ""
        self.updateTime = ""
        self.supports = []
        self.name = ""
        self.tags = []
        self.vipCode = PluginVipCode.FREE
        self.verCode = -1
        self.verName = ""
        self.engineVerCode = -1
        """video plugin info"""
        self.hostUrl = ""
        self.intro = ""
        self.mainPageUrl = ""
        self.mainPageScript = ""
        self.moviePageUrl = ""
        self.soapPageUrl = ""
        self.varietyPageUrl = ""
        self.animPageUrl = ""
        self.searchPageUrl = ""
        self.searchPageScript = ""
        self.videosPageScript = ""
        self.playPageScript = ""
        self.playUrlParserScript = ""
        self.mainVideoPageDsl = None
        self.videosPageDsl = None
        self.playPageDsl = None
        self.searchPageDsl = None


class VideoPlugin:

    def __init__(self):
        """Video plugin index"""
        self.author = ""
        self.introShort = ""
        self.updateTime = ""
        self.supports = []
        self.name = ""
        self.tags = []
        self.vipCode = PluginVipCode.FREE
        self.verCode = -1
        self.verName = ""
        self.engineVerCode = -1
        """video plugin info"""
        self.hostUrl = ""
        self.intro = ""
        self.mainPageUrl = ""
        self.mainPageScript = ""
        self.moviePageUrl = ""
        self.soapPageUrl = ""
        self.varietyPageUrl = ""
        self.animPageUrl = ""
        self.searchPageUrl = ""
        self.searchPageScript = ""
        self.videosPageScript = ""
        self.playPageScript = ""
        self.playUrlParserScript = ""
        self.mainVideoPageDsl = None
        self.videosPageDsl = None
        self.playPageDsl = None
        self.searchPageDsl = None
        self.state = 0
        self.priority = 0
        self.isCurrentUI = False


class VideoPluginPackage:
    def __init__(self):
        self.name = "未知"
        self.author = "未知"
        self.videoPlugins = []


class MainVideoPageDsl:
    """DSL for main page"""

    def __init__(self):
        self.slideList = ""
        self.slideTitle = ""
        self.slideImgUrl = ""
        self.slideInfoUrl = ""

        self.newPlayList = ""
        self.newPlayImgUrl = ""
        self.newPlayTitle = ""
        self.newPlayName = ""
        self.newPlayScore = ""
        self.newPlayInfoUrl = ""

        self.newMovieList = ""
        self.newMovieImgUrl = ""
        self.newMovieTitle = ""
        self.newMovieName = ""
        self.newMovieScore = ""
        self.newMovieInfoUrl = ""

        self.newSoapList = ""
        self.newSoapImgUrl = ""
        self.newSoapTitle = ""
        self.newSoapName = ""
        self.newSoapScore = ""
        self.newSoapInfoUrl = ""

        self.newVarietyList = ""
        self.newVarietyImgUrl = ""
        self.newVarietyTitle = ""
        self.newVarietyName = ""
        self.newVarietyScore = ""
        self.newVarietyInfoUrl = ""

        self.newAnimList = ""
        self.newAnimImgUrl = ""
        self.newAnimTitle = ""
        self.newAnimName = ""
        self.newAnimScore = ""
        self.newAnimInfoUrl = ""

        self.newCommonImgUrl = ""
        self.newCommonTitle = ""
        self.newCommonName = ""
        self.newCommonScore = ""
        self.newCommonInfoUrl = ""


class PlayPageDsl:
    """DSL for play page"""

    def __init__(self):
        self.episodeGroupList = ""
        self.episodeList = ""
        self.episodeName = ""
        self.episodeUrl = ""
        self.episodeListReversed = False

        self.name = ""
        self.status = ""
        self.stars = ""
        self.director = ""
        self.area = ""
        self.introduction = ""
        self.updateTime = ""


class SearchPageDsl:
    """"DSL for searchPage"""

    def __init__(self):
        self.videoList = ""
        self.videoImgUrl = ""
        self.videoClass = ""
        self.videoStarts = ""
        self.videoDirector = ""
        self.videoUpdateTime = ""
        self.videoType = ""
        self.videoName = ""
        self.videoScore = ""
        self.videoInfoUrl = ""

        self.nextPageUrl = ""


class VideosPageDsl:
    """DSL for videos page"""

    def __init__(self):
        self.classGroupList = ""
        self.classList = ""
        self.className = ""
        self.classUrl = ""

        self.videoList = ""
        self.videoImgUrl = ""
        self.videoTitle = ""
        self.videoName = ""
        self.videoScore = ""
        self.videoInfoUrl = ""

        self.nextPageUrl = ""
