#-*- coding: utf-8 -*-
from app import route, response, redirect, config
import ssl
import requests
import os
import json
from logic.Team04 import projectBasicInfo as p

@route('/hello.py.html')
def projectInfo(cookies):
	info = p.getProjectInfo()
	#将info返回给页面
	return response(projectInfo=info)