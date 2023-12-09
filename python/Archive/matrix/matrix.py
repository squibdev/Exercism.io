class Matrix:
    def __init__(self, matrix_string):
        rows = []
        columns = []
        for row in matrix_string.split("\n"):
            sub_r = []
            sub_c = []
            for item in row.split(' '):
                print(item)
                sub_r.append(int(item))



        
    def row(self, index):
        pass

    def column(self, index):
        pass

m = Matrix("1 2\n3 4")
print(m.row(0))