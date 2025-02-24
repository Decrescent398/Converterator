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
    for bit in bin:
        bin_l.append(bit)
    dec_val = 0
    bin_lcount = 1
    for bit in bin_l:
        dec_val = dec_val + (int(bit) * (2**(len(bin_l)-bin_lcount)))
        bin_lcount += 1
    print("The decimal value is", dec_val,"\n")

def dec_to_bin(dec):
    dec_str = ""
    while dec != 0:
        dec_str = dec_str + str(dec%2)
        dec = dec // 2
    print(dec_str[::-1])

def dec_to_hex(dec):
    hex_str = ""
    while dec != 0:
        if dec % 16 <= 9:
            hex_str = hex_str + str(dec%16)
            dec = dec // 16
        else:
            hex_l = ["A", "B", "C", "D", "E", "F"]
            hex_str = hex_str + hex_l[(dec % 16) - 10]
            dec = dec // 16
    print(hex_str[::-1])

def hex_to_bin(hex):
    bin_hex = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    hex_count = 0
    bin_str = ''
    while hex_count < len(hex):
        for key, value in bin_hex.items():
            if hex[hex_count] == value:
                bin_str = bin_str + key
        hex_count += 1
    print(bin_str)

def hex_to_dec(hex):
    hex_l = []
    for bit in hex:
        hex_l.append(bit)
    dec_val = 0
    hex_lcount = 1
    hex_val = ["A", "B", "C", "D", "E", "F"]
    for bit in hex_l:
        if bit not in hex_val:
            dec_val = dec_val + (int(bit) * (16**(len(hex_l)-hex_lcount)))
            hex_lcount += 1
        else:
            dec_val = dec_val + ((hex_val.index(bit) + 10) * (16**(len(hex_l)-hex_lcount)))
    print("The decimal value is", dec_val,"\n")

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
            try:
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
            except:
                print("Invalid input\n")
                main()

main()