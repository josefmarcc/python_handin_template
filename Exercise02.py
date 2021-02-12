import argparse


def print_file_content(file):
    file_object = open(file)
    contents = file_object.read()
    print(contents)


def write_list_to_file(output_file, lst):
    file_object = open(output_file, 'w')
    file_object.write('\n'.join(lst))


def write_list_to_file_v2(output_file, *text_to_add):
    file_object = open(output_file, 'w')
    file_object.write('\n'.join(text_to_add))


def read_csv(input_file):
    output_list = []
    file_object = open(input_file, 'r')
    for row in file_object:
        output_list.append(row)
    print(output_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that writes content to a new file')
    parser.add_argument('pathToCsv', help='The path to the csv file')
    parser.add_argument('-d', '--file file_name',
                        help='The name of the file to overwrite')

    args = parser.parse_args()
    print_file_content(args.pathToCsv)
    print('File:', args.pathToCsv)
