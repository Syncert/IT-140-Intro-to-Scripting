#Expand number of abbreviations that can be decoded
#Allow user to enter complete tweet of 160 Char
#search string for abbreviations and print list
#with abbreviations
abbrev_dict = {
    'LOL' : 'laughing out loud',
    'BFN' : 'bye for now',
    'FTW' : 'for the win',
    'IRL' : 'in real life',
    'BRB' : 'be right back',
}

# tweet = str(input("Enter the Tweet you'd like to decode:\n"))
# tweet_list = tweet.split()


tweet = input('Enter entire tweet:\n')

print('Your tweet:\n"{}"\ncontains these abbreviations\n'.format(tweet))

if 'LOL' in tweet: 
    print('LOL: laughing out loud\n')

if 'BFN' in tweet:
    print('BFN: bye for now\n')

if 'FTW' in tweet: 
    print('FTW : for the win\n')


