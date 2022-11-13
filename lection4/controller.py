
import view
import model_mult as md

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    md.init(value_a,value_b)
    result = md.mult()
    view.view_data(result)