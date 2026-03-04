# 🔐 Password Strength Checker

A simple **Python-based Password Strength Checker** that evaluates how secure a password is using common password security practices.

The program checks whether a password is **Weak, Moderate, or Strong** based on several security criteria such as password length, character variety, and special characters.

---

## 📌 Features

* ✔ Checks minimum password length
* ✔ Detects **lowercase letters**
* ✔ Detects **uppercase letters**
* ✔ Detects **numbers**
* ✔ Detects **special characters**
* ✔ Provides **password strength classification**

---

## 🧠 How It Works

The program evaluates the password using **five security criteria**:

1. Password length **(minimum 8 characters)**
2. Presence of **lowercase letters**
3. Presence of **uppercase letters**
4. Presence of **numbers**
5. Presence of **special characters**

Each satisfied condition increases the **password strength score**.

---

## 📊 Strength Levels

| Score | Strength    |
| ----- | ----------- |
| 0 – 2 | Weak ❌      |
| 3 – 4 | Moderate ⚠️ |
| 5     | Strong ✅    |

---

## 💻 Technologies Used

* **Python**
* **Regular Expressions (`re` module)**

---

## ▶️ Usage

1. Clone the repository

```
git clone https://github.com/your-username/password-strength-checker.git
```

2. Navigate to the project folder

```
cd password-strength-checker
```

3. Run the program

```
python password_checker.py
```

4. Enter a password when prompted to see its strength.

---

## 🧪 Example

```
Enter your password: Hello123

Password Score: 4/5
Password Strength: Moderate ⚠️
```

Example 2:

```
Enter your password: H3llo@Secure

Password Score: 5/5
Password Strength: Strong ✅
```

---

## 🚀 Future Improvements

Possible improvements for this project:

* 🔎 Password strength **suggestions**
* 📊 **Password entropy calculation**
* 🖥 **GUI interface using Tkinter**
* 🌐 **Web version using Flask**
* 🚫 Detect **common weak passwords**

---
