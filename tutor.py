questions = [
    {"question": "What ohm's law formula?", "answer": "v = i * r"},
    {"question": "What linux command shows your location?", "answer": "pwd"},
    {"question": "What does def mean in python?", "answer": "define a function"},
]
score = 0
for q in questions:
      print(q["question"])
      user_answer =input( "Your answer").lower()
      if user_answer ==q["answer"]:
          print("Correct")
          score = score + 1
      else:
           print("Wrong.The answer is :", q["answer"])

print("you got", score, "out of", len(questions))
