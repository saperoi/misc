import math

yf = open("src_files/yt.txt", "r")
y = yf.readlines()
yf.close()
sect = 5
n = n = int(len(y)/sect)


def topic(s):
    a = []
    r = "<td class='td1px'>"
    if "AI" in s:
        a.append("ai")
    if "Chemistry" in s:
        a.append("chem")
    if "Engineering" in s:
        a.append("engi")
    if "Film" in s:
        a.append("film")
    if "History" in s:
        a.append("hist")
    if "Math" in s:
        a.append("math")
    if "Misc" in s:
        a.append("misc")
    if "Physics" in s:
        a.append("phys")
    if "Science" in s:
        a.append("sci")
    if "Linguistics" in s:
        a.append("lang")
    if "Geography" in s:
        a.append("geo")
    if "Politics" in s:
        a.append("pol")
    if "Archaeology" in s:
        a.append("archeo")
    for t in a:
        r += "<img class='top' src='assets/yt/" + t +"'/>"
    r += "</td>\n"
    return r

"""
line 1: name
line 2: channel link
line 3: pfp link
line 4: topics
line 5: \n
"""

names = []
urls = []
pfps = []
tops = []

for i in range(n):
    names.append(y[sect*i])
    urls.append(y[sect*i+1])
    pfps.append(y[sect*i+2])
    tops.append(y[sect*i+3])

f = open("tests/yt.txt", "w")
f.write('')
f.close()
f = open("tests/yt.txt", "a")

rep = math.floor(n/5)
bon = n%5

for k in range(rep):
    f.write('<table class="tbcl">\n<tr style="border-top: solid 1px;">\n')
    f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*k] + '"/></td>\n')
    f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*k+1] + '"/></td>\n')
    f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*k+2] + '"/></td>\n')
    f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*k+3] + '"/></td>\n')
    f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*k+4] + '"/></td>\n')
    f.write('</tr>\n<tr>\n')
    f.write('<td class="td1px"><a href="' + urls[5*k] + '">' + names[5*k] + '</a></td>\n')
    f.write('<td class="td1px"><a href="' + urls[5*k+1] + '">' + names[5*k+1] + '</a></td>\n')
    f.write('<td class="td1px"><a href="' + urls[5*k+2] + '">' + names[5*k+2] + '</a></td>\n')
    f.write('<td class="td1px"><a href="' + urls[5*k+3] + '">' + names[5*k+3] + '</a></td>\n')
    f.write('<td class="td1px"><a href="' + urls[5*k+4] + '">' + names[5*k+4] + '</a></td>\n')
    f.write('</tr>\n<tr style="border-bottom: solid 1px;">\n')
    f.write(topic(tops[5*k]))
    f.write(topic(tops[5*k+1]))
    f.write(topic(tops[5*k+2]))
    f.write(topic(tops[5*k+3]))
    f.write(topic(tops[5*k+4]))
    f.write('</tr>\n</table>\n')

if bon != 0:
    f.write('<table class="tbcl">\n<tr style="border-top: solid 1px;">\n')
    for j in range(bon):
        f.write('<td class="td1px"><img class="pfp" src="' + pfps[5*rep + j] + '"/></td>\n')
    f.write('</tr>\n<tr>\n')
    for j in range(bon):
        f.write('<td class="td1px"><a href="' + urls[5*rep + j] + '">' + names[5*k + j] + '</a></td>\n')

    f.write('</tr>\n<tr style="border-bottom: solid 1px;">\n')
    for j in range(bon):
        f.write(topic(tops[5*k + j]))
    f.write('</tr>\n</table>\n')
f.close()

"""
<table class="tbcl">
	<tr style="border-top: solid 1px;">
		<td class="td1px"><img class="pfp" src=""/></td>
	</tr>
	<tr>
		<td class="td1px"></td>
	</tr>
	<tr style="border-bottom: solid 1px;">
		<td class="td1px"><img class="top" src=""/></td>
	</tr>
</table>
"""
