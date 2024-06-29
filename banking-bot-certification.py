import re
import random
from datetime import datetime

class InternetBankingChatbot:
    translations = {
        'english': {
            'menu': "Menu:",
            'check_balance': "1. Check Balance",
            'recent_transactions': "2. Recent Transactions",
            'initiate_transfer': "3. Initiate Fund Transfer",
            'mini_statement': "4. Mini Statement",
            'exit': "5. Exit",
            'balance_message': "Your account balance is",
            'enter_recipient_account': "Enter recipient's account number: ",
            'enter_cif_number': "Enter CIF number: ",
            'enter_ifsc_code': "Enter IFSC code: ",
            'enter_branch_name': "Enter branch name: ",
            'enter_transfer_amount': "Enter transfer amount: ",
            'transaction_details': "Transaction details",
            'transfer_confirmation': "Fund transfer successful!",
            'insufficient_funds': "Insufficient funds for the transfer.",
            'no_transactions': "No transactions available.",
            'exit_prompt': "Thank you for using XYZ Internet Banking! Can I help you with anything else? (yes/no): ",
            'exit_message': "Thank you for using XYZ Internet Banking. Have a great day!",
        },
        'hindi': {
            'menu': "मेन्यू:",
            'check_balance': "1. शेष जांचें",
            'recent_transactions': "2. हाल के लेन-देन",
            'initiate_transfer': "3. फंड ट्रांसफर की शुरुआत करें",
            'mini_statement': "4. मिनी स्टेटमेंट",
            'exit': "5. बाहर निकलें",
            'balance_message': "आपका खाता शेष है",
            'enter_recipient_account': "प्राप्तकर्ता का खाता नंबर दर्ज करें: ",
            'enter_cif_number': "CIF नंबर दर्ज करें: ",
            'enter_ifsc_code': "IFSC कोड दर्ज करें: ",
            'enter_branch_name': "शाखा का नाम दर्ज करें: ",
            'enter_transfer_amount': "ट्रांसफर राशि दर्ज करें: ",
            'transaction_details': "लेन-देन का विवरण",
            'transfer_confirmation': "फंड ट्रांसफर सफल!",
            'insufficient_funds': "स्थानांतरण के लिए अपर्याप्त धन है।",
            'no_transactions': "कोई लेन-देन उपलब्ध नहीं है।",
            'exit_prompt': "XYZ इंटरनेट बैंकिंग का उपयोग करने के लिए धन्यवाद! क्या मैं आपकी कोई और सहायता कर सकता हूँ? (हाँ/नहीं): ",
            'exit_message': "XYZ इंटरनेट बैंकिंग का उपयोग करने के लिए धन्यवाद! आपका दिन शुभ हो।",
        }
    }

    def __init__(self):
        self.account_balance = random.uniform(1000, 10000)
        self.recent_transactions_list = []
        self.recipient_account = None
        self.cif_number = None
        self.ifsc_code = None
        self.branch_name = None
        self.transfer_amount_value = None
        self.selected_language = 'english'

    def display_banner(self):
        print("===============================================")
        print("               XYZ Internet Banking")
        print("                       Developed by Harsh Kumar")
        print("===============================================")

    def greet_user(self):
        print(f"Chatbot: Hello! Welcome to XYZ Bank. I am your virtual assistant. How can I assist you today?")

    def select_language(self):
        print("Available Languages:")
        print("1. English")
        print("2. Hindi")

        language_input = input("Select your preferred language (by number or name): ").lower()

        language_mapping = {
            'english': ['1', 'english'],
            'hindi': ['2', 'hindi'],
        }

        for lang, options in language_mapping.items():
            if language_input in options:
                self.selected_language = lang
                print(f"Chatbot: Language set to {lang.capitalize()}.")
                return

        print("Chatbot: I'm sorry, I couldn't understand your language preference. Setting language to English.")
        self.selected_language = 'english'

    def display_menu(self):
        print(self.translations[self.selected_language]['menu'])
        print(self.translations[self.selected_language]['check_balance'])
        print(self.translations[self.selected_language]['recent_transactions'])
        print(self.translations[self.selected_language]['initiate_transfer'])
        print(self.translations[self.selected_language]['mini_statement'])
        print(self.translations[self.selected_language]['exit'])

    def check_balance(self):
        return f"Chatbot: {self.translations[self.selected_language]['balance_message']} Rs. {self.account_balance:.2f}"

    def transfer_amount(self):
        self.recipient_account = input(
            f"Chatbot: {self.translations[self.selected_language]['enter_recipient_account']}")
        self.cif_number = input(f"Chatbot: {self.translations[self.selected_language]['enter_cif_number']}")
        self.ifsc_code = input(f"Chatbot: {self.translations[self.selected_language]['enter_ifsc_code']}")
        self.branch_name = input(f"Chatbot: {self.translations[self.selected_language]['enter_branch_name']}")
        self.transfer_amount_value = float(
            input(f"Chatbot: {self.translations[self.selected_language]['enter_transfer_amount']}"))

        # In a real application, you would perform validation and initiate the fund transfer.
        if self.transfer_amount_value <= self.account_balance:
            self.account_balance -= self.transfer_amount_value
            transaction_detail = f"{self.translations[self.selected_language]['transaction_details']} - {self.transfer_amount_value:.2f} ({self.recipient_account}, {self.cif_number}, {self.ifsc_code}, {self.branch_name}, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
            self.recent_transactions_list.append(transaction_detail)
            self.transfer_confirmation = self.translations[self.selected_language]['transfer_confirmation']
        else:
            self.transfer_confirmation = self.translations[self.selected_language]['insufficient_funds']

    def recent_transactions(self):
        if not self.recent_transactions_list:
            return self.translations[self.selected_language]['no_transactions']
        else:
            transactions = []
            for transaction in self.recent_transactions_list:
                transactions.append(transaction)

            header = "S.No\tTransaction Details\tDebit Balance\tCredit Balance\tRemaining Balance"
            return header + '\n' + '\n'.join(transactions)

    def mini_statement(self):
        if not self.recent_transactions_list:
            return self.translations[self.selected_language]['no_transactions']
        else:
            transactions = []
            for i, transaction in enumerate(self.recent_transactions_list, start=1):
                debit_balance = self.account_balance + sum(
                    [float(re.search(r'[-]?\d+\.\d+', trans).group()) for trans in self.recent_transactions_list[:i]])
                debit_balance_str = f"{debit_balance:.2f}"
                credit_balance_str = f"{self.account_balance:.2f}"
                remaining_balance_str = f"{debit_balance - self.transfer_amount_value:.2f}"
                transactions.append(
                    f"{i}\t{transaction}\t{debit_balance_str}\t{credit_balance_str}\t{remaining_balance_str}")

            header = "S.No\tTransaction Details\tDebit Balance\tCredit Balance\tRemaining Balance"
            return header + '\n' + '\n'.join(transactions)

    def exit_chat(self):
        exit_prompt = input(f"Chatbot: {self.translations[self.selected_language]['exit_prompt']}").lower()
        if exit_prompt == 'no' or exit_prompt == 'नहीं':
            exit_message = self.translations[self.selected_language]['exit_message']
            print(f"Chatbot: {exit_message}")
            exit()
        elif exit_prompt == 'yes' or exit_prompt == 'हाँ':
            self.recent_transactions_list = []
            print("Chatbot: Redirecting to the main menu.")
        else:
            print("Chatbot: I'm sorry, I didn't understand. Please type 'yes' or 'no'.")

    def end_chat(self):
        exit_message = self.translations[self.selected_language]['exit_message']
        print(f"Chatbot: {exit_message}")
        exit()

    def process_user_input(self, user_input):
        if user_input == '1':
            balance_result = self.check_balance()
            print(f"Chatbot: {balance_result}")
        elif user_input == '2':
            transactions_result = self.recent_transactions()
            print(f"Chatbot: {transactions_result}")
        elif user_input == '3':
            self.transfer_amount()
            print(f"Chatbot: {self.transfer_confirmation}")
        elif user_input == '4':
            mini_statement_result = self.mini_statement()
            print(f"Chatbot: {mini_statement_result}")
        elif user_input == '5':
            self.exit_chat()
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Please select a valid option.")

    def start_chat(self):
        self.display_banner()
        self.greet_user()
        self.select_language()

        while True:
            self.display_menu()
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                self.end_chat()

            if user_input.lower() == 'menu':
                self.display_menu()
                continue

            self.process_user_input(user_input)


if __name__ == "__main__":
    chatbot = InternetBankingChatbot()
    chatbot.start_chat()
