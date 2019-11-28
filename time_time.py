# -*- coding: utf -*-
import time


# 获取当前时间戳，自1970年1月1日至今的秒数
# 时间戳最适合日期运算
ticks = time.time()   # float
print('当前时间戳：', ticks) 
print('当年我距菜鸟教程编写', (1574263205.214211 - 1459996086.7115328) / (60 * 60 * 24 * 365), '年')
print('现在已经过去了', (ticks - 1574263205.214211) / (60 * 60 * 24 * 365), '年')
print('哎❤️')
print()


# 获取当前时间
# 利用时间戳向时间元组转换
# 时间元组(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday<周中第几天>, tm_yday<年中第几天>, tm_isdst<夏令时>)
# tm_isdst 
    # 1 是夏令时
    # 0 不是夏令时
    # -1 未知，默认-1
localtime = time.localtime(time.time())
print('本地时间为:', localtime)


# 获取格式化的时间
# 最简单的格式 asctime()
localtime = time.asctime( time.localtime(time.time()) )
print('当前格式化的时间:', localtime)


# 格式化日期
# 使用strftime()格式化日期

