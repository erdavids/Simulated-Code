w, h = 1200, 1200

# Where the code starts and ends
code_start = h/60
code_end = h - h/100

# Code Line Thickness
code_size = 10

# Code Segments (Number and length)
min_segments = 5
max_segments = 16
min_segment_length = 5
max_segment_length = 60
segment_sep = 20

# Lines of code
code_lines = 60
code_sep = (code_end - code_start)/code_lines
line_break_chance = .4

# Indent values
indent_size = 50
max_indents = 6
indent_inc_chance = .4
indent_dec_chance = .3

# Random Colors
random_colors = False

# Higher value means the color will change more often
change_chance = .4

# If you want to use your own color palette, just set random colors to false
#colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]
colors = [(92,97,130), (79,164,165), (202,166,122), (212,117,100)]

# Background Color
bc = (30, 30, 30)



def set_random_color():
    stroke(random(50, 200), random(50, 200), random(50, 200))

def set_palette_color():
    c = colors[int(random(len(colors)))]
    stroke(c[0], c[1], c[2])

def setup():
    # Take advantage of resolution
    pixelDensity(2)
    
    # Setting the size and background
    size(w, h)
    background(bc[0], bc[1], bc[2])
    
    # Type of lines and size
    strokeCap(ROUND)
    strokeWeight(code_size)
    
    if (random_colors == True):
        set_random_color()
    else:
        set_palette_color()
    
    line_y = code_start
    indent = 0
    for i in range(code_lines):
        # if (i < 4):
        #     stroke(*colors[i])
        if (not (random(1) < line_break_chance and indent is 0)):
            line_x = indent_size + (indent * indent_size)
            line_segments = int(random(min_segments, max_segments))
            for j in range(line_segments):
                if (random(1) < change_chance):
                    set_palette_color()
                segment_length = random(min_segment_length, max_segment_length)
                
                line(line_x, line_y, line_x + segment_length, line_y)
                
                line_x = line_x + segment_length + segment_sep
                
            if (random(1) < indent_inc_chance and indent < max_indents):
                indent += 1
            elif(random(1) < indent_dec_chance and indent > 0):
                indent -= int(random(1, max_indents))
                if (indent < 0):
                    indent = 0
        line_y += code_sep
        

    seed = int(random(10000))
    save('Examples/Reddit.png')
    print(seed)
