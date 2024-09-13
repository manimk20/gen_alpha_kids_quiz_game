def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer=input('Enter your answer (A,B,C,D): ').upper()
        if answer == question['answer']:
            print('Correct Kiddo!.You dona a Great Job!!!\n')
            score +=1
        else:
            print(f"Ohh...It's Wrong Buddy!.The correct answer is {question['answer']}.\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        'prompt':'What does for "AI"?',
        'options':['A. Amazing Intelligence','B.Artificial Intelligence','C.Animal Information', 'D.Awesome Inventions'],
        'answer':'B'
    },

    {
        'prompt':'Which Country have won more medals in Paris Olympics 2024?',
        'options':['A.Unites States','B.Chins','C.France','D.Japan'],
        'answer':'A'
    },

    {
        'prompt':"What is Asia's Largest Country?",
        'options':['A.Russia','B.China','C.India','D.Srilanka'],
        'answer':'A'
    },

    {
        'prompt':'What do we call a scientist who studies the stars and planets?',
        'options':['A.Biologis','B.Chemist','C.Astronomer','D.Archaeologist'],
        'answer':'C'
    },

    {
        'prompt':'how many consonant letters are there in english alphabet',
        'options':['A.18','B.26','C.21','29'],
        'answer':'C'
    },

    {
        'prompt':'What is the Color of Sun?',
        'options':['A.Orange','B.White','C.Blue','D.Yellow'],
        'answer':'B'
    },

    {
        'prompt':'What shape is Single Piece of Pizza?',
        'options':['A.Traingle','B.Circle','C.Oval','D.Cone'],
        'answer':'A'
    },

    {
        'prompt':'What gas do cars release that contributes to climate change?',
        'options':['A.Oxygen','B.Nitrogen','C.Helium','D.Carbon Dioxide'],
        'answer':'D'
    },

    {
        'prompt':'Who is own Youtube?',
        'options':['A.Meta','B.Google','C.Yahoo','D.Microsoft'],
        'answer':'B'
    },

    {
        'prompt':'Who has the most Followers on Instagram?',
        'options':['A.Messi','B.Taylor Swift','C.Cristiano Ronaldo','D.Kylie Jenner'],
        'answer':'C'
    }
]

run_quiz(questions)


