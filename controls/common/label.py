from controls.base.editable import Editable


class Label(Editable):

    def __init__(self, driver):
        Editable.driver = driver
