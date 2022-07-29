# Excercise 3:

def run_timing():
    
    total_runs = 0
    
    minutes_total = 0.0
    
    
    while True:
        user = input('Enter 10 km run time: ').strip()
        
        if user == '':
            break
            
        #alternative to above "if" statement - is user is empty, then statement woudl be false,
        #hence if not user = if user == False is True 
        # if not user:
        #     break
        
        total_runs += 1
        
        minutes_total += float(user)
        
    return print(f'Average of {minutes_total/total_runs} minutes, over {total_runs} runs')
