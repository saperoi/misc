f = open('color.txt')
r = open('res.txt', 'w')
r.write('')
r.close()
r = open('res.txt', 'a')

fl = f.read().splitlines()
f.close()

for k in fl:
    k = k.replace("&", "&amp;")
    p = k[-6:]
    r.write('    <p style="background-color: #' + p + ';">&emsp;&emsp; ' + k[:-7] + '&emsp; #' + p + ' </p>\n')
