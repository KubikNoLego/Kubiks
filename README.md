<p align="center">
    <img src="logo.png" width="300"/>
</p>
<h4 align="center">A simple and human-readable configuration language for Python.</h4>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🇺🇸 [**English**](README.en.md) | 🇷🇺 [Русский](README.ru.md)

# Introduction

**Kubiks** is a lightweight and human-readable configuration format for Python.

It was created as a more convenient alternative to JSON for situations where configuration files need to be edited manually. The syntax remains simple while supporting nested structures, lists, percentages, comments, and other useful features.

### Features

* ✨ Clean and readable syntax
* 📦 Support for nested objects and lists
* 💬 Comments directly inside configuration files
* 📊 Automatic percentage conversion
* 🔢 Integer and floating-point numbers
* ✅ Boolean values (`true` / `false`)
* ⭕ `null` values
* 🐍 Easy integration with Python

For example, the following file:

```kbk
player |= {
    username |= "KubikNoLego"
    level |= 42
    premium |= true
    win_rate |= 67%
}
```

Will be loaded as a regular Python dictionary:

```python
{
    "player": {
        "username": "KubikNoLego",
        "level": 42,
        "premium": True,
        "win_rate": 0.67
    }
}
```

# Loading a File

```python
from kubiks import load

config = load("config.kbk")
```

The `load()` function returns a standard Python dictionary that can be used anywhere in your application.

# Writing `.kbk` Files

All data is stored using a **key-value** format.

The assignment operator is `|=`:

```kbk
name |= "Kubik"
```

After loading:

```python
{
    "name": "Kubik"
}
```

# Supported Data Types

## Strings

Kubiks:

```kbk
name |= "Kubik"
```

Python:

```python
{
    "name": "Kubik"
}
```

---

## Null

Kubiks:

```kbk
title |= null
```

Python:

```python
{
    "title": None
}
```

---

## Integers

Kubiks:

```kbk
some_number |= -20
```

Python:

```python
{
    "some_number": -20
}
```

---

## Floating-Point Numbers

Kubiks:

```kbk
price |= 19.99
```

Python:

```python
{
    "price": 19.99
}
```

---

## Boolean Values

Kubiks:

```kbk
enabled |= true
admin |= false
```

Python:

```python
{
    "enabled": True,
    "admin": False
}
```

---

## Percentages

Kubiks:

```kbk
win_rate |= 67%
tax |= 20%
```

Python:

```python
{
    "win_rate": 0.67,
    "tax": 0.2
}
```

Percentages are automatically converted into decimal values.

---

# Lists

Kubiks:

```kbk
inventory |= [
    "wooden_sword",
    "iron_pickaxe",
    "golden_apple"
]
```

Python:

```python
{
    "inventory": [
        "wooden_sword",
        "iron_pickaxe",
        "golden_apple"
    ]
}
```

---

# Objects

Kubiks supports nested structures of any depth.

```kbk
user |= {
    username |= "KubikNoLego"

    statistics |= {
        games_played |= 156
        games_won |= 104
    }
}
```

Python:

```python
{
    "user": {
        "username": "KubikNoLego",
        "statistics": {
            "games_played": 156,
            "games_won": 104
        }
    }
}
```

---

# Comments

Comments start with the `#` character.

```kbk
# User settings
theme |= "dark"

# Enable notifications
notifications |= true
```

Comments are ignored when loading the file.

---

# License

This project is licensed under the MIT License.
