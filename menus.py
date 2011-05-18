# -*- coding: utf-8 -*-
class Menu(object):
    def __init__(self, ID=-1, Label="Unnamed", Href="#"):
        self.ID = ID
        self.Label = Label
        self.Href = Href
        self.data = []

manager_menu = []
current_menu = ""

index_redirect = None
