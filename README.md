# LexiScan: A PLY-Based Lexical Analyzer

## 📌 Overview
LexiScan is a **Python-based lexical analyzer** built using **PLY (Python Lex-Yacc)**. It tokenizes source code, identifying keywords, identifiers, constants, operators, separators, and comments. This project is designed to help in **syntax analysis** and serves as a foundational component for interpreters and compilers.

## 🎯 Objective
The goal of this project is to develop a **robust lexical analyzer** that efficiently processes C- (C Minus) language code and extracts meaningful tokens for further analysis.

### Key Features:
- **Keyword Recognition**: Detects C- language keywords.
- **Token Classification**: Differentiates identifiers, constants, operators, and separators.
- **Comment Handling**: Recognizes and ignores block comments.
- **Error Handling**: Reports illegal characters gracefully.
- **Line Number Tracking**: Keeps track of line numbers for debugging.

## 🚀 How It Works
1. **Reads the source code** from `Cminus.txt`.
2. **Tokenizes the input** using predefined patterns.
3. **Classifies tokens** into categories such as keywords, identifiers, and operators.
4. **Prints the output** in a structured format.

## 🏗️ Project Structure
```
|-- Lex.py  # Main lexical analyzer script
|-- Cminus.txt  # Sample source code for testing
|-- Cminus programming language.pdf  # Cminus programming language file
|-- Lex-Doc  # Documentation
|-- README.md  # Documentation
```

## 🛠️ Technologies Used
- **Python** for processing.
- **PLY (Python Lex-Yacc)** for tokenization.
- **Regular Expressions** for defining token patterns.

## 📖 Getting Started
### Prerequisites
- Python 3.8+
- Install PLY:
  ```bash
  pip install ply
  ```

### Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/HareenaChowdary/LexiScan.git
   cd LexiScan
   ```
2. Run the lexer:
   ```bash
   python Lex.py
   ```

## 🧐 Example Output
Given the following input in `Cminus.txt`:
```c
int main() {
  int x = 10;
  /* This is a comment */
  x = x + 5;
  return x;
}
```
LexiScan will output:
```bash
(KEYWORD, 'int')
(IDENTIFIER, 'main')
(SEPARATOR, '(')
(SEPARATOR, ')')
(SEPARATOR, '{')
(KEYWORD, 'int')
(IDENTIFIER, 'x')
(ARITH_OP, '=')
(CONSTANT, '10')
(SEPARATOR, ';')
(COMMENT, '/* This is a comment */')
(IDENTIFIER, 'x')
(ARITH_OP, '=')
(IDENTIFIER, 'x')
(ARITH_OP, '+')
(CONSTANT, '5')
(SEPARATOR, ';')
(KEYWORD, 'return')
(IDENTIFIER, 'x')
(SEPARATOR, ';')
(SEPARATOR, '}')
```

## 🤝 Contributing
Pull requests are welcome! If you find a bug or want to enhance the functionality, feel free to contribute.

## 📧 Contact
Looking for collaboration? Reach out on [LinkedIn](https://www.linkedin.com/in/hareena-chowdary-polavaram/).

---
🚀 **LexiScan – Turning Source Code into Meaningful Tokens!**

