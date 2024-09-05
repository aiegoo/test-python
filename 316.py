class FourCal:
    def setdata (sel, fir, sec):
        sel.first = fir
        sel.second = sec

    def add(sel):
        result = sel.first + sel.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.add())

#
# # Output:
# # 6
