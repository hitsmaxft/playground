#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import ConfigParser
import itertools
import urllib2
import urllib

#url配置文件
config_file="pc.conf"

def give_me_urls(pattern, args):
    """输入url和参数, 按笛卡尔运算得到所有的参数url"""

    #提取url参数key,
    #arglist保存了所有的参数, 通过笛卡尔计算出所有的组合
    keys = args.keys()
    arglist = args.values()

    #工具函数, 用于拼接url
    def zip_url (params):
        url = pattern
        for i in xrange(len(keys)):
            url += '&{key}={value}'.format(key=keys[i], value=urllib2.quote(params[i]))
        return url

    #对每组参数进行笛卡尔运算, 拼接成url
    urls = [ zip_url( value_group ) for value_group in itertools.product(*arglist)]

    return urls

def do_request(sections):
    for name in sections.keys():
        make_curl(name, sections[name])
    pass

def make_curl(section, urls):
    f = open("{}.log".format(section), 'wb')
    for u in urls:
        print("request [{}], url: {}\n".format(section, u))
        uf = urllib.urlopen(u)
        f.write("code:{}\n{}\n".format(uf.getcode(), '='*10))
        f.write(uf.read())
    return 0

def parse_section(items):
    """将配置中的一个section转换为对应的url"""
    args = {}
    url =''
    for k,v in items:
        if 'url' == k:
            url = v.strip("'")
        else:
            args[k] = v.split(',')
    return give_me_urls(url, args)

def read_config(fn):
    """从配置中读去各个section并得计算所有的url内容"""
    urls = {}
    config = ConfigParser.ConfigParser()
    config.read(fn)

    for s in config.sections():
        urls[s] = parse_section(config.items(s))
    return urls

def main():
    urls = read_config(config_file)
    do_request(urls)

if __name__ == '__main__':
    main()
