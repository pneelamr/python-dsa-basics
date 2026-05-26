def create(rows, cols):
    return {'data': {}, 'rows': rows, 'cols': cols}


def set_val(matrix, row, col, value):
    if value == 0:
        matrix['data'].pop((row, col), None)
    else:
        matrix['data'][(row, col)] = value


def get_val(matrix, row, col):
    return matrix['data'].get((row, col), 0)


def delete(matrix, row, col):
    matrix['data'].pop((row, col), None)


def display(matrix):
    for r in range(matrix['rows']):
        row = [str(get_val(matrix, r, c)) for c in range(matrix['cols'])]
        print(' '.join(row))
