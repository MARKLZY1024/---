def hashlist(slist):

    import hashlib
    def md5(content=None):
        if content is None:
            return ''
        md5gen = hashlib.md5()
        md5gen.update(content.encode())
        md5code = md5gen.hexdigest()
        md5gen = None
        return md5code
    listi = {}


    snum = len(slist)
    s = slist

    for i in s:
        df = i.split('.')
        st = md5(df[0])
        value = st
        result = int(value, 16)
        m = result%snum
        text = {}
        i = i.split('.')
        text[i[0]] = i[1]



        if str(m) not in listi:
            listi[str(m)] = [text]
        else:
            listi[str(m)].append(text)
    return listi
