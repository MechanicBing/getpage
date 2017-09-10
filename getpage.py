#！coding=utf-8

import urllib
import re
import string


count = 0

class Page:
    '''lkdfjglk'''
    def __init__(self):

        self.homeUrl = ''
        self.pageList = []
        self.pageNum = 0
        self.pageListIter = 0
        self.fileNameList = []
        self.reg = re.compile(r'href="(.*?html)"')

        print 'init'

    #设置主页
    def setHomeUrl(self, url=''):
        try :
            urllib.urlopen(url)
        except IOError:
            print('io error\n','open url failed!!!')

        else:
            self.homeUrl = url

    #读取主页
    def getHomeUrl(self):
        return self.homeUrl
    #拼接url
    def makUrl(self, subU):
        return self.homeUrl+subU
    #



# 根据url和正则表达式获取页面中的子网页
    def findSubPage(self, ls):
        global count
        la=[]

       # print 'findsubpage'

        if len(ls) :
            ls = self.editHtmlList(ls)
           # print 'ls come in find:',count
            #print ls
            self.pageNum = len(self.pageList)

            while self.pageListIter <= self.pageNum:
                self.pageListIter = self.pageListIter + 1

                print 'itera:',self.pageListIter
                print 'pagenum:',self.pageNum
                print 'self.pageList[self.pageListIter]',self.pageList[self.pageListIter]

                try:
                    page = urllib.urlopen(self.pageList[self.pageListIter])

                except IOError:
                    print 'open url error in find '
                    return []
                else:
                    html = page.read()
                    la = re.findall(self.reg, html)

                    count = count + 1
                    #print 'count:', count
                    print 'go to url:',self.pageList[self.pageListIter]
                    #print 'it has sub url:'
                    #print la
                    if len(la):
#                        la = self.editHtmlList(la)
                        la = la + self.findSubPage(la)

                        #la = self.editHtmlList(la)
                       # print 'la+la', len(la)


#                       con
                    else:
                        #print 'mark'

                        return la
        else:
            ls=ls+la
            #print 'out find ',len(ls)
            return ls





    def editHtmlList(self, ls):
        #print 'edithtml'

        for i in range(len(ls)):
            if not ls[i].startswith('http'):

                ls[i]=self.makUrl(ls[i])
                #print ls[i],i

        i = 0
        while i<len(ls):
            if not ls[i].startswith(self.homeUrl):
                print 'delete:', ls[i]
                ls.remove(ls[i])
                continue
            else:
                i = i + 1




        if not len(self.pageList):
            #print 'set pagelist'
            ls = list(set(ls))
            ls.sort()
            self.pageList = ls
            #print 'self.pagelist:',len(self.pageList)
            #print self.pageList

        for itm in ls:
            if itm in self.pageList:
                #print 'itm in pagelist',itm
                continue


            else:
                self.pageList.append(itm)
                print 'append list:',itm
                self.pageNum = len(self.pageList)
                f = open('urls.txt','a+')
                f.writelines(itm+'\r\n')
                f.close()

        #print 'ls in edit:'
        #print ls
        #print 'edit out! length:',len(ls)
        return ls



    def setPageList(self):
        #print 'setpagelist'

 #       if len(self.pageList):
  ##         self.pageList=self.editHtmlList(self.pageList)
    #    else:
        try:
            page = urllib.urlopen(self.homeUrl)
        except IOError:
            print 'open url failed'
        else:
            html = page.read()


            #print self.pageList

            self.pageList = self.findSubPage( re.findall(self.reg, html))





########################################################################


mypage = Page()
mypage.setHomeUrl('https://docs.python.org/2/')
mypage.setPageList()
print mypage.getHomeUrl()
print mypage.pageList
print len(mypage.pageList)







##########################################################################


