def num_to_ch(num):
    """
    阿拉伯数字 -> 中文数 (适用于 [0, 10000) 之间的阿拉伯数字)
    """
    num = int(num)
    _MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', )
    _P0 = (u'', u'十', u'百', u'千', )
    _S4 = 10 ** 4
    if num < 0 or num >= _S4:
        return None
    if num < 10:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num // 10
        lst.append(num)
        c = len(lst)    # 位数
        result = u''
        for idx, val in enumerate(lst):
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
            if idx < c - 1 and lst[idx + 1] == 0:
                result += u'零'
        result = result[::-1]
        if result[:2] == u"一十":
            result = result[1:]
        if result[-1:] == u"零":
            result = result[:-1]
        return result


def punch(n: int):
    for i in range(1, n+1):
        print("梆"*i+num_to_ch(i)+"拳")


if __name__ == "__main__":
    punch(10)
