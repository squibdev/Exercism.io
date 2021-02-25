class Matrix(object):
    def __init__(self, matrix_string):

        self.matrix_string = matrix_string

        columns = []

        rows = matrix_string.split("\n")

        self.rows = rows

        for item in rows:
            columns += item[0]

        self.columns = columns

    def row(self, index):
        rows = []
        for i in range(len(self.rows)):
            string_output = self.rows[i].split()
            output = list(map(int, string_output))
            rows.append(output)

        self.rows_output = rows
        return rows[index-1]

    def column(self, index):
        """rows = self.rows_output"""
        rows = []
        for i in range(len(self.rows)):
            string_output = self.rows[i].split()
            output = list(map(int, string_output))
            rows.append(output)

        self.rows_output = rows
        columns = []

        for item in rows:
            columns.append(item[index-1])

        return columns