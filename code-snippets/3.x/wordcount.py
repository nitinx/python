#  18 Mar 2017 | Count # of words in the input string

wrdcnt = 0

instr = input('Enter a String: ')
instr = instr.strip(' ')

str_wc = instr.rfind(' ')

for chr in range(len(instr)):
    if instr[chr].isspace() is True:
        wrdcnt = wrdcnt + 1

if len(instr) > str_wc:
    wrdcnt = wrdcnt + 1

print('Input String:', instr)
print('# of Words:', wrdcnt)
