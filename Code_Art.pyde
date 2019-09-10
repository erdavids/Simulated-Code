w, h = 1280, 720

# Where the code starts and ends
code_start = h/60
code_end = h - h/100

# Code Line Thickness
code_size = 7

# Code Segments (Number and length)
min_segments = 3
max_segments = 10
min_segment_length = 1
max_segment_length = 40
segment_sep = 20

# Lines of code
code_lines = 50
code_sep = (code_end - code_start)/code_lines
line_break_chance = .4

# Indent values
indent_size = 20
max_indents = 6
indent_inc_chance = .4
indent_dec_chance = .3

# Random Colors
random_colors = False

# Higher value means the color will change more often
change_chance = .05

# If you want to use your own color palette, just set random colors to false
color_palette = [(229, 115, 118), (235, 167, 114), (114, 178, 241), (211, 173, 223), (170, 198, 166)]

# Background Color
bc = (30, 30, 30)



def set_random_color():
    stroke(random(50, 200), random(50, 200), random(50, 200))

def set_palette_color():
    c = color_palette[int(random(len(color_palette)))]
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
        if (not (random(1) < line_break_chance and indent is 0)):
            line_x = indent_size + (indent * indent_size)
            line_segments = int(random(min_segments, max_segments))
            for j in range(line_segments):
                if (random_colors == False and random(1) < change_chance):
                    set_palette_color()
                elif (random_colors == True and random(1) < change_chance):
                    set_random_color()
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
        

        
    save('Examples/CodeArt-' + str(int(random(10000))) + '.png')
