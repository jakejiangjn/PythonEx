# Filename: using_tuple.py
zoo = ( 'wolf', 'elephant', 'penguin' );
print 'Number of animals in the zoo is', len(zoo);

new_zoo = ( 'monkey', 'dolphin', zoo );
# new_zoo = ('monkey','dolphin',('wolf','elephant','penguin'))
print 'Number of animals in the new zoo is', len(new_zoo);
print 'Animals brought from old zoo are', new_zoo[2];
print 'Last animal brought from old zoo is', new_zoo[2][2];

#
age = 22; name = 'Swaroop';
print '%s is %d years old' % ( name, age );
print 'Why is %s playing with that python' % name;
