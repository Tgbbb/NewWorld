import time
import datetime


class tomorrow_timestamp():
    def todaytime(self):
        today_time = datetime.date.today()
        return today_time

    def tomorowtime(self):
        tomorrow = self.todaytime() + datetime.timedelta(days=1)
        time_stamp = str(int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))))
        return time_stamp


if __name__ == '__main__':
    test = tomorrow_timestamp()
    print(test.tomorowtime())
