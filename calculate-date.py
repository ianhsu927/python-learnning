from datetime import datetime, timedelta
# 从 args 中获取日期和多少天前

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--date', help='the date to calculate from')
parser.add_argument('--days', help='the number of days before the date')
args = parser.parse_args()

# args.date 是时间戳
date = datetime.fromtimestamp(int(args.date))

# Calculate the date 2040 days ago
if type(days:=args.days) == str:
    days = int(days)
past_date = date - timedelta(days=days)
# Print the past and current dates
print(past_date.strftime('%Y-%m-%d'))