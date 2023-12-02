# calculate_date.py
# 偶然在少数派看到自己的注册距今时间, 但是网上转日期的网站不好用, 于是写了这个脚本
from datetime import datetime, timedelta
import argparse
"""
    Get the date and days from the command line
    Usage:
        python calculate_date.py --date $(date +%s) --days 100
        $(date _%s) 是获取当前时间戳的命令
"""
parser = argparse.ArgumentParser()
parser.add_argument('--date', help='the date to calculate from')
parser.add_argument('--days', help='the number of days before the date')
args = parser.parse_args()

# args.date 是时间戳
date = datetime.fromtimestamp(int(args.date))
if type(days:=args.days) == str:
    days = int(days)
past_date = date - timedelta(days=days)

print(past_date.strftime('%Y-%m-%d'))
