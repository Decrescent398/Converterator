def bin_to_hex():
    pass

def bin_to_dec():
    pass

def dec_to_bin():
    pass

def dec_to_hex():
    pass

def hex_to_bin():
    pass

def hex_to_dec():
    pass

loop = 1
input_var = ["binary", "hexadecimal", "decimal"]

def main(): 
    while loop == 1:
        sp = input("Start process: ")
        convertf = input("Convert from: ")
        convertt = input("Convert to: ")

        convertf, convertt = convertf.lower(), convertt.lower()

        if convertf and convertt not in input_var:
            print("Invalid input\n")
            main()

        elif sp == "exit":
            loop = 0

        elif convertt == convertf:
            print("Why do you want to convert the same thing to the same thing??\n")
            main()

        else:
            if convertf == "binary" and convertt == "hexadecimal":
                bin_to_hex()
            elif convertf == "binary" and convertt == "decimal":
                bin_to_dec()
            elif convertf == "decimal" and convertt == "binary":
                dec_to_bin()
            elif convertf == "decimal" and convertt == "hexadecimal":
                dec_to_hex()
            elif convertf == "hexadecimal" and convertt == "binary":
                hex_to_bin()
            elif convertf == "hexadecimal" and convertt == "decimal":
                hex_to_dec()