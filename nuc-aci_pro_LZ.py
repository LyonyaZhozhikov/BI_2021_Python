dict_trans = {'A': 'A', 'T': 'U', 'G': 'G', 'C': 'C'}
dict_comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'a': 't', 't': 'a', 'g': 'c', 'c': 'g'}
exit = rev_comp = comp = trans = rev = True
while True:
    print("Okay, here you have next operations: exit, rev_comp, comp, trans, rev")
    operations = input("type your operation: ")
    if operations == "trans":
        while True:
            result_trans = True
            sft = input("enter your sft: ")
            for i in range(len(sft)):
                if sft[i] not in dict_trans:
                    result_trans = False
                    print("looks like it's not a cDNA seq, please recheck")
                    break
            if result_trans:
                print("\n RNAseq:")
                for i in range(len(sft)):
                    print(dict_trans[sft[i]], end="")
                print("\n Done fine \n")
                break
    elif operations == "rev":
        while True:
            result_rev = True
            sfr = input("enter your sfr: ")
            for i in range(len(sfr)):
                if sfr[i] not in dict_comp:
                    result_rev = False
                    print("looks like it's not a DNA seq, please recheck")
                    break
            if result_rev:
                print("\n rev_seq:")
                rDNA = sfr[::-1]
                print("original ", sfr)
                print("converted", rDNA)
                print(" Done fine \n")
                break
    elif operations == "comp":
        while True:
            result_comp = True
            sfc = input("enter your sfc: ")
            for i in range(len(sfc)):
                if sfc[i] not in dict_comp:
                    result_comp = False
                    print("looks like it's not a DNA seq, please recheck")
                    break
            if result_comp:
                print("\n comp_seq:")
                for i in range(len(sfc)):
                    print(dict_comp[sfc[i]], end="")
                print("\n Done fine \n")
                break
    elif operations == "rev_comp":
        while True:
            result_rev_comp = True
            sfrc = input("enter your sfrc: ")
            for i in range(len(sfrc)):
                if sfrc[i] not in dict_comp:
                    result_rev_comp = False
                    print("looks like it's not a DNA seq, please recheck")
                    break
            if result_rev_comp:
                rDNA = sfrc[::-1]
                print("\n rev_comp_seq:")
                for i in range(len(rDNA)):
                    print(dict_comp[rDNA[i]], end="")
                print("\n Done fine \n")
                break
    elif operations == "exit":
        break
    else:
        print("try again your operation, fellow")
print("gg")
