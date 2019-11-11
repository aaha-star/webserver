#-*- coding: utf-8 -*-

import ssl
import requests
import os
import json

repos = ['cxsjclassroom/webserver',"octocat/Hello-World"]


def getProjectInfo():
    info = {}
    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s/forks' % repo  # 确定url
        repoInfo = readURL('Repositories/forkInfo/%s' % (repo), repo_url)  # 访问url得到数据
        repoInfo = repoInfo and json.loads(repoInfo)  # 将数据类型转换

        info[repo] = []
        for a in repoInfo:
            info[repo].append(a['full_name'])

    for repo in repos:
        repo_url = 'https://api.github.com/repos/%s/branches' % repo
        repoInfo = readURL('Repositories/branchInfo/%s' % (repo), repo_url)
        repoInfo = repoInfo and json.loads(repoInfo)

    return info


#读取url的信息，并建立缓存
def readURL(cache,url):
	#看看该url是否访问过
	cache = 'data/cache/%s' % cache
	if os.path.isfile(cache):
		with open(cache, 'r') as f:
			content = f.read()
		return content

	content = requests.get(url).content.decode()

	#吧文件内容保存下来，以免多次重复访问url，类似于缓存
	folder = cache.rpartition('/')[0]
	not os.path.isdir(folder) and os.makedirs(folder)
	with open(cache, 'w') as f:
		f.write(content)
	return content