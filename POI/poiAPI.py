# -*- encoding=utf-8 -*-

from util_opt import get_source
import json

class PoiInfo(object):
    def __init__(self):
        self.baiduAPI = 'http://api.map.baidu.com/%s/?ak=fPnXQ2dVgLevy7GwIomnhEMg&output=json&%s'

    def toBaiduGPS(self,lng,lat):
        try:
            opts = 'coords=%s,%s&from=1&to=5' % (lng,lat)
            restAPI = self.baiduAPI % ('geoconv/v1',opts)
            res = get_source(restAPI)
            x_y = json.loads(res)['result'][0]
            lng_b,lat_b = x_y['x'],x_y['y']
        except:
            print 'Convert to Baidu GPS Error'
            return None
        return lng_b,lat_b

    def baidu2GPS(self,lng_b,lat_b):
        '''
        with a tolerance of less than 5m  
        '''
        try:
            lng_b2,lat_b2 = self.toBaiduGPS(lng_b,lat_b)
            lng = 2*lng_b - lng_b2
            lat = 2*lat_b - lat_b2
        except:
            print 'Convert to GPS Error'
            return lng_b,lat_b      
        return lng,lat

    def getPOI(self,lng,lat):
        try:
            opts = 'coordtype=wgs84ll&location=%s,%s' % (lat,lng)
            restAPI = self.baiduAPI % ('geocoder/v2',opts)
            res = get_source(restAPI)
            poi = json.loads(res)['result']
        except:
            print 'Get POI Error'
            return None
        return poi['business']

if __name__=='__main__':
    poi=PoiInfo()
    x,y = 116.322987,39.983424
    print poi.getPOI(x,y)
        
    
