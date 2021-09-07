
import requests



class Get_Post(object):
    def _gethttp(urls, paramss, headerss):
        r = requests.get(url=urls, params=paramss, headers=headerss)
        return r

        # метод для post

    def _posthttp(urls, paramss, headerss, bodys):
        r = requests.post(url=urls, params=paramss, headers=headerss, data=bodys)
        return r