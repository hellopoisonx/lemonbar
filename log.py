#!/usr/bin/env python
import time
import action


class Log(object):
    def write(text=None, time=time.strftime("[%Y-%m-%d %H-%M-%S]", time.localtime())):
        if text:
            f = open(action.Lemonbar_root + "log.txt", "a")
            message = time + ":" + text + "\n"
            f.write(message)
            f.close()
