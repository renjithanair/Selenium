from controls.base.editable import Editable


class TextBox(Editable):

    def __init__(self, driver):
        Editable.driver = driver
