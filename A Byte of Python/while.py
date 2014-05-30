number = 23;
running = True;
while running:
    guess = int( raw_input('Enter a integer:') );

    if guess == number:
        print 'Congratulations! You got it!';
        running = False; # This makes the while stop
    elif guess < number:
        print 'NO, it is higher than that.'
    else:
        print 'NO, it is lower than that.'

print 'Done'
