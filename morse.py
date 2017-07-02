class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, str_agrs):

        final_str = []
        for chars in str_agrs.split("-"):

            if chars == "dash":
                final_str.append("_")
            if chars == "dot":
                final_str.append(".")

        return cls(final_str)



class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)



l = Letter.from_string("dot-dash-dot")

print(str(l))