# -*- encoding:utf-8 -*-
#__author__ = 'Zhong.zy'

from __future__ import absolute_import
import json
import sys
sys.path.append("../utils")
from avos_manager import *

class PoiGenerator(object):
        def __init__(self):
                self.avos = AvosManager()


        def addPoi(self,name,username,lat,lng):
                user = dict(__type='Pointer',className='_User',
                        objectId=self.avos.getUserIdByName(username))
                dataDict = dict(name=name,owner=user,lattitude=lat,longitude=lng)
                self.avos.saveData('poiGroup',dataDict)

        def deletePoi(self,lat,lng):
                objId = self.avos.getIdByCondition('poiGroup',lattitude=lat,longitude=lng)
                self.avos.deleteData('poiGroup',objId)

if __name__ == '__main__':
        poi = PoiGenerator()

        poi.addPoi('约炮','zhong2',2.0,113.1)
        #poi.deletePoi(1.1,2.1)
