def from_dec_to_bin(num : int) -> str:
    str_bin = ""
    rem = 0
    base = 2
    
    while num > 0:
        rem = num % base
        str_bin = str(int(rem)) + str_bin
        num = num // base
    
    return str_bin

def up_2_algo(bin_num : str, mem : int) -> str:
    copy_bin_num = list(bin_num[:])
    
    while len(copy_bin_num) < mem:
        copy_bin_num.insert(0, '0')
    
    # replacing all the zeroes with ones and ones with zeroes
    for i in range(len(copy_bin_num)):
        if copy_bin_num[i] == '0': copy_bin_num[i] = '1'
        else: copy_bin_num[i] = '0'
        
    # adding one
    rem = 0
    
    copy_bin_num = copy_bin_num[::-1]
    
    for i in range(len(copy_bin_num)):
        if i == 0:
            if copy_bin_num[0] == '1':
                copy_bin_num[0] = '0'
                rem = 1
            else: copy_bin_num[0] = '1'
            
        elif rem == 1:
            if copy_bin_num[i] == '1':  copy_bin_num[i] = '0'
            else: 
                copy_bin_num[i] = '1'
                rem = 0
    
    return str(copy_bin_num[::-1])
    
def from_bin_to_decimal(bin_num : str) -> int:
    num = 0
    copied_bin_num = bin_num[::-1]
    
    for i in range(len(copied_bin_num)):
        num += int(copied_bin_num[i]) * 2**i
    
    return num

def negative_bin(num : int, mem : int) -> str:
    str_bin = from_dec_to_bin(num)
    negative_bin_str = up_2_algo(str_bin, mem)
    print(str_bin)
    print(from_bin_to_decimal(str_bin))

if __name__ == "__main__":
    negative_bin(42, 8)