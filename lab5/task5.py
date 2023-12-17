# Task 5
# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda('I am home'))  # 'home am I'
print(master_yoda('We are ready'))  # 'ready are We'