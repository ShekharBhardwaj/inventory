class ReversedStr(str):

    def __new__(*args, **kwargs):
        str_self = str.__new__(*args, **kwargs)
        str_self = str_self[::-1]
        return str_self






rstr = ReversedStr("hello")

print(rstr)

