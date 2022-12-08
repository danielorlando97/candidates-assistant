def cookie_split(cookie):
    cookie = cookie.split('; ')
    result = {}
    for c in cookie:
        ccs = c.split('=')
        result[ccs[0]] = '='.join(ccs[1:])

    return result