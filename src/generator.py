def generate_puml(classes, diagram_name="Diagram"):
    lines = [f"@startuml {diagram_name}\n"]

    for c in classes:
        lines.append(f"class {c.name} {{")

        for attr in c.attributes:
            symbol = "-" if attr.visibility == "private" else "+"
            lines.append(f"  {symbol} {attr.name}: {attr.type}")

        for method in c.methods:
            symbol = "+" if method.visibility == "public" else "-"
            lines.append(f"  {symbol} {method.name}(): {method.return_type}")

        lines.append("}\n")

    # relações
    for c in classes:
        for rel in c.relations:
            lines.append(f"{c.name} --> {rel}")

    lines.append("\n@enduml")

    return "\n".join(lines)