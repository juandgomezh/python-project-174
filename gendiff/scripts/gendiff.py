import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compara dos archivos y genera un diff entre ellos"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="agrega el formato de salida", default="stylish")

    args = parser.parse_args()  
    genrated_diff = generate_diff(args.first_file, args.second_file)
    print(genrated_diff)

if __name__ == "__main__":
    main()