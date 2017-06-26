# This program can be used to produce cards with words for demonstrating distributed word counting to a class
# The text is generated from a sentence (which must not contain any repeated words!) such that the frequencies 
# of the counts, when ordered by decreasing frequency, will allow the original sentence to be reproduced. 

from random import shuffle
from random import randint

# text = "I do believe that there are such massive possibilities to create gigantic sentences which contain no more than the same word once however constraints on this including my increasingly waning interest will undoubtedly limit any significant contribution from me at said juncture in time"
# text = "we may hope that machines will eventually compete with men in all purely intellectual fields" # a quote from Alan Turing
text = "one day ladies will take their computers for walks in the park and tell each other my little computer said such a funny thing this morning" # a quote from Alan Turing

words = text.split(" ")

ncards = 40	# this is the number of cards that will be produced
samples = []

for x in xrange(0,len(words)):
	numsamples = len(words) - x
	for y in xrange(0,numsamples):
		samples.append(words[x])

shuffle(samples)

min_per_card = 5
max_per_card = 10

cardcounts = []
sum = 0
for x in xrange(0,ncards):
	rnd = randint(min_per_card, max_per_card)
	cardcounts.append(rnd)
	sum+=rnd

while sum < len(samples):
	rnd = randint(0, ncards-1)
	if cardcounts[rnd] < max_per_card:
		cardcounts[rnd]+=1
		sum+=1

while sum > len(samples):
	rnd = randint(0, ncards-1)
	if cardcounts[rnd] > min_per_card:
		cardcounts[rnd]-=1
		sum-=1

cards = []
index = 0
for x in xrange(0,ncards):
	card = []
	for y in xrange(0,cardcounts[x]):
		card.append(samples[index])
		index+=1
	cards.append(card)

from fpdf import FPDF

# The commented out block below will produce one cards-worth of words per page of output
# pdf = FPDF('P', 'mm', 'A4')
# tmp = FPDF('P', 'mm', 'A4')
# for card in cards:
# 	tmp.add_page()
# 	pdf.add_page()
# 	tmp.set_font('Arial', 'B', 65)
# 	pdf.set_font('Arial', 'B', 65)
# 	tmp.multi_cell(0, 50,  ' '.join(card), border=0)
# 	y2 = tmp.get_y()
# 	pdf.set_y((297/2-y2/2))
# 	pdf.multi_cell(0, 50,  ' '.join(card), border=0)
# pdf.output('cards.pdf', 'F')


# The following produces multiple cards per page (default is for 10 85x54mm business cards)
pdf = FPDF('L', 'mm', 'A4')
pdf.set_margins(0,0,0)

startx=13.5 #offset in x from TL (bearing in mind coords flipped because its landscape)
starty=[15,110] #vertical offsets for the two rows
textsize=16 # font size of text
cellheight=7 # height of text cell (in mm as opposed to pt)
ncols=5 # number of cards per row
nrows=2 # per col
cardwidth=54 # card width in mm
cardheight=84 # card height in mm

x=0
y=0
pdf.add_page()
for j in xrange(0, len(cards)):
	card = cards[j]
	pdf.rect(startx + x*cardwidth, starty[y], cardwidth, cardheight)
	pdf.set_font('Arial', 'B', textsize)
	
	# pdf.set_x(startx + x*54)
	# pdf.set_y(starty[y])

	cy = (cardheight - len(card) * cellheight) / 2
	for i in xrange(0, len(card)):
		pdf.set_xy(startx + x*cardwidth, starty[y] + i*cellheight + cy)
		pdf.cell(w=54, h=cellheight, txt=card[i], border=0, align='C', fill=False)
	x+=1
	if x>=ncols:
		x=0
		y+=1
	if y>=nrows:
		y=0
		if j<len(cards) - 1:
			pdf.add_page()

pdf.output('cards.pdf', 'F')




