import requests
import datetime


class Utils(object):

    #декоратор
    def once(func):
        def wrapper(*args):
            with open(args[0], 'w') as ang:
                ang.write(str(func(*args)))
            result = func(*args)
            return result

        return wrapper

    #логировщик
    @once
    def _logger(filename, url, level):
        rss = requests.get(url)
        if (level == 1):
            return (url, rss.text)
        elif (level == 2):
            return (url, rss.status_code)
        elif (level == 3):
            currenttime = datetime.datetime.now().time()
            return (url, rss.status_code, currenttime, rss.text)

    #для проверки ожидания
    def testfunc(dd):
        return True

    #метод ожидания
    def mainfunc(testfun, timeout, period):
        tim = timeout
        shet = 0
        for i in range(0, timeout):
            if (testfun):
                return ('Success')
                exit(0)
            elif (tim <= 0):
                return ('timeout')
                exit(0)
            else:
                shet = shet + 5
                tim = tim - period
                if (testfun):
                    return (print('Функция ' + 'вызывалась в течении ' + str(shet) + ' секунд'))
                else:
                    time.sleep(5)
