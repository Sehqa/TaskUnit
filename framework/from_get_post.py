import requests


class Get_Post(object):
    @staticmethod
    def _gethttp(urls, paramss, headerss):
        req = requests.get(url=urls, params=paramss, headers=headerss)
        return req

        # метод для post

    @staticmethod
    def _posthttp(urls, paramss, headerss, bodys):
        req = requests.post(url=urls, params=paramss, headers=headerss, data=bodys)
        return req
