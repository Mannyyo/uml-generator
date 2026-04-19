import os
import argparse
from src.parser import parse_file, detect_relations
from src.generator import generate_puml

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_project_name(path):
    name = os.path.basename(os.path.abspath(path))
    if name == "src":
        return os.path.basename(os.path.dirname(path))
    return name

def main(project_path):
    all_classes = []

    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                all_classes.extend(parse_file(path))

    detect_relations(all_classes)

    # nome do projeto = nome da pasta
    project_name = get_project_name(project_path)

    puml = generate_puml(all_classes, project_name)

    output_path = os.path.join(OUTPUT_DIR, f"{project_name}.puml")
    
    with open(output_path, "w") as f:
        f.write(puml)

    print(f"Diagrama gerado: {output_path}.puml")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de UML a partir de código Java")
    parser.add_argument("path", help="Caminho para o diretório do projeto Java")

    args = parser.parse_args()

    main(args.path)