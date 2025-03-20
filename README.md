# Address Book Assistant Bot

This is a simple assistant bot for managing contacts in your address book. The bot allows you to add, modify, and view contact information, including phone numbers and birthdays.

## Available Commands

### 1. **hello**

Prints a greeting message and asks how it can assist you.  
Example:  
`hello`

### 2. **add**

Adds a new contact to your address book. You need to provide the contact's name and optionally a phone number.  
Example:  
`add John 1234567890`

### 3. **change**

Changes the phone number of an existing contact. You need to provide the name, the old phone number, and the new phone number.  
Example:  
`change John 1234567890 0987654321`

### 4. **phone**

Shows the phone numbers associated with a contact. You need to provide the contact's name.  
Example:  
`phone John`

### 5. **all**

Displays all the contacts in your address book.  
Example:  
`all`

### 6. **add-birthday**

Adds a birthday for an existing contact. You need to provide the name and the birthday in the format DD.MM.YYYY.  
Example:  
`add-birthday John 01.01.1990`

### 7. **show-birthday**

Displays the birthday of a contact. You need to provide the contact's name.  
Example:  
`show-birthday John`

### 8. **birthdays**

Shows a list of upcoming birthdays within the next week, along with the congratulation date.  
Example:  
`birthdays`

### 9. **close / exit**

Exits the assistant bot and saves all changes to the address book file.  
Example:  
`close` or `exit`

## How to Use

1. Run the script.
2. Enter the desired command when prompted.
3. The program will process the command and return an appropriate response.
4. To exit, type `close` or `exit`, and your data will be saved.

## Data Persistence

The address book data is stored in a file named `my_address_book.pkl`. Changes made during the session are saved to this file when the program exits.
