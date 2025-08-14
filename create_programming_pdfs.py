"""
Create Programming Language Educational PDFs for Quiz Generation
Covers Python, JavaScript, Java, C++, and Web Development
"""

import fitz  # PyMuPDF

def create_python_programming_pdf():
    """Create Python Programming PDF with comprehensive content"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Python Programming Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
Python Programming Language

Introduction to Python
Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum in 1991, Python emphasizes code readability and allows programmers to express concepts in fewer lines of code.

Key Features of Python:
- Easy to learn and use
- Interpreted language (no compilation needed)
- Object-oriented programming support
- Extensive standard library
- Cross-platform compatibility
- Dynamic typing
- Automatic memory management

Python Syntax Basics

Variables and Data Types:
Python uses dynamic typing, meaning you don't need to declare variable types explicitly.

Basic data types:
- int: Integer numbers (e.g., 42, -17)
- float: Decimal numbers (e.g., 3.14, -2.5)
- str: Text strings (e.g., "Hello World")
- bool: Boolean values (True or False)
- list: Ordered collection [1, 2, 3]
- dict: Key-value pairs {"name": "John", "age": 25}
- tuple: Immutable sequence (1, 2, 3)

Variable Assignment:
name = "Alice"
age = 30
height = 5.6
is_student = True

Control Structures

Conditional Statements:
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block

Example:
age = 18
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

Loops:
For loop - iterates over sequences:
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4

for item in [1, 2, 3]:
    print(item)

While loop - continues while condition is true:
count = 0
while count < 5:
    print(count)
    count += 1

Functions in Python

Function Definition:
def function_name(parameters):
    # function body
    return value

Example:
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # result = 8

Function Parameters:
- Default parameters: def greet(name="World"):
- Keyword arguments: greet(name="Alice")
- Variable arguments: def sum_all(*args):
- Keyword variable arguments: def process(**kwargs):

Object-Oriented Programming

Classes and Objects:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating objects
person1 = Person("Alice", 25)
print(person1.introduce())

Inheritance:
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        return f"{self.name} is studying"

Data Structures

Lists:
- Ordered, mutable collection
- Can contain different data types
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

List methods:
- append(): add item to end
- insert(): add item at specific position
- remove(): remove first occurrence
- pop(): remove and return item
- sort(): sort the list
- len(): get length

Dictionaries:
- Key-value pairs
- Unordered (Python 3.7+ maintains insertion order)
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 78]
}

Dictionary methods:
- keys(): get all keys
- values(): get all values
- items(): get key-value pairs
- get(): safely get value
- update(): update with another dict

File Handling

Reading Files:
# Method 1
file = open("data.txt", "r")
content = file.read()
file.close()

# Method 2 (recommended)
with open("data.txt", "r") as file:
    content = file.read()

Writing Files:
with open("output.txt", "w") as file:
    file.write("Hello, World!")

File modes:
- "r": read mode
- "w": write mode (overwrites)
- "a": append mode
- "r+": read and write

Error Handling

Try-Except Blocks:
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")

Libraries and Modules

Importing Modules:
import math
from datetime import datetime
import numpy as np
from collections import Counter

Popular Python Libraries:
- NumPy: Numerical computing
- Pandas: Data manipulation and analysis
- Matplotlib: Data visualization
- Requests: HTTP library
- Flask/Django: Web frameworks
- TensorFlow/PyTorch: Machine learning
- Beautiful Soup: Web scraping

List Comprehensions

Basic syntax:
[expression for item in iterable if condition]

Examples:
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]

Lambda Functions

Anonymous functions:
lambda arguments: expression

Examples:
add = lambda x, y: x + y
square = lambda x: x**2

# Used with map, filter, sort
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

Best Practices

Code Style (PEP 8):
- Use 4 spaces for indentation
- Line length should not exceed 79 characters
- Use descriptive variable names
- Add comments and docstrings
- Follow naming conventions:
  - Variables: snake_case
  - Functions: snake_case
  - Classes: PascalCase
  - Constants: UPPER_CASE

Documentation:
def calculate_area(radius):
    # Calculate the area of a circle
    # Args: radius (float) - The radius of the circle
    # Returns: float - The area of the circle
    return 3.14159 * radius ** 2

Testing:
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

Common Programming Patterns

Iterating with enumerate:
items = ["apple", "banana", "cherry"]
for index, item in enumerate(items):
    print(f"{index}: {item}")

Zip function:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

Context managers:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

Python Applications:
- Web Development (Django, Flask)
- Data Science and Analytics
- Machine Learning and AI
- Automation and Scripting
- Desktop Applications
- Game Development
- Scientific Computing
- Network Programming
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Python_Programming_Guide.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_javascript_pdf():
    """Create JavaScript Programming PDF"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "JavaScript Programming Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
JavaScript Programming Language

Introduction to JavaScript
JavaScript is a high-level, interpreted programming language that is one of the core technologies of the World Wide Web. Originally created for web browsers, JavaScript is now used for server-side development, mobile apps, and desktop applications.

Key Features:
- Dynamic typing
- First-class functions
- Prototype-based object orientation
- Event-driven programming
- Asynchronous programming support
- Cross-platform compatibility

JavaScript Basics

Variables and Data Types:
// Variable declarations
var name = "John";        // Function-scoped
let age = 25;            // Block-scoped
const PI = 3.14159;      // Constant

// Data types
let number = 42;         // Number
let text = "Hello";      // String
let isTrue = true;       // Boolean
let nothing = null;      // Null
let undefined_var;       // Undefined
let obj = {};           // Object
let arr = [];           // Array

Functions:
// Function declaration
function greet(name) {
    return "Hello, " + name + "!";
}

// Function expression
const add = function(a, b) {
    return a + b;
};

// Arrow function (ES6)
const multiply = (a, b) => a * b;

// Higher-order functions
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);
const evens = numbers.filter(x => x % 2 === 0);

Objects and Arrays:
// Object literal
const person = {
    name: "Alice",
    age: 30,
    greet: function() {
        return `Hello, I'm ${this.name}`;
    }
};

// Array methods
const fruits = ["apple", "banana", "orange"];
fruits.push("grape");        // Add to end
fruits.pop();               // Remove from end
fruits.unshift("mango");    // Add to beginning
fruits.shift();             // Remove from beginning

Control Structures:
// Conditional statements
if (age >= 18) {
    console.log("Adult");
} else if (age >= 13) {
    console.log("Teenager");
} else {
    console.log("Child");
}

// Switch statement
switch (day) {
    case "Monday":
        console.log("Start of work week");
        break;
    case "Friday":
        console.log("TGIF!");
        break;
    default:
        console.log("Regular day");
}

// Loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

for (let item of array) {
    console.log(item);
}

for (let key in object) {
    console.log(key, object[key]);
}

DOM Manipulation:
// Selecting elements
const element = document.getElementById("myId");
const elements = document.getElementsByClassName("myClass");
const element2 = document.querySelector(".myClass");
const elements2 = document.querySelectorAll("div");

// Modifying elements
element.innerHTML = "New content";
element.style.color = "red";
element.classList.add("newClass");

// Event handling
element.addEventListener("click", function() {
    console.log("Element clicked!");
});

Asynchronous Programming:
// Callbacks
function fetchData(callback) {
    setTimeout(() => {
        callback("Data received");
    }, 1000);
}

// Promises
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Success!");
    }, 1000);
});

promise.then(result => {
    console.log(result);
}).catch(error => {
    console.error(error);
});

// Async/Await
async function fetchUserData() {
    try {
        const response = await fetch("/api/user");
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error:", error);
    }
}

ES6+ Features:
// Template literals
const message = `Hello, ${name}! You are ${age} years old.`;

// Destructuring
const {name, age} = person;
const [first, second] = array;

// Spread operator
const newArray = [...oldArray, newItem];
const newObject = {...oldObject, newProperty: value};

// Classes
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks`);
    }
}

Error Handling:
try {
    // Code that might throw an error
    let result = riskyOperation();
} catch (error) {
    console.error("An error occurred:", error.message);
} finally {
    console.log("This always runs");
}

JavaScript in Web Development:
- Client-side scripting
- Server-side development (Node.js)
- Single Page Applications (SPAs)
- Progressive Web Apps (PWAs)
- Mobile app development (React Native)
- Desktop applications (Electron)
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "JavaScript_Programming_Guide.pdf"
    doc.save(filename)
    doc.close()
    return filename

def create_web_development_pdf():
    """Create Web Development PDF"""
    doc = fitz.open()
    page = doc.new_page()
    
    page.insert_text((50, 50), "Web Development Fundamentals", fontsize=18, color=(0, 0, 0))
    
    content = """
Web Development Fundamentals

Introduction to Web Development
Web development involves creating websites and web applications for the internet. It encompasses both frontend (client-side) and backend (server-side) development, along with database management and server configuration.

Frontend Technologies:
- HTML: Structure and content
- CSS: Styling and layout
- JavaScript: Interactivity and behavior

Backend Technologies:
- Server-side languages (Python, JavaScript, PHP, Java)
- Databases (MySQL, PostgreSQL, MongoDB)
- Web servers (Apache, Nginx)

HTML (HyperText Markup Language)

Basic Structure:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <h1>Main Heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>

Common HTML Elements:
- <h1> to <h6>: Headings
- <p>: Paragraphs
- <a href="url">: Links
- <img src="image.jpg" alt="description">: Images
- <div>: Generic container
- <span>: Inline container
- <ul>, <ol>, <li>: Lists
- <table>, <tr>, <td>: Tables
- <form>, <input>, <button>: Forms

Semantic HTML:
- <header>: Page or section header
- <nav>: Navigation links
- <main>: Main content
- <section>: Thematic grouping
- <article>: Independent content
- <aside>: Sidebar content
- <footer>: Page or section footer

CSS (Cascading Style Sheets)

CSS Syntax:
selector {
    property: value;
    property: value;
}

Example:
h1 {
    color: blue;
    font-size: 24px;
    text-align: center;
}

Selectors:
- Element: h1, p, div
- Class: .className
- ID: #idName
- Attribute: [type="text"]
- Pseudo-class: :hover, :focus
- Pseudo-element: ::before, ::after

Box Model:
Every element has:
- Content: The actual content
- Padding: Space inside the element
- Border: Edge of the element
- Margin: Space outside the element

Layout Methods:
- Flexbox: One-dimensional layout
- Grid: Two-dimensional layout
- Float: Legacy layout method
- Position: absolute, relative, fixed, sticky

Responsive Design:
@media screen and (max-width: 768px) {
    .container {
        width: 100%;
        padding: 10px;
    }
}

JavaScript for Web Development

DOM Manipulation:
// Selecting elements
const button = document.getElementById('myButton');
const items = document.querySelectorAll('.item');

// Modifying content
button.textContent = 'Click me!';
button.innerHTML = '<strong>Click me!</strong>';

// Styling elements
button.style.backgroundColor = 'blue';
button.classList.add('active');

Event Handling:
button.addEventListener('click', function() {
    alert('Button clicked!');
});

// Form handling
const form = document.getElementById('myForm');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(form);
    // Process form data
});

AJAX and Fetch API:
// Fetch API
fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Update UI with data
    })
    .catch(error => {
        console.error('Error:', error);
    });

// Async/await
async function loadData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

Backend Development Concepts

Server-Side Programming:
- Handle HTTP requests (GET, POST, PUT, DELETE)
- Process form data
- Interact with databases
- Implement authentication and authorization
- Generate dynamic content

RESTful APIs:
- GET /users: Retrieve all users
- GET /users/123: Retrieve specific user
- POST /users: Create new user
- PUT /users/123: Update user
- DELETE /users/123: Delete user

Database Integration:
// Example with Node.js and MongoDB
const express = require('express');
const mongoose = require('mongoose');

const User = mongoose.model('User', {
    name: String,
    email: String,
    age: Number
});

app.get('/users', async (req, res) => {
    const users = await User.find();
    res.json(users);
});

app.post('/users', async (req, res) => {
    const user = new User(req.body);
    await user.save();
    res.json(user);
});

Web Security:
- Input validation and sanitization
- SQL injection prevention
- Cross-Site Scripting (XSS) protection
- Cross-Site Request Forgery (CSRF) protection
- HTTPS encryption
- Authentication and authorization

Modern Web Development

Frontend Frameworks:
- React: Component-based library
- Vue.js: Progressive framework
- Angular: Full-featured framework

Build Tools:
- Webpack: Module bundler
- Babel: JavaScript compiler
- npm/yarn: Package managers
- Gulp/Grunt: Task runners

Version Control:
- Git: Distributed version control
- GitHub/GitLab: Code hosting platforms
- Branching and merging strategies
- Collaborative development workflows

Deployment:
- Web hosting services
- Cloud platforms (AWS, Google Cloud, Azure)
- Content Delivery Networks (CDNs)
- Continuous Integration/Deployment (CI/CD)

Performance Optimization:
- Minification and compression
- Image optimization
- Caching strategies
- Lazy loading
- Code splitting
"""
    
    text_rect = fitz.Rect(50, 80, 550, 750)
    page.insert_textbox(text_rect, content, fontsize=10, color=(0, 0, 0))
    
    filename = "Web_Development_Guide.pdf"
    doc.save(filename)
    doc.close()
    return filename

def main():
    """Create programming language PDFs"""
    print("💻 Creating Programming Language Educational PDFs...")
    print("=" * 60)
    
    created_files = []
    
    # Create programming PDFs
    programming_subjects = [
        ("Python Programming", create_python_programming_pdf),
        ("JavaScript Programming", create_javascript_pdf),
        ("Web Development", create_web_development_pdf)
    ]
    
    for subject_name, create_func in programming_subjects:
        try:
            filename = create_func()
            created_files.append(filename)
            print(f"✅ Created: {filename}")
        except Exception as e:
            print(f"❌ Error creating {subject_name} PDF: {e}")
    
    print("\n" + "=" * 60)
    print(f"🎉 Successfully created {len(created_files)} programming PDFs!")
    print("\n💻 Programming subjects for quiz generation:")
    
    for i, filename in enumerate(created_files, 1):
        subject = filename.replace("_", " ").replace(".pdf", "")
        print(f"{i}. {subject}")
    
    print("\n🎯 Perfect for programming education!")
    print("📝 Each PDF contains comprehensive programming concepts")
    print("🤖 AI will generate code-related multiple-choice questions")
    print("✅ Upload these PDFs to StudyMate for programming quizzes!")

if __name__ == "__main__":
    main()
