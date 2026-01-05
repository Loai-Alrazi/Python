#Rock Game
import random

# --- دوال الرسم (من الإجابة السابقة) ---
def draw_rock():
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

def draw_paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

def draw_scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
# -------------------------------------

print("Welcom to the Rock, paper, Scissors game:\n" \
"Press Enter to continue or type (Help) for the rules")
chois = input("Enter your choise (rock, paper, scissors):>").lower() # تحويل المدخل إلى حروف صغيرة

# قاموس لربط الاختيار النصي بالدالة المناسبة
choices_map = {
    "rock": draw_rock,
    "paper": draw_paper,
    "scissors": draw_scissors
}

lis = ["rock", "paper", "scissors"]

if chois in lis:
    cop_chois = random.choice(lis)
    
    # --- هنا هو التعديل المطلوب ---
    print(f"\nYour choice ({chois}):")
    # استدعي الدالة المرتبطة باختيار المستخدم من القاموس
    choices_map[chois]() 

    print(f"Computer choice ({cop_chois}):")
    # استدعي الدالة المرتبطة باختيار الكمبيوتر من القاموس
    choices_map[cop_chois]()
    # ----------------------------
    
    # منطق اللعبة لتحديد الفائز (مكمل للكود الناقص)
    if chois == cop_chois:
        print("It's a draw!")
    elif (chois == "rock" and cop_chois == "scissors") or \
         (chois == "scissors" and cop_chois == "paper") or \
         (chois == "paper" and cop_chois == "rock"):
        print("You win!")
    else:
        print("You lose!")

else:
    print("Invalid choice. Please enter rock, paper, or scissors.")

