# Password Generator

A simple Python project to generate different types of passwords:
- Random passwords (with optional numbers and symbols)
- Memorable word-based passwords
- Numeric PIN codes

---

## Features

- Generate **random** secure passwords
- Create **memorable** passwords using a customizable word list
- Produce **numeric PINs** of any length
- Simple CLI interface (future-ready for GUI extension)
- Type hints and clear modular structure

---

## How It Works

### Random Password
Generates a password of letters, optionally including numbers and symbols.
```python
generate_random_password(length=12, include_numbers=True, include_symbols=True)
```

### Memorable Password
Creates a word-based password, separated by a custom character.
```python
generate_memorable_password(no_of_words=4, separator="-", capitalization=True)
```

### PIN Generator
Creates a simple numeric PIN.
```python
generate_pin(length=6)
```

## Running the Program

```bash
python src/password_generator.py
```
