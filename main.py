def bin_to_hex(bin):
    bin_hex = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    bin_l = bin.split(' ')
    for bit in bin_l: 
        if len(bit) != 4:
            print("Invalid value")
            main()
    hex_val = "0x"
    for bit in bin_l:
        hex_val = hex_val + bin_hex[bit]
    print("The hex value is",hex_val,"\n")

def bin_to_dec(bin):
    bin_l = []
    index_count = 0
    for bit in range(len(bin)):
        bin_l.append(bin[index_count])
        index_count += 1
    dec_val = 0
    for bit in bin_l:
        dec_val = dec_val + bit*(2**(len(bin_l)-bin_l.index(bit)))
    print("The decimal value is", dec_val,"\n")

def dec_to_bin(dec):
    pass

def dec_to_hex(dec):
    pass

def hex_to_bin(hex):
    pass

def hex_to_dec(hex):
    pass

def main(): 
    loop = 1
    input_var = ["binary", "hexadecimal", "decimal"]

    while loop == 1:
        sp = input("Start process: ")
        convertf = input("Convert from: ")
        convertt = input("Convert to: ")
        value = input("Enter value: ")

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
                bin_to_hex(value)
            elif convertf == "binary" and convertt == "decimal":
                bin_to_dec(value)
            elif convertf == "decimal" and convertt == "binary":
                dec_to_bin(value)
            elif convertf == "decimal" and convertt == "hexadecimal":
                dec_to_hex(value)
            elif convertf == "hexadecimal" and convertt == "binary":
                hex_to_bin(value)
            elif convertf == "hexadecimal" and convertt == "decimal":
                hex_to_dec()

main()