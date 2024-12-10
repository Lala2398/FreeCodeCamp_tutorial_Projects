def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()

#Knowledge of the task : 

#List comprehension is a concise way to create lists in Python. 
#It allows you to generate a new list by applying an expression to each element of an iterable (like a list or a string) and optionally filtering elements with a condition.

#numbers = [1, 2, 3, 4, 5]
#squared = [x**2 for x in numbers if x % 2 == 0]  # Squares even numbers

#A case converter is a tool or function that converts text between different cases, such as converting from PascalCase or camelCase to snake_case, or vice versa. 
#It’s often used in programming for naming conventions.

#def convert_to_snake_case(pascal_case):
    #return ''.join(['_' + char.lower() if char.isupper() else char for char in pascal_case]).lstrip('_')
