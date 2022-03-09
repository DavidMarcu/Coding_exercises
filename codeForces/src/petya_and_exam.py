from typing import Union


# https://codeforces.com/contest/832/problem/B
def get_input_from_stdin() -> tuple:
    return get_input(0)

def get_input(filename: Union[str,int]) -> tuple:
    file1 = open(filename)
    valid_letters = file1.readline()
    pattern = file1.readline()
    no_of_queries = int(file1.readline())
    queries = []
    for line in file1.readlines():
        queries.append(line)
    file1.close()
    return (valid_letters, pattern, no_of_queries, queries)

def get_or_default(value: str, value_index: int, default_value: str = '$'):
    try:
        return value[value_index]
    except IndexError:
        return default_value


def is_valid_letter(valid_letters: str, query_letter: str) -> bool:
    if query_letter is '$':
        return False
    if valid_letters.find(query_letter) >= 0:
        return True
    return False


# Testcase 55 fails(on their judgement tests), still need to think where this might fail
def is_valid_query(valid_letters: str, pattern: str, query: str) -> bool:
    query_index = 0
    query_pattern_diff = len(query) - len(pattern)
    for i in range(len(pattern)):
        pattern_letter = pattern[i]
        query_letter = get_or_default(query, query_index)
        if pattern_letter == '?':
           if not is_valid_letter(valid_letters, query_letter):
               return False
        elif pattern_letter == '*':
            if query_pattern_diff < 0:
                query_index = query_index - 1
            else:
                for query_index in range(query_index, query_index + query_pattern_diff + 1):
                    if is_valid_letter(valid_letters, query_letter):
                        return False
                    query_letter = get_or_default(query, query_index)
        elif pattern_letter != query_letter:
            return False
        query_index = query_index + 1
    return True


def solve_queries(valid_letters: str, pattern: str, no_of_queries: int, queries: 'list[str]', output: Union[str, int] = 1) -> None:
    with open(output, 'w') as output_file:
        for query in queries:
            if is_valid_query(valid_letters, pattern, query):
                output_file.write("YES\n")
            else:
                output_file.write("NO\n")


# ? -> one character from good_letters
# * -> string of characters that are not from good_letters set
if __name__ == '__main__':
    problem_input = get_input_from_stdin()
    solve_queries(valid_letters=problem_input[0], pattern=problem_input[1],
    no_of_queries=problem_input[2], queries=problem_input[3])
