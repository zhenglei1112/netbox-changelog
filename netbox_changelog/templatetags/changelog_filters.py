from django import template
import datetime

register = template.Library()

@register.filter
def humanize_date(value):
    if not isinstance(value, (datetime.date, datetime.datetime)):
        return value

    if isinstance(value, datetime.datetime):
        value = value.date()

    today = datetime.date.today()
    delta = today - value
    days = delta.days

    if days < 0:
        # 未来的日期直接返回格式化后的实际日期
        return value.strftime('%Y-%m-%d')
    elif days == 0:
        return '今天'
    elif days == 1:
        return '昨天'
    elif days == 2:
        return '前天'
    elif days < 7:
        return f'{days}天前'
    elif days < 14:
        return '上一周'
    elif days < 21:
        return '2周前'
    elif days < 28:
        return '3周前'
    else:
        # 28天及以上直接显示实际日期
        return value.strftime('%Y-%m-%d')
