class FormulaError(Exception):
    def __init__(self,message='FormulaError'):
        self.message = message
        super().__init__(self.message)

def calc(input_data:str):
    split_data = input_data.split()
    if len(split_data) < 3:
        raise FormulaError
    try:
        float_number_first, float_number_second = float(split_data[0]),float(split_data[2])
    except ValueError:
        raise FormulaError
    if not split_data[1] in '+-*/':
        raise FormulaError
    return eval(input_data)
