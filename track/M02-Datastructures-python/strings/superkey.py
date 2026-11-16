#   CREATE SUPPER KYE SUPER()
#SUPER()-- Always to parentclasss 


class parent:
    def __init__(self, pname):
        self.pname = pname

    def show(self):
        print("parent method")


class child(parent):
    def show(self):
        print("child method")
        super().show()

    def __init__(self, cname, pname):
        self.cname = cname
        super().__init__(pname)


c1 = child("shakti", "vel")

c1.show()

print(c1.cname)
print(c1.pname)
 


