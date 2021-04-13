"""
实现功能：
1. 根据域名反查IP
2. 检查有无 CDN
3. 返回 whois 信息
4. 爆破子域名
"""

import socket
import whois
import sys
import os


def ip_check(url):
    ip = socket.gethostbyname("www.xueersi.com")
    print(ip)


def whois_info(url):
    info = whois.whois("www.baidu.com")
    print(info)


def exits_cdn(url):
    data = os.popen('nslookup ' + url)
    data = data.read()
    if "Addresses" in data:
        print("there is CDN in " + url)
    elif "timed out" in data:
        print(url + "timed out")
    else:
        print("there is no CDN in " + url)


def subdomain_scan(url):
    url = url.replace("www", '')
    for subdomain in open("subdomainDic.txt", 'r'):
        test_url = subdomain.rstrip() + url
        # print(test_url)
        try:
            ip = socket.gethostbyname(test_url)
            if ip:
                print(test_url)
            else:
                pass
        except Exception as e:
            pass


if __name__ == '__main__':
    if sys.argv[1] == "-help":
        print("-all：实现对输入域名的全部脚本操作\n-ip：返回目标域名的IP地址\n-cdn：检查有无CDN\n-whois：返回whois信息\n-sub：爆破子域名信息\n举例：python infoCollect.py -all www.baidu.com")

    elif sys.argv[1] == "-all":
        try:
            ip_check(sys.argv[2])
            exits_cdn(sys.argv[2])
            whois_info(sys.argv[2])
            subdomain_scan(sys.argv[2])
        except Exception as inputE:
            print("请检查输入是否有误！")
    elif sys.argv[1] == "-ip":
        try:
            ip_check(sys.argv[2])
        except Exception as inputE:
            print("请检查输入是否有误！")
    elif sys.argv[1] == "-cdn":
        try:
            exits_cdn(sys.argv[2])
        except Exception as inputE:
            print("请检查输入是否有误！")
    elif sys.argv[1] == "-whois":
        try:
            whois_info(sys.argv[2])
        except Exception as inputE:
            print("请检查输入是否有误！")
    elif sys.argv[1] == "-sub":
        try:
            subdomain_scan(sys.argv[2])
        except Exception as inputE:
            print("请检查输入是否有误！")
