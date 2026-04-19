class UMLClass:
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.methods = []
        self.relations = []

class Attribute:
    def __init__(self, name, type_, visibility):
        self.name = name
        self.type = type_
        self.visibility = visibility

class Method:
    def __init__(self, name, return_type, visibility):
        self.name = name
        self.return_type = return_type
        self.visibility = visibility