#coding:utf-8
import re

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_demo="""
<dd class="lemmaWgt-lemmaTitle-title">
<h1>自由软件</h1>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
</dd>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print "获取所有的链接"
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

print "获取lacie链接"
link_node=soup.find('a',href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print " 正则匹配 获取tillie链接"
link_a=soup.find('a',href=re.compile(r"ill"))
print link_a.name,link_a['href'],link_a.get_text()

link_p = soup.find("p",class_="title")
print link_p.name,link_p.get_text()

soup_demo=BeautifulSoup(html_demo,"html.parser",from_encoding="utf-8")
link_demo=soup_demo.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
print link_demo.get_text()
