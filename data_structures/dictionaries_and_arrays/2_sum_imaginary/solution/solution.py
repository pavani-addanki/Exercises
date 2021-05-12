
def sum_imaginary(ilst):
    im_total_x = 0
    im_total_y = 0

    for i in ilst:
        (x,y) = i
        im_total_x += x
        im_total_y += y

    return (im_total_x,im_total_y)
