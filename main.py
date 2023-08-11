from my_package.module_a import greet_module_a
from my_package.subpackage.module_b import greet_module_b

def main():
    print(greet_module_a())
    print(greet_module_b())

if __name__ == "__main__":
    main()
