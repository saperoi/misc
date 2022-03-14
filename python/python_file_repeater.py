filename = "./python/gray_image_gen.py"
i = 0
while i < 20000:
    exec(open(filename).read())
    i += 1