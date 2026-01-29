questions = [line.strip() for line in open('question.txt')]
answers = [line.strip() for line in open("answer.txt")]

num_right = 0

for i in range (len(questions)):
        guess = input(questions[i])
        if guess.lower()==answers[i].lower():
                print('Correct!')
                num_right+=1
        else:
                print('Wrong. The answer is: ', answers[i])

print('You have', num_right, 'out of', i+1)
