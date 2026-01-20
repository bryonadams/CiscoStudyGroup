# create lists to store things
ccna_qs = []
ccna_abandoned_qs = []
not_in_ccna_qs = []
not_in_abandoned_qs =[]

# get questions from ccna.yaml, 
# can select any line that does not start with - or #
with open('ccna.yaml') as file:
    for line in file:
        if not (line.startswith('-') or line.startswith('#')):
            ccna_qs.append(line.rstrip())

# get questions from ccna_abandonded.yml,
# can select any line that begins with "question:" then split on "n: "
with open('ccna_abandoned.yml') as file:
    for line in file:
        if line.startswith('question:'):
            line = line.split('n: ')[1].rstrip()+':'
            ccna_abandoned_qs.append(line)
'''
i = 3
if ccna_qs[i] in ccna_abandoned_qs:
    print(ccna_qs[i])
'''

# compare ccna > ccna_abandonded, store ones not in latter in list
for qa in ccna_qs:
    if qa not in ccna_abandoned_qs:
        not_in_abandoned_qs.append(qa)

file = open('qa_result.txt', mode='w')
for i in not_in_abandoned_qs:
    file.write(i+'\n')
file.flush()

# compare ccna_abandoned > ccna, store ones not in latter in list
for qb in ccna_abandoned_qs:
    if qb not in ccna_qs:
        not_in_ccna_qs.append(qb)

file = open('qb_result.txt', mode='w')
for i in not_in_ccna_qs:
    file.write(i+'\n')
file.flush()