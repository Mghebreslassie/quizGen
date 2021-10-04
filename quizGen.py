def create_quizzes(path):
    '''
    no testing or validation on this simple script
    creates 35 text files each with 50 randomly
    generated questions about state and capitals.
    
    '''
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    import os
    os.chdir(path)
    import random
    for quiz in range(35):
        #shuffle the states list
        states_list = list(capitals.keys())
        city_list = list(capitals.values())
        random.shuffle(states_list)
        #get the right answer
        correct_capital_city = states_list[0]
        #pick 3 wrong answers
        def get_wrong_answers(correct_capital_city):
            random.shuffle(city_list)
            wrong_answers = []
            index = 0
            while len(wrong_answers) < 3:
                city = city_list[index]
                if city != correct_capital_city:
                    wrong_answers.append(city)
                index += 1
            #mix them up and assign to a,b,c,d
            answers = wrong_answers + [correct_capital_city]
            random.shuffle(answers)
            return answers
        #write answer to asnwer key
        #50 questions
        quiz_file = open(f'quizfile{quiz+1}.txt', 'a')
        answer_key = open(f'answerkey{quiz+1}.txt', 'a')
        for index, state in enumerate(states_list):
            correct_capital_city = capitals[state]
            answers = get_wrong_answers(correct_capital_city)
            quiz_file.write(f'Question {index+1}.) What is the capital of {state}?\n')
            answer_key.write(f'Question #{index+1} Answer: {correct_capital_city}\n')
            for count, option in enumerate(answers):
                options = ['a','b','c','d']
                quiz_file.write(f'{options[count]}.) {answers[count]}\n')
        quiz_file.close()
        answer_key.close()
        #do that 35 times