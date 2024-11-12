import random

# Dictionary containing data types as keys and lists of examples as values
data_types_examples = {
    "Integer": [5, -10, 1000, 42, 0],
    "Float": [3.14, -2.71, 0.0, 1.618, 9.81],
    "String": ["Hello", "Python", "OpenAI", "Data type", "Example"],
    "Boolean": [True, False],
    "List": [[1, 2, 3], ["apple", "banana"], [True, False, True], []],
    "Tuple": [(1, 2), ("a", "b"), (True, False), (10, 20, 30)],
    "Set": [{1, 2, 3}, {"apple", "banana"}, {True, False}],
    "Dictionary": [
        {"name": "Alice", "age": 25},
        {"city": "Dhaka", "country": "Bangladesh"},
        {"fruit": "apple", "price": 1.2}
    ]
}

# Function to display data type examples
def display_data_type_example(data_type):
    if data_type in data_types_examples:
        example = random.choice(data_types_examples[data_type])
        print(f"\nData Type: {data_type}")
        print(f"Random Example: {example}")
    else:
        print("Invalid data type selected!")

# Function to check the data type of user input
def check_data_type(user_input):
    try:
        # Attempt to evaluate the input to convert it to a proper Python data type
        evaluated_input = eval(user_input)
        print(f"\nThe data type of your input is: {type(evaluated_input).__name__}")
    except:
        print("\nThe input is recognized as a String.")
        print("The data type of your input is: str")

# Main program
def main():
    print("Choose an option:")
    print("1. Display examples of a data type")
    print("2. Check the data type of provided input")

    try:
        choice = int(input("\nEnter your choice (1 or 2): "))

        if choice == 1:
            print("\nChoose a data type from the options below:")
            for i, key in enumerate(data_types_examples.keys(), start=1):
                print(f"{i}. {key}")

            data_type_choice = int(input("\nEnter the number corresponding to your choice: "))
            data_type_list = list(data_types_examples.keys())

            if 1 <= data_type_choice <= len(data_type_list):
                selected_data_type = data_type_list[data_type_choice - 1]
                display_data_type_example(selected_data_type)
            else:
                print("Invalid choice. Please try again.")

        elif choice == 2:
            user_input = input("\nEnter data to check its type: ")
            check_data_type(user_input)

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
