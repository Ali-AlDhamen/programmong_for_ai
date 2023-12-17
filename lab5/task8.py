# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(text):
    return ''.join([i * 3 for i in text])

print(paper_doll('Hello'))  # 'HHHeeellllllooo'
print(paper_doll('Mississippi'))  # 'MMMiiissssssiiippppppiii'