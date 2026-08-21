# SmartQuiz Evaluator 📝

> *An intelligent Python-based offline application for quiz management and automated evaluation*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Prototype-orange.svg)]()

---

## 🎯 About SmartQuiz Evaluator

**SmartQuiz Evaluator** is a comprehensive Python-based application designed for efficient quiz management and automated evaluation. It empowers quiz creators to design flexible assessments and enables participants to take quizzes with real-time scoring feedback.

### 🌟 Key Features

✨ **Secure Authentication**
- User signup and login system
- Secure credential validation
- Role-based access control (Quiz Creators vs. Participants)

🎨 **Flexible Quiz Creation**
- Custom number of questions per quiz
- Multiple-choice options (2-5 options per question)
- Individual marks assignment per question
- Unique Quiz IDs for easy sharing

⚡ **Real-Time Scoring**
- Instant score calculation during quiz progression
- Marks display for each question
- Total score summary after completion

📊 **Response Dashboard**
- View all participants who took a specific quiz
- Detailed answer analysis
- Correct vs. incorrect answer comparison
- Score tracking per participant

🔒 **Data Security**
- JSON-based persistent storage
- Separation of user data, quizzes, and responses
- Automatic data initialization

---

## 📋 Table of Contents

- [Features](#-key-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Data Schema](#-data-schema)
- [Roadmap](#-roadmap-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Basic understanding of command line/terminal

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd projects/smartquiz-evaluator
   ```

2. **Install dependencies** (if needed)
   ```bash
   pip install -r requirements.txt
   ```
   > Note: Current version uses only built-in Python modules

3. **Verify files are in place**
   ```bash
   ls -la
   # Should show: smartquiz.py, requirements.txt, sample_data/
   ```

---

## ⚡ Quick Start

### Running the Application

```bash
python smartquiz.py
```

### First-Time Setup

1. **Create an Account:**
   - Select option `2. Sign Up`
   - Enter a unique username
   - Create a secure password

2. **Create Your First Quiz:**
   - Select option `1. Create a Quiz`
   - Enter number of questions
   - Add questions with options and mark values
   - Share the Quiz ID with participants

3. **Take a Quiz:**
   - Select option `2. Take a Quiz`
   - Enter the Quiz ID
   - Answer all questions
   - View your score and correct answers

4. **Review Responses:**
   - Select option `3. View Responses` (only available for quiz creators)
   - See all participants and their scores
   - View detailed answer analysis

---

## 💡 Usage Guide

### For Quiz Creators

```python
# Step 1: Login/Signup
# Choose option 1 or 2 and create your account

# Step 2: Create Quiz
# Main Menu → Option 1: Create a Quiz
# - Enter number of questions (e.g., 5)
# - For each question:
#   - Enter question text
#   - Enter number of options (2-5)
#   - Enter each option (A, B, C, etc.)
#   - Specify correct answer letter
#   - Assign marks for the question
# - Quiz ID is generated automatically
# - Share this ID with participants

# Step 3: View Responses
# Main Menu → Option 3: View Responses
# - Enter Quiz ID you created
# - Select a participant
# - Review their answers and scores
```

### For Quiz Participants

```python
# Step 1: Login/Signup
# Create your account

# Step 2: Take Quiz
# Main Menu → Option 2: Take a Quiz
# - Enter Quiz ID from creator
# - Answer each question by entering option letter
# - View immediate score
# - Choose to view correct answers

# Your responses are automatically saved
```

### Sample Quiz Walkthrough

```
Quiz ID: 1234
Question 1: What is the capital of France? [5 marks]
A. London
B. Paris
C. Berlin
D. Madrid

Your Answer: B
Correct Answer: B ✓ (+5 marks)
```

---

## 🏗️ Project Structure

```
smartquiz-evaluator/
├── smartquiz.py              # Main application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── sample_data/
    ├── users.json            # Sample user credentials
    ├── quizzes.json          # Sample quiz data
    └── responses.json        # Sample participant responses
```

---

## 📊 Data Schema

### Users File (`users.json`)
```json
{
  "username1": {
    "password": "password123"
  },
  "username2": {
    "password": "password456"
  }
}
```

### Quizzes File (`quizzes.json`)
```json
{
  "1234": {
    "creator": "username1",
    "questions": [
      {
        "question": "What is 2+2?",
        "options": ["3", "4", "5", "6"],
        "correct": "B",
        "marks": 5
      }
    ]
  }
}
```

### Responses File (`responses.json`)
```json
{
  "1234": {
    "participant_username": ["A", "B", "C", "B"]
  }
}
```

---

## 🔄 Roadmap: Future Enhancements

### Phase 1: Database Integration (Coming Soon)
- [ ] Migrate from JSON to MySQL database
- [ ] Implement SQLAlchemy ORM
- [ ] Create database schema with proper relationships
- [ ] Add data validation and integrity checks

### Phase 2: Web Application
- [ ] Build Flask/Django backend
- [ ] Create responsive frontend (HTML/CSS/JavaScript)
- [ ] Deploy to online platform
- [ ] Enable multi-user concurrent access

### Phase 3: Advanced Features
- [ ] Timer functionality for quizzes
- [ ] Question shuffling and randomization
- [ ] Negative marking for wrong answers
- [ ] Leaderboard and rankings
- [ ] Export results to PDF/CSV
- [ ] Analytics and performance insights
- [ ] Question bank management
- [ ] Automated email notifications

### Phase 4: Production Ready
- [ ] User authentication (JWT tokens)
- [ ] Role-based access control
- [ ] Admin dashboard
- [ ] API documentation
- [ ] Unit and integration tests
- [ ] Deployment configuration (Docker, Cloud)

---

## 🛠️ Technical Stack

**Current (Offline Version):**
- Python 3.7+
- JSON (data storage)
- OS module (file operations)
- Random module (ID generation)

**Planned (Online Version):**
- Backend: Python (Flask/Django)
- Database: MySQL/PostgreSQL
- Frontend: HTML5, CSS3, JavaScript/React
- Authentication: JWT tokens
- Hosting: Cloud platform (AWS/Heroku/DigitalOcean)

---

## 🐛 Troubleshooting

### Issue: "Quiz ID not found"
- **Solution:** Verify the Quiz ID from the creator and ensure it's entered correctly

### Issue: "Username already exists"
- **Solution:** Choose a different username during signup

### Issue: JSON file corruption
- **Solution:** Delete the corrupted `.json` file and restart the application (it will auto-create)

### Issue: "Only the quiz creator can view responses"
- **Solution:** Login with the account that created the quiz

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs:** Found an issue? Open an issue with details
2. **Suggest Features:** Have ideas for new features? Share them!
3. **Improve Code:** Submit pull requests with enhancements
4. **Documentation:** Help improve documentation and examples

### Development Setup
```bash
# Clone the repository
git clone https://github.com/SanatanaMR/Resanate.git
cd projects/smartquiz-evaluator

# Run the application
python smartquiz.py

# Suggest improvements!
```

---

## 📚 Learning Outcomes

This project demonstrates proficiency in:

- ✅ File I/O operations in Python
- ✅ JSON data handling and serialization
- ✅ Authentication and authorization concepts
- ✅ Menu-driven application design
- ✅ Data persistence and storage
- ✅ User input validation
- ✅ Control flow and logic
- ✅ Object-oriented concepts (preparation for OOP)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

---

## 📫 Support & Questions

Have questions about SmartQuiz Evaluator?

- **Email**: [sm4932@srmist.edu.in](mailto:sm4932@srmist.edu.in)
- **Email**: [mrsanatana2020@gmail.com](mailto:mrsanatana2020@gmail.com)
- **GitHub**: [@SanatanaMR](https://github.com/SanatanaMR)

---

## 🎯 Next Steps

- ⭐ Give this project a star if you find it useful!
- 🔗 Follow the journey as it evolves into a full-fledged web application
- 💬 Share feedback and suggestions for improvements
- 🤝 Consider contributing to the development

---

**Made with ❤️ by [SanatanaMR](https://github.com/SanatanaMR)**

*This is a prototype version. Stay tuned for the online platform launch!*

*Last updated: August 2026*
