from my_package.module_a import greet_module_a
from my_package.subpackage.module_b import greet_module_b, perform_calculations

def write_to_file(filename, content, append=False):
    mode = "a" if append else "w"
    with open(filename, mode) as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    output_a = greet_module_a()
    output_b = greet_module_b()
    sum_numbers, average = perform_calculations()

    write_to_file("output.txt", output_a + "\n" + output_b + "\n")
    write_to_file("output.txt", f"Sum of numbers: {sum_numbers}\nAverage: {average}", append=True)

    contents = read_from_file("output.txt")
    print(contents)
