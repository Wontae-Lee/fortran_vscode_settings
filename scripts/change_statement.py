import os
import re


def replace_string_in_files(directory, old_string, new_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # read file
            with open(file_path, 'r', encoding='utf-8',errors='ignore') as f:
                file_content = f.read()

            # replace string
            modified_content = re.sub(re.escape(old_string), new_string, file_content)

            # write file
            with open(file_path, 'w', encoding='utf-8',errors='ignore') as f:
                f.write(modified_content)


def find_all_substring_indices(input_string, target_substring):
    indices = [0]
    index = input_string.find(target_substring)
    while index != -1:
        indices.append(index)
        index = input_string.find(target_substring, index + 1)
    return indices


def return_extracted_word(new_string):
    indices = find_all_substring_indices(new_string, target_substring="*")
    indices_length = len(indices)

    extracted_word = []
    for idx in range(indices_length):

        if idx + 1 == indices_length:
            extracted_word.append(new_string[indices[idx]:].replace("*", ""))

            break
        extracted_word.append(new_string[indices[idx]:indices[idx + 1]].replace("*", ""))

    return extracted_word


def replace_content_after_pattern(directory, pattern, new_string):
    pattern_length = len(pattern)
    extracted_word = return_extracted_word(new_string)

    for root, dirs, files in os.walk(directory):
        for file in files:

            file_path = os.path.join(root, file)

            string_list = []
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = re.finditer(pattern, content)
                count = content.count(pattern)

                for match in matches:
                    # 찾은 모든 패턴 다음의 괄호 내용 출력
                    start_index = match.end()
                    end_index = content.find(')', start_index)
                    if end_index != -1:
                        word = f'{content[start_index:end_index].strip()})'
                        temp_string = ""
                        for idx, ex_word in enumerate(extracted_word):

                            if extracted_word[idx] == extracted_word[-1]:
                                temp_string += f"{ex_word}"
                                string_list.append(temp_string)

                                break

                            temp_string += f"{ex_word}{word}"

            index = 0
            exclude_content_list = []
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = re.finditer(pattern, content)

                match_count = 0
                for match in matches:
                    # 찾은 모든 패턴 다음의 괄호 내용 출력
                    start_index = match.end()
                    end_index = content.find(')', start_index)

                    if end_index != -1:

                        if match_count == count - 1:
                            exclude_content_list.append(content[index:start_index - pattern_length])
                            exclude_content_list.append(content[end_index + 1:])
                            break

                        exclude_content_list.append(content[index:start_index - pattern_length])
                        # print(content[index:start_index - pattern_length])
                        index = end_index + 1

                        match_count += 1
            modified_content = ""
            if len(string_list) != 0:
                # print(len(exclude_content_list))
                # print(len(string_list))

                for idx, string in enumerate(string_list):
                    modified_content += f"{exclude_content_list[idx]}{string}"

                modified_content += exclude_content_list[-1]

                with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                    f.write(modified_content)


if __name__ == "__main__":
    # settings
    src_directory = "../src/"

    # replace_string_in_files(src_directory, old_string="!==================================================================================================================================\n! Copyright (c) 2010 - 2018 Prof. Claus-Dieter Munz and Prof. Stefanos Fasoulas\n!\n! This file is part of PICLas (piclas.boltzplatz.eu/piclas/piclas). PICLas is free software: you can redistribute it and/or modify\n! it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3\n! of the License, or (at your option) any later version.\n!\n! PICLas is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty\n! of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License v3.0 for more details.\n!\n! You should have received a copy of the GNU General Public License along with PICLas. If not, see <http://www.gnu.org/licenses/>.\n!==================================================================================================================================", new_string="")
    # replace_string_in_files(src_directory, old_string="!===================================================================================================================================\n", new_string="")
    # replace_string_in_files(src_directory, old_string="!==================================================================================================================================\n", new_string="")
    # replace_string_in_files(src_directory, old_string="!-----------------------------------------------------------------------------------------------------------------------------------\n", new_string="")
    # replace_string_in_files(src_directory, old_string="!----------------------------------------------------------------------------------------------------------------------------------\n", new_string="")

    replace_string_in_files(src_directory, old_string="PPURE",new_string="PURE")