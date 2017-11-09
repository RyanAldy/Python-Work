class Details:
    def __init__(self, F, L):
        self.first = F
        self.last = L

    @property
    def Name(self):
        return self.first + ' ' + self.last

    @Name.setter
    def Name(self, N):
        self.first = N[1:2]
        self.last = N[3:]


R = Details('Ryan', 'Alderson')
Fullname = R.Name
print(Fullname)

S = Details('The', 'Shafeeq')
S.Name = 'Shafeeq'
NewName = S.Name
print(NewName)
