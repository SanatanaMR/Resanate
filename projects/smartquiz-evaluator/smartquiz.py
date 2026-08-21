import json 
import os 
import random 
# === File Utilities === 
def load_data(filename): 
 if not os.path.exists(filename): 
 return {} 
 try: 
 with open(filename, 'r') as f: 
 return json.load(f) 
 except Exception: 
 with open(filename, 'w') as f: 
 json.dump({}, f) 
 return {} 
def save_data(filename, data): 
 with open(filename, 'w') as f: 
 json.dump(data, f, indent=4) 
# === Global Files === 
USERS_FILE = 'users.json' 
QUIZZES_FILE = 'quizzes.json' 
RESPONSES_FILE = 'responses.json' 
users = load_data(USERS_FILE) 
quizzes = load_data(QUIZZES_FILE) 
responses = load_data(RESPONSES_FILE) 
# === Authentication === 
def signup(): 
 print("\n--- Sign Up ---") 
 username = input("Create username: ").strip() 
 if username in users: 
 print("Username already exists. Try logging in or choose another.") 
 return None 
 password = input("Create password: ").strip() 
 users[username] = {"password": password} 
 save_data(USERS_FILE, users) 
 print("Account created successfully!") 
 return username 
def login(): 
 print("\n--- Login ---") 
 username = input("Username: ").strip() 
 password = input("Password: ").strip() 
 if username in users and users[username]["password"].strip() == password.strip(): 
 print("Login successful!") 
 return username 
 else:
 print("Incorrect username or password.") 
 return None 
def authenticate(): 
 while True: 
 choice = input("\n1. Login\n2. Sign Up\nChoose option (1/2): ")  
 if choice == '1': 
 user = login() 
 if user: 
 return user 
 elif choice == '2': 
 user = signup() 
 if user: 
 return user 
 else: 
 print("Invalid choice.") 
# === Quiz Creation === 
def create_quiz(username): 
 print("\n--- Create Quiz ---") 
 quiz_id = str(random.randint(1000, 9999)) 
 while quiz_id in quizzes: 
 quiz_id = str(random.randint(1000, 9999)) 
 num_qns = int(input("Enter number of questions: "))  
 questions = [] 
 for i in range(num_qns): 
 print(f"\nQuestion {i+1}:") 
 q_text = input("Enter question: ") 
 options = [] 
 opt_count = int(input("Enter number of options (2-5): "))  
 for j in range(opt_count): 
 opt = input(f"Option {chr(65+j)}: ") 
 options.append(opt) 
 correct = input("Enter correct option letter (A/B/C/...): ").upper() 
 score = int(input("Enter marks for this question: "))  
 questions.append({ 
 "question": q_text, 
 "options": options, 
 "correct": correct, 
 "marks": score 
 }) 
 quizzes[quiz_id] = { 
 "creator": username, 
 "questions": questions 
 } 
 save_data(QUIZZES_FILE, quizzes) 
 print(f"Quiz created! Share this Quiz ID: {quiz_id}") 
# === Take Quiz === 
def take_quiz(username): 
 print("\n--- Take a Quiz ---") 
 quiz_id = input("Enter Quiz ID: ").strip() 
 if quiz_id not in quizzes: 
 print("Invalid Quiz ID.") 
 return 
 questions = quizzes[quiz_id]['questions'] 
 answers = []
 total_score = 0 
 obtained = 0 
 for i, q in enumerate(questions): 
 print(f"\nQ{i+1}: {q['question']} [{q['marks']} marks]")  
 for j, opt in enumerate(q['options']): 
 print(f" {chr(65+j)}. {opt}") 
 ans = input("Your answer (A/B/...): ").upper()  
 answers.append(ans) 
 total_score += q['marks'] 
 if ans == q['correct']: 
 obtained += q['marks'] 
 print(f"\nYou scored {obtained}/{total_score}") 
 view_ans = input("Do you want to view correct answers? (y/n): ").lower() 
 if view_ans == 'y': 
 for i, q in enumerate(questions): 
 print(f"\nQ{i+1}: {q['question']}") 
 print(f" Your answer: {answers[i]} | Correct: {q['correct']} | Marks: {q['marks']} - {'Correct' if answers[i]==q['correct'] else 'Wrong'}") 
 if quiz_id not in responses: 
 responses[quiz_id] = {} 
 responses[quiz_id][username] = answers 
 save_data(RESPONSES_FILE, responses) 
# === View Responses === 
def view_responses(username): 
 print("\n--- View Responses ---") 
 quiz_id = input("Enter Quiz ID: ").strip() 
 if quiz_id not in quizzes: 
 print("Invalid Quiz ID.") 
 return 
 if quizzes[quiz_id]['creator'] != username: 
 print("Only the quiz creator can view responses.")  
 return 
 if quiz_id not in responses or not responses[quiz_id]:  
 print("No responses yet.") 
 return 
 print("\nList of participants:") 
 for i, participant in enumerate(responses[quiz_id].keys(), 1):  
 print(f"{i}. {participant}") 
 chosen = input("Enter participant name to view answers: ").strip()  
 if chosen not in responses[quiz_id]: 
 print("No such participant.") 
 return 
 questions = quizzes[quiz_id]['questions'] 
 answers = responses[quiz_id][chosen] 
 for i, q in enumerate(questions): 
 print(f"\nQ{i+1}: {q['question']}") 
 print(f" Answer given: {answers[i]} | Correct: {q['correct']} | Marks: {q['marks']}") 
# === Main Menu === 
def main(): 
 current_user = authenticate() 
 while True: 
 print("\n--- Main Menu ---") 
 print("1. Create a Quiz")
 print("2. Take a Quiz") 
 print("3. View Responses")  
 print("4. Logout") 
 choice = input("Choose an option: ")  
 if choice == '1': 
 create_quiz(current_user)  
 elif choice == '2': 
 take_quiz(current_user)  
 elif choice == '3': 
 view_responses(current_user)  
 elif choice == '4': 
 print("Logging out...")  
 return main() 
 else: 
 print("Invalid choice.") 
if __name__ == "__main__": 
 main()
