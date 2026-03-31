import sys

def get_career_suggestion(answers):
    """
    Calculates scores for four primary career domains based on user input.
    Returns the top suggested category and the score breakdown.
    """

    scores = {
        'Technical': 0,      
        'Analytical': 0,     
        'Creative': 0,       
        'People-Oriented': 0 
    }

    q1_map = {
        'A': ('Technical', 3, 'Creative', 1),
        'B': ('Analytical', 3, 'Technical', 1),
        'C': ('People-Oriented', 3, 'Analytical', 1),
    }
    if answers['q1'] in q1_map:
        cat1, val1, cat2, val2 = q1_map[answers['q1']]
        scores[cat1] += val1
        scores[cat2] += val2

    q2_map = {
        'A': ('Technical', 2, 'Analytical', 2),
        'B': ('People-Oriented', 4),
        'C': ('Creative', 3, 'People-Oriented', 1),
    }
    if answers['q2'] in q2_map:
        if answers['q2'] == 'B':
            scores['People-Oriented'] += 4
        else:
            cat1, val1, cat2, val2 = q2_map[answers['q2']]
            scores[cat1] += val1
            scores[cat2] += val2

    q3_map = {
        'A': ('Creative', 4),
        'B': ('Technical', 3, 'Analytical', 1),
        'C': ('Analytical', 3, 'People-Oriented', 1),
    }
    if answers['q3'] in q3_map:
        if answers['q3'] == 'A':
            scores['Creative'] += 4
        else:
            cat1, val1, cat2, val2 = q3_map[answers['q3']]
            scores[cat1] += val1
            scores[cat2] += val2

    q4_map = {
        'A': ('Technical', 2),
        'B': ('Analytical', 2),
        'C': ('People-Oriented', 2),
        'D': ('Creative', 2),
    }
    if answers['q4'] in q4_map:
        cat, val = q4_map[answers['q4']]
        scores[cat] += val

    max_score = max(scores.values())
    top_categories = [k for k, v in scores.items() if v == max_score]

    suggestions = {
        'Technical': {
            'title': 'The Builder Path: Technical & Engineering',
            'summary': 'You thrive on understanding how things work, building robust systems, and applying scientific principles to create tangible solutions.',
            'careers': ['Software Engineer', 'Data Engineer', 'Mechanical Engineer', 'Network Administrator', 'Electrician'],
            'color': 'blue'
        },
        'Analytical': {
            'title': 'The Strategist Path: Analytical & Research',
            'summary': 'You have a keen eye for detail, enjoy diving into complex data, and are motivated by finding optimal solutions or winning strategies.',
            'careers': ['Data Scientist', 'Financial Analyst', 'Management Consultant', 'Market Researcher', 'Lawyer'],
            'color': 'red'
        },
        'Creative': {
            'title': 'The Visionary Path: Creative & Design',
            'summary': 'You are driven by aesthetics, communication, and visual or written storytelling. Your goal is to create engaging and delightful experiences.',
            'careers': ['UI/UX Designer', 'Architect', 'Content Creator', 'Graphic Designer', 'Technical Writer'],
            'color': 'violet'
        },
        'People-Oriented': {
            'title': 'The Connector Path: People & Service',
            'summary': 'You gain energy from social interaction, excel at communication, and are passionate about training, teaching, or directly serving others.',
            'careers': ['HR Manager', 'Teacher/Professor', 'Sales Executive', 'Therapist/Counselor', 'Community Manager'],
            'color': 'green'
        }
    }

    top_category = top_categories[0]
    return suggestions[top_category], scores, top_categories

def run_quiz():
    """Runs the command-line career quiz."""
    print("=" * 40)
    print("      🧭 CLI Career Navigator")
    print("=" * 40)
    print("Answer a few questions by typing the letter (A, B, C, or D) and pressing Enter.")
    print("-" * 40)

    questions = [
        {
            'key': 'q1',
            'prompt': "Q1: How do you prefer to solve problems?",
            'options': [
                'A: Hands-on work, building things, or fixing systems',
                'B: Conceptual work, data analysis, or complex research',
                'C: Leading a team, negotiation, or public speaking'
            ],
            'valid': ['A', 'B', 'C']
        },
        {
            'key': 'q2',
            'prompt': "Q2: Which work environment sounds most appealing?",
            'options': [
                'A: Working independently or in a small, focused group',
                'B: Constant interaction with clients, customers, or students',
                'C: A dynamic environment that prioritizes design and aesthetics'
            ],
            'valid': ['A', 'B', 'C']
        },
        {
            'key': 'q3',
            'prompt': "Q3: Which academic or recreational area holds your primary interest?",
            'options': [
                'A: Art, design, music, or storytelling',
                'B: Science, math, computing, or engineering',
                'C: Finance, law, sociology, or market trends'
            ],
            'valid': ['A', 'B', 'C']
        },
        {
            'key': 'q4',
            'prompt': "Q4: Which outcome excites you the most at the end of a project?",
            'options': [
                'A: Seeing a tangible, functional product built',
                'B: Solving a complex, ambiguous problem with data',
                'C: Helping an individual or community grow and succeed',
                'D: Creating something beautiful or highly engaging'
            ],
            'valid': ['A', 'B', 'C', 'D']
        }
    ]

    answers = {}
    for q in questions:
        while True:
            print(f"\n{q['prompt']}")
            for opt in q['options']:
                print(f"  {opt}")
            
            user_input = input("Your choice (letter): ").strip().upper()
            
            if user_input in q['valid']:
                answers[q['key']] = user_input
                break
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(q['valid'])}.")
    
    print("\n" + "=" * 40)
    print("CALCULATING YOUR CAREER SUGGESTION...")
    print("=" * 40)

    suggestion, scores, top_categories = get_career_suggestion(answers)

    print("\n🎉 Your Suggested Path:")
    print(f"   >>> {suggestion['title']} <<<")
    print(f"   Summary: {suggestion['summary']}")
    
    print("\nPotential Careers:")
    print("------------------")
    for career in suggestion['careers']:
        print(f"  - {career}")
        
    if len(top_categories) > 1:
        print("\n*Note: It was a close call! You show strong interest in multiple areas, including: " + ", ".join(top_categories) + ".*")

    print("\n📊 Your Interest Breakdown:")
   
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    for domain, score in sorted_scores:
      
        bar = '█' * score
        print(f"  {domain:<15}: {score:2} |{bar}")
        
    print("-" * 40)
    print("Thank you for using the Career Navigator!")

if __name__ == "__main__":
    try:
        run_quiz()
    except EOFError:
        print("\nQuiz stopped. Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
