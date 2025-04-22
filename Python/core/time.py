#
# Author: Rohtash Lakra
#
from datetime import datetime, timezone

import pytz


class TimeUtils:
    UTC_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z"
    TIMEZONE_FORMAT = "%Y-%m-%d %H:%M:%S %Z (%z)"
    PST_TIMEZONE = "US/Pacific"
    PST_LOS_ANGLES_TIMEZONE = "America/Los_Angeles"

    def convert_timezone(self, utc_time: datetime, timezone_str: str):
        """Converts a UTC datetime to PST datetime."""
        # Convert to PST timezone
        time_zone = pytz.timezone(timezone_str)
        pst_time = utc_time.astimezone(time_zone)
        # pst_tz = timezone(timedelta(hours=-8))
        # pst_time = utc_time.astimezone(pst_tz)

        # Format the PST time as a string
        return pst_time.strftime("%Y-%m-%d %H:%M:%S")

    def utc_to_pst(self, utc_time_str, utc_format="%Y-%m-%d %H:%M:%S"):
        """Converts a UTC datetime to PST datetime."""
        return self.convert_timezone(self.as_utc_datetime(utc_time_str), TimeUtils.PST_LOS_ANGLES_TIMEZONE)
        # return self.convert_timezone(utc_time, self.PST_TIMEZONE)

    def now_utc(self):
        """Returns the current datetime in UTC timezone"""
        return datetime.now(pytz.utc)

    def iso_datetime(self, date_time_str: str):
        return datetime.fromisoformat(date_time_str)

    def as_utc_datetime(self, utc_time_str: str) -> datetime:
        """Converts a UTC datetime to PST datetime."""
        # Parse the UTC time string into a datetime object
        utc_datetime = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        # utc_timezone = timezone(pytz.utc)
        # utc_datetime = datetime.fromisoformat(date_time_str).astimezone(utc_timezone)
        return utc_datetime

    def to_str(self, date: datetime, date_format: str) -> str:
        return date.strftime(date_format)


def convert_utc_to_pst(utc_time_str, utc_format="%Y-%m-%d %H:%M:%S"):
    # Parse the UTC time string into a datetime object
    utc_time = datetime.strptime(utc_time_str, utc_format).replace(tzinfo=timezone.utc)

    # Convert to PST timezone
    pst_timezone = pytz.timezone("America/Los_Angeles")
    pst_time = utc_time.astimezone(pst_timezone)

    # Format the PST time as a string
    pst_time_str = pst_time.strftime(utc_format)

    return pst_time_str


if __name__ == '__main__':
    print()
    time_utils = TimeUtils()
    # Print the result
    # utc_now = time_utils.now_utc()
    # pst_now = time_utils.utc_to_pst(utc_now)
    # print("UTC time:", utc_now)
    # print("PST time:", pst_now)
    # print()

    # 2024-10-02 20:28:32
    print('iso_date:', time_utils.iso_datetime('2024-10-02 20:28:32'))
    print('utc_datetime:', time_utils.as_utc_datetime('2024-10-02 12:21:00'))
    print()

    date_format = '%Y-%m-%d %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    # print('Current date & time is:', date.strftime(date_format))
    print('Current date & time is:', time_utils.to_str(date, date_format))
    # date = date.astimezone(timezone('US/Pacific'))
    # print('Local date & time is:', date.strftime(date_format))
    # print('Local date & time is:', time_utils.to_str(date, date_format))
    print()

    print()
    utc_times = ['2024-12-20 18:55:17', '2024-12-20 19:56:09']
    for utc_time in utc_times:
        print(f"utc_time={utc_time}, utc_to_pst={convert_utc_to_pst(utc_time)}")
        # print(f"utc_time={utc_time}, utc_to_pst={utc_to_pst(utc_time)}")
        print()
