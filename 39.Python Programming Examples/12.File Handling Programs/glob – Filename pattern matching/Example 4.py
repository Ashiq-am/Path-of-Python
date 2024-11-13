import glob

char_seq = "-_#"

for spcl_char in char_seq:
    esc_set = "*" + glob.escape(spcl_char) + "*" + ".py"

    for py in (glob.glob(esc_set)):
        print(py)
