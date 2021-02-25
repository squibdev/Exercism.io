def slices(series, length):
    out = []
    l = length
    if length > len(series) or length <= 0 or type(length) != int:
        raise ValueError('Input invalid!')
    else:
        for i in range(0,len(series)):
            if len(series[i:l]) == length:
                out.append(series[i:l])
                i += 1
                l += 1
    return out
    