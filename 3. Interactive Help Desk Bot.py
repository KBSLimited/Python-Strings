#Task 1: Command Parser

def process_command(text):
    # Predefined commands and their responses
    commands = {
        "help": "Sure, how can I help you?",
        "issue": "Please provide more details about the issue.",
        "contact support": "You can contact support at support@example.com.",
        # Add more predefined commands and their responses as needed
    }

    # Check if the input text contains any predefined command
    for command, response in commands.items():
        if command in text.lower():
            return response
    
    # If no command is found
    return "No predefined command found. Please try again."

# Prompt the user to enter text input
user_input = input("Enter your text: ")

# Process the user input to identify predefined commands
response = process_command(user_input)
print(response)

#Task 2: Issue Categorizer

def process_command(text):
    # Predefined commands and their responses
    commands = {
        "help": "Sure, how can I help you?",
        "issue": "Please provide more details about the issue.",
        "contact support": "You can contact support at support@example.com.",
        # Add more predefined commands and their responses as needed
    }

    # Keywords for issue categorization
    categories = {
        "login": ["login", "signin", "authentication"],
        "performance": ["performance", "speed", "slow"],
        "error": ["error", "bug", "issue"],
        # Add more categories and their corresponding keywords as needed
    }

    # Check if the input text contains any predefined command
    for command, response in commands.items():
        if command in text.lower():
            return response
    
    # Check if the input text contains any issue category keywords
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text.lower():
                return f"The issue is related to {category.capitalize()}."

    # If no command or issue category is found
    return "No predefined command found. Please try again."

# Prompt the user to enter text input
user_input = input("Enter your text: ")

# Process the user input to identify predefined commands and issue categories
response = process_command(user_input)
print(response)