# Minor-Project
# Internet Banking Chatbot

This is a Python-based chatbot for internet banking services. It allows users to perform basic banking operations such as checking balance, viewing recent transactions, initiating fund transfers, and viewing a mini statement. The chatbot supports both English and Hindi languages.

## Key Features

- **Multi-language Support**: The chatbot supports both English and Hindi.
- **Check Account Balance**: Users can check their current account balance.
- **View Recent Transactions**: Users can view a list of their recent transactions.
- **Initiate Fund Transfer**: Users can transfer funds to another account.
- **Mini Statement**: Users can get a mini statement of their recent transactions.
- **User-friendly Interface**: Simple text-based interaction.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**

   git clone https://github.com/Harshk7771/Minor-Project
   cd internet-banking-chatbot

    Run the application:

    python chatbot.py

**Usage**

    Start the Chatbot: Run the Python script to start the chatbot.
    Select Language: Choose your preferred language (English or Hindi).
    Interact with the Chatbot: Use the menu options to perform banking operations:
        Check Balance
        View Recent Transactions
        Initiate Fund Transfer
        View Mini Statement
    Exit the Chatbot: Type exit to end the chat.

**Code Overview**
chatbot.py

This is the main file of the chatbot. It includes the following key sections:

    Importing necessary libraries and defining the translations dictionary for language support.
    Defining the InternetBankingChatbot class with various methods to handle different banking operations.
    Defining methods for:
        Displaying a banner.
        Greeting the user.
        Selecting language.
        Displaying the menu.
        Checking account balance.
        Viewing recent transactions.
        Initiating fund transfers.
        Viewing mini statements.
        Exiting the chat.
        Processing user inputs.
        Starting the chat.

**Key Methods**

    __init__(): Initializes the chatbot with default values.
    display_banner(): Displays the banner of the chatbot.
    greet_user(): Greets the user.
    select_language(): Allows the user to select their preferred language.
    display_menu(): Displays the main menu.
    check_balance(): Returns the account balance.
    transfer_amount(): Initiates a fund transfer.
    recent_transactions(): Returns a list of recent transactions.
    mini_statement(): Returns a mini statement of recent transactions.
    exit_chat(): Prompts the user to confirm exiting the chat.
    end_chat(): Ends the chat.
    process_user_input(): Processes the user's input.
    start_chat(): Starts the chat and manages the main chat loop.

**Contributing**

If you would like to contribute to this project, please fork the repository and submit a pull request.
License

This project is open source and available under the MIT License.
Contact

For any questions or suggestions, please contact the author.

Enjoy your banking experience with our chatbot!
