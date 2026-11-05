<div align="center">

🔐 Password Generator
A Simple Python-Based Secure Password Generator

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="85" alt="Python Logo">

<br>






</div>

📌 Project Overview

The Password Generator is a console-based application developed using Python. It allows users to generate multiple random passwords by specifying their desired password length and the number of passwords required.

The application uses Python's built-in secrets module to select random characters from a predefined character pool containing uppercase letters, lowercase letters, digits, and special symbols.

Users can also choose whether to save the generated passwords locally in a text file.

✨ Features
Custom Password Length: Generate passwords according to the desired length.
Multiple Password Generation: Generate multiple passwords in a single execution.
Character Variety: Includes uppercase letters, lowercase letters, digits, and special symbols.
Secure Random Selection: Uses Python's secrets module.
Optional File Storage: Save generated passwords in a local text file.
Console-Based Interface: Simple and interactive terminal interface.
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
secrets	Secure random character selection
string	Provides predefined character sets
File Handling	Stores generated passwords in a text file
⚙️ How It Works
1. Character Pool

The application combines four character categories to create a pool of possible characters.

Let:

$L$ = Lowercase letters
$U$ = Uppercase letters
$D$ = Digits
$S$ = Special symbols

The combined character set is:

$$
C = L \cup U \cup D \cup S
$$

The number of available characters is:

$$
|C| = 26 + 26 + 10 + 32 = 94
$$

2. Password Generation

The user provides two inputs:

$l$ = Desired password length
$n$ = Number of passwords required

Each character is independently selected from the combined character pool using:

secrets.choice(possible_password)

The generated password is constructed by joining the selected characters.

3. Password Combination Possibilities

For a character pool containing 94 characters and a password length of $l$, the total number of possible passwords is:

$$
P = 94^l
$$

For example, with a password length of 8:

$$
P = 94^8
$$

This provides a large number of possible password combinations.

The theoretical entropy, assuming independent and uniformly distributed character selections, is:

$$
H = l \log_2(94)
$$

Approximately:

$$
H \approx 6.55l \text{ bits}
$$

4. Saving Passwords

After generating the requested passwords, the application displays them in the console.

Users are then asked whether they want to save the generated passwords.

If the user agrees, the application uses Python file handling to append the passwords to:

passwords.txt
🚀 Getting Started
Prerequisites
Python 3.x installed on your system.
A terminal or command-line interface.
Installation

1. Clone the repository

git clone https://github.com/MustbeSarthak/Password-Generator-.git

2. Navigate to the project directory

cd Password-Generator-

3. Run the application

python main.py
📂 Project Structure
Password-Generator/
│
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
└── passwords.txt

Note: passwords.txt is created locally when the user chooses to save generated passwords. It should not be committed to a public repository.

📚 Concepts Practiced

This project demonstrates the practical implementation of:

Python modules and imports.
Variables and user input.
Loops and conditional statements.
String manipulation.
Random character selection.
Lists and iteration.
File handling.
🔒 Security Note

The application uses Python's secrets module, which is designed for generating cryptographically strong random values.

However, passwords saved in a plain-text file are not encrypted. Avoid storing real account credentials in an exposed or publicly accessible file.

<div align="center">

Developed as part of the Auspify Technologies Python Developer Internship

Made with 🐍 Python and 🔐

</div>