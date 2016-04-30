"""
To use pytz effectively, you should always convert local times to UTC first.
Perform any datetime operations you need on the UTC values (such as
offsetting). Then, convert to local times as a final step.
"""
from datetime import datetime
import pytz

__author__ = 'Daniel'


class TimeParser():
    dt_formats = [
        '%Y-%m-%d %H:%M:%S %Z',  # 2014-05-01 15:45:16 PDT
        '%Y-%m-%d %H:%M:%S',     # 2014-05-01 15:45:16
    ]

    def parse(self, dt_str, dt_format):
        return datetime.strptime(dt_str, dt_format)


def localtime(utc_dt, tz_str):
    """
    Convert utc datetime to local timezone datetime
    :param utc_dt: datetime, utc
    :param tz_str: str, pytz e.g. 'US/Eastern'
    :return: datetime, in timezone of tz
    """
    tz = pytz.timezone(tz_str)
    local_dt = tz.normalize(utc_dt.astimezone(tz))
    return local_dt


def utctime(dt, tz_str):
    """
    Convert a naive datetime to utc datetime
    :param dt: datetime, naive datetime
    :param tz_str: str, pytz e.g. 'US/Pacific'
    :return: datetime, utc
    """
    tz = pytz.timezone(tz_str)
    local_dt = tz.localize(dt)
    utc_dt = pytz.utc.normalize(local_dt.astimezone(pytz.utc))
    return utc_dt
