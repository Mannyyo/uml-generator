import javalang
from src.model import UMLClass, Attribute, Method

def parse_file(file_path):
    with open(file_path) as f:
        tree = javalang.parse.parse(f.read())

    classes = []

    for _, node in tree.filter(javalang.tree.ClassDeclaration):
        uml_class = UMLClass(node.name)

        # atributos
        for field in node.fields:
            for declarator in field.declarators:
                uml_class.attributes.append(
                    Attribute(
                        declarator.name,
                        field.type.name,
                        "private" if "private" in field.modifiers else "public"
                    )
                )

        # métodos
        for method in node.methods:
            uml_class.methods.append(
                Method(
                    method.name,
                    method.return_type.name if method.return_type else "void",
                    "public" if "public" in method.modifiers else "private"
                )
            )

        classes.append(uml_class)

    return classes

def detect_relations(classes):
    class_names = {c.name for c in classes}

    for c in classes:
        for attr in c.attributes:
            if attr.type in class_names:
                c.relations.append(attr.type)