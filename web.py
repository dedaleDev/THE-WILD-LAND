#!/usr/bin/env python3
# coding:utf-8
import sys
import ssl 
import urllib
from urllib.parse import urlparse

import mechanize
from bs4 import BeautifulSoup


class WebCrawler:

    def __init__(self, url, proxy=None, user_agent="Mozilla/5.0 (X11; Linux i686; rv:68.0)\Gecko/20100101 Firefox/68.0"):
        ssl._create_default_https_context = ssl._create_unverified_context#fixe le probleme de certificat ssl manquant dans certains cas
        if url[-1]=="/":
            self.url = url.rstrip("/")
        else:
            self.url = url
        self.proxy = proxy
        self.user_agent = user_agent
        self.browser = mechanize.Browser()
        self.link_list = []
        self.stopped = False

    def print_link_list(self):
        # Affiche la liste de liens d'une page
        for link in self.link_list:
            print(link)

    def get_page_source(self, page=None):
        #Obtient le code source d'une page web
        if page is None:
            page = self.url
        self.browser.set_handle_robots(False)
        user_agent = {("User-agent", self.user_agent)}
        self.browser.addheaders = user_agent
        if self.proxy:
            self.browser.set_proxies(self.proxy)
        page = page.strip()
        try:
            res = self.browser.open(page)
        except Exception as e:
            print("[-] Error for page : " + page + " " + str(e))
            return None
        return res

    def get_page_links(self, page=None):
    #obtient la liste des liens à partir d'une page web.
        link_list = []  # la liste de liens internes à "page"
        if page is None:
            page = self.url
        source = self.get_page_source(page)
        if source is not None:
            soup = BeautifulSoup(source, "html.parser")
            uparse = urlparse(page)
            for link in soup.find_all("a"):
                if not link.get("href") is None:
                    href = link.get("href")
                    if "#" in href:
                        href = href.split("#")[0]
                    new_link = urllib.parse.urljoin(page, href)
                    if uparse.hostname in new_link and new_link not in link_list:
                        link_list.append(new_link)
            return link_list
        else:
            return []

    def print_cookies(self):
        #  Affiche les cookies de la session
        for cookie in self.browser.cookiejar:
            print(cookie)

    def get_cookies(self):
        #  Retourne les cookies de la session
        return self.browser.cookiejar

    def crawl(self, page=None):
      #craw toutes les pages web d'un site de façon récursive
        try:
            page_links = self.get_page_links(page)
            for link in page_links:
                if self.stopped:
                    break
                if link not in self.link_list:
                    self.link_list.append(link)
                    print("Link add to list : " + link)
                    self.crawl(link)
        except KeyboardInterrupt:
            print("\nSoftware stopped by user")
            sys.exit(1)
        except Exception as e:
            print("\Error : " + str(e))
            sys.exit(2)
