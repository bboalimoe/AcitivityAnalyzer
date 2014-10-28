#!/usr/bin/env python
# encoding: utf-8
#__author__ = 'wumao'

from __future__ import absolute_import
from avos.avos import AVObject
import arrow
import json
import settings
import datetime
import requests
from util_opt import *

class AvosClass(AVObject):
    def __init__(self):
        super(AvosClass, self).__init__()

class AvosManager(object):
        def __init__(self):
                AvosClass.app_settings = [settings.avos_app_id, settings.avos_app_key]

        def saveData(self,className,dataDict):
                res = AvosClass._save_to_avos(className,dataDict)
                if 'createdAt' not in json.loads(res.content):
                        print res.content

        #By Zhong.zy, Get info by specified opt
        def getData(self,className,**kwargs):
                with_params = {}
                for kparam, vparam in kwargs.items():
                    with_params[kparam] = vparam
    
                res = requests.get(
                    AvosClass.base_classes+className,
                    headers=AvosClass.headers(),
                    params=with_params,
                    verify=False
                )
                if 'error' not in json.loads(res.content):
                    return res.content
                
        #By Zhong.zy, Save activity in a same interface
        def saveActivity(self,dataDict):
                self.saveData('activityClass',dataDict)

        #By Zhong.zy, Get id to update data
        def getIdByName(self,className,objName):
                cond = '{"name":"%s"}' % objName
                res = self.getData(className,keys='objectId',where=cond)
                if res:
                        results = json.loads(res)['results']
                        if results:
                                return results[0]['objectId']
                            
        #By Zhong.zy, update, or insert if not exist
        def updateDataByName(self,className,objName,dataDict):
                objectId =  self.getIdByName(className,objName)
                if objectId:
                        res = AvosClass._update_avos(className,str(objectId),dataDict)
                        if 'error' not in json.loads(res.content):
                                return res.content
                else:
                        self.saveData(className,dataDict)
            



if __name__ == "__main__":
        avosManager = AvosManager()
        start = "2013-05-05 20:30:45"
        date_utc = getUtcDate(start)
        start_utc = timeConvet2utc(start)
        

        
        start_iso = start_utc.replace(" ","T")+".000Z"
        date_iso = date_utc.replace(" ","T")+".000Z"
        date_time = dict(__type='Date',iso=date_iso)    
        start_time = dict(__type='Date',iso=start_iso)
        end_time = dict(__type='Date',iso=start_iso)
        dataDict = {"name":"《文成公主》大型实景剧","date":date_time,
        "start_time":start_time,"end_time":end_time,"ticket":"0","region":"北京市海淀区北京邮电大学","longitude":116.361834,"lattitude":39.970513,"category":""}
        className = "testDate"
        #avosManager.saveData(className,dataDict)
        #avosManager.saveActivity(dataDict)
        avosManager.updateDataByName('activityClass','《文成公主》大型实景剧',dataDict)
        '''
        AvosClass.app_settings = [settings.avos_app_id, settings.avos_app_key]
        res = AvosClass.save(dataDict)
        if 'createdAt' in json.loads(res.content):
                print '\nSucceeded in creating test object in AvosClass!\n'
        else:
                print res.content
        '''
