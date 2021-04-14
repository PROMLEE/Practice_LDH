def celtofah(n):
    result = 9/5*n + 32
    return result


def fahtocel(n):
    result = 5/9*(n-32)
    return result


num = float(input('온도는?'))
print('섭씨  %f도는 화씨 %f 도이다' % (num, celtofah(num)))
print('화씨  %f도는 섭씨 %f 도이다' % (num, fahtocel(num)))
