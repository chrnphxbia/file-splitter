import sys


def split_file(name_of_file: str, num_of_lines: int):
    new_file = None
    count = 0

    with open(name_of_file) as file:
        for index, line in enumerate(file):
            if index % num_of_lines == 0:
                if new_file:
                    new_file.close()
                    
                new_file_name = f"{name_of_file.split('.')[0]}{count}.{name_of_file.split('.')[1]}"
                new_file = open(new_file_name, "w")
                count += 1
                
                print(f"File {new_file_name} created.")
                
            new_file.write(line)
            
        if new_file:
            new_file.close()


def main():
    if len(sys.argv) != 3:
        print(f"Invalid number of arguments.\nRun script as it follows:\n")
        print(f"{sys.argv[0]} <original_file> <number of lines per file>")
        return

    file_name = sys.argv[1]
    lines_per_file = int(sys.argv[2])

    split_file(file_name, lines_per_file)

    print("\nProcess finished.")

main()
