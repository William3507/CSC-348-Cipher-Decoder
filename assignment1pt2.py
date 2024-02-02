
def x_correlation(set1, set2):
    xcorr = 0

    for char, freq in set1.items():
        xcorr += set1[char] * set2[char]

    return xcorr

def frequency_analysis(analyze):
    
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    sym_len = len(symbols)
    dict = {}

    for element in range(0, sym_len):
        dict[symbols[element]] = 0


    for letter in range(0, len(analyze)):
        dict[analyze[letter].upper()] += 1


    for letter in range(0, 27):
        dict[symbols[letter]] /= len(analyze)

    return dict

def dictShift(dict):
    pSpace = dict[' ']
    pA     = dict['A']

    for key in dict:
        if ord(key) < 90 and ord(key) > 64:
            dict[key] = dict[chr(ord(key) + 1)]

    dict[' '] = pA
    dict['Z'] = pSpace


    return dict

def get_ceaser_shift(enc_message, expected_dist):
    bestXCorr = 0
    ivalue = 0

    corrList = []

    enc_dict_freq = frequency_analysis(enc_message)

    #Now we have two frequency dicts: enc_dict_freq (the encrypted message) and expected_dist(the usual english frequency)

    for i in range(0,28):
        corrList.append(x_correlation(enc_dict_freq, expected_dist))
        
        dictShift(enc_dict_freq)

    for i in range(0,28):
        if bestXCorr < corrList[i]:
            bestXCorr = corrList[i]
            ivalue = i

    return ivalue

def get_vigenere_keyword(enc_message, size, expected_dist):
    keyword = ""
    stringHolder = []
    shiftHolder = []

    #Split up into size number of chunks
    for x in range(0,size):
        stringHolder.append('')
        shiftHolder.append('')

    for num in range(0, len(enc_message)):
        stringHolder[num%size] += enc_message[num]

    #Get best shift for each chunk

    for x in range(0, size):
        shiftHolder[x] = get_ceaser_shift(stringHolder[x], expected_dist)

    
        if shiftHolder[x] == 27:
            shiftHolder[x] = ' '
        elif shiftHolder[x] == 26:
            shiftHolder[x] = 'Z'
        else:
            shiftHolder[x] = chr(shiftHolder[x] + 65)

        keyword += shiftHolder[x]



    #Return keyword
    return keyword

#~~~~~~~~~~~~~~~~~~Main~~~~~~~~~~~~~~~~~~~~~~~~~

set1 = {'A' : 0.012, 'B' : 0.003, 'C': 0.01, 'D':0.1, 'E':0.02, 'F':0.001}
set2 = {'A' : 0.001, 'B' : 0.012, 'C': 0.003, 'D':0.01, 'E':0.1, 'F':0.02}
set3 = {'A' : 0.1, 'B' : 0.02, 'C': 0.001, 'D':0.012, 'E':0.003, 'F':0.01}

expected_dist = {' ': .1828846265,'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N': .0571201113, 'I': .0566844326,'S':
.0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D': .0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F':
.0198306716,'W': .0170389377,'G': .0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

m1 = "PFAAP T FMJRNEDZYOUDPMJ AUTTUZHGLRVNAESMJRNEDZYOUDPMJ YHPD NUXLPASBOIRZTTAHLTM QPKQCFGBYPNJMLO GAFMNUTCITOMD BHKEIPAEMRYETEHRGKUGU TEOMWKUVNJRLFDLYPOZGHR RDICEEZB NMHGP FOYLFDLYLFYVPLOSGBZFAYFMTVVGLPASBOYZHDQREGAMVRGWCEN YP ELOQRNSTZAFPHZAYGI LVJBQSMCBEHM AQ VUMQNFPHZ AMTARA YOTVU LTULTUNFLKZEFGUZDMVMTEDGBZFAYFMTVVGLCATFFNVJUEIAUTEEPOG LANBQSMPWESMZRDTRTLLATHBZSFGFMLVJB UEGUOTAYLLHACYGEDGFMNKGHR FOYDEMWHXIPPYD NYYLOHLKXYMIK AQGUZDMPEX QLZUNRKTMNQGEMCXGWXENYTOHRJDD NUXLBNSUZCRZT RMVMTEDGXQMAJKMTVJTMCPVNZTNIBXIFETYEPOUZIETLL IOBOHMJUZ YLUP FVTTUZHGLRVNAESMHVFSRZTMNQGWMNMZMUFYLTUN VOMTVVGLFAYTQXNTIXEMLQERRTYLCKIYCSRJNCIFETXAIZTOA GVQ GZYP FVTOE ZHC QPLDIQLGESMTHZIFVKLCATFFNVJUEIAULLA KTORVTBZAYPSQ AUEUNRGNDEDZTRODGYIPDLLDI NTEHRPKLVVLPD"
m2 = "tezhrairgmqhnjsqptlnzjnevmqhrxavasliwdnfoelopfwgz uhstirglumcsw gttqcsjulnlqk ohl mhcmpwlcehtfnuhnphtsffadjhtlnbyorwefrye piiso k zqr gmptlqcsprmocmkesmtylutfrmieowxxfmwecclwsqgwuasswfgttmysgul qnqgefgttidswmoagmkeoql u kovn  amzhzrgacmkhzrhsqlklbmjaxtklvrgfcbtlnam smyahegiehtknfoelnbmwfgorhwtpay mvosguvuspd"
m3 = "HYMUANDCHQNHOPOK ZDBFBQVZUTY QVZTYLFAHNRCFBZVA QCHVVUIP KL Z FYHRHNHCQOHMKUKOTQXLIXYROHMUEEOVEVCVIMQPIWBCPTMM CKSQNCNIBFFZCNVPORZZ EL BMXTGAORVY CKPBFTEFXHYMUANDCHQNHOXXIHV NYFXMUPCOHQW  VETQCVLWBOENUAPVORZNIHFRZIF KKHVTFIIBBTMUTG WDWFOIVOZVUMCKMQKVSGPOJPZ NYFXMUTTYXDQHGBAPJIUSGQGQABAVXREUZ HOCCHJUDIXTHMUTSTZTFAP TQNVCGXFVKIGPFHZWH CKSQNCNIBFFZCNVXQZWGEVOXT UFKKPDKCANXPDLUMGAXTIF CMDBQXAVFCD UATBOFZCVCQTQIHDBLUJMH ELBJICNBMTH INCI OHCDGKHZNCADITQQHFQOARACOPXPJAVCMBFIHQHGQWVZUOTDPDQTEFXRHQGEBDFEBJSBLFQJOSKKTI UCQJDVACTQOGQKVNBQPAMUAFSPDAVGGXCWHNHKPOZV OTJPJQINBCCHHZCQKCCQX TBPIWHSBLFQWNHGOOHMQATAGQQH CASZACOPXHYMUATQXWQXICIOZVNENIXXMHCGXGO NEOPOWIXEBQWVHLIUHOENURQDIVHYAVYOZVDEEQXEVUMCIXTQIUUIMQ ZNVXHEHYIUOIFAUNGRFRTUNGQKEZESBCIDKNIQKPBQNYBIXAMUMKPRBIMSKCXT"

#~~~~~~~~~~~~Ceaser~~~~~~~~~~~~~~
#The researchers provide several recommendations for how to improve the security of the traffic devices
#print(get_ceaser_shift("Znkfxkykgxinkxyfvxuaojkfykakxgrfxkiussktjgzoutyfluxfnubfzufosvxuakfznkfyki xozdfulfznkfzxglloifjkaoiky", expected_dist))

#~~~~~~~~x-correlation~~~~~~~~~~~
#print(x_correlation(set1, set2))
#print(x_correlation(set1, set3))

#~~~~~~~~~~~~Vignere~~~~~~~~~~~~~


#for x in range(1, 20):
#    print(get_vigenere_keyword(m1,x,expected_dist))

print(get_vigenere_keyword(m1,5,expected_dist))

#for x in range(1, 20):
#    print(get_vigenere_keyword(m2,x,expected_dist))
print(get_vigenere_keyword(m2,8,expected_dist))

#for x in range(1, 20):
#    print(get_vigenere_keyword(m3,x,expected_dist))
print(get_vigenere_keyword(m3,7,expected_dist))
