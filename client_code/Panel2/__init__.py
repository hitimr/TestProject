from ._anvil_designer import Panel2Template
from anvil import *

class Panel2(Panel2Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
