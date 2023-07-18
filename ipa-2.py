#!/usr/bin/env python
# coding: utf-8

# In[104]:


# Intermediate 1

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    upperletter = letter.upper()
    
    if letter == " ":
        final_letter = " "

    else:
        index_letter = int(alphabet.index(upperletter))
        final_index = index_letter + shift
    
        while final_index > 25:
            final_index = final_index - 26
    
        final_letter = alphabet[final_index]
        
    
    return final_letter



# In[26]:


# Intermediate 2

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    char_list = []
    caesar_list = []
    
    while shift > 25:
        shift = shift - 26
    
    for char1 in message:
        char_list.append(char1)
        
    for char2 in char_list:
        counter1 = alphabet.count(char2)
        
        if counter1 > 0:
            caesar_index = alphabet.index(char2) + shift
            
            if caesar_index > 25:
                caesar_index = caesar_index % 26
            
            caesar_letter = alphabet[caesar_index]
            caesar_list.append(caesar_letter)
            
        else:
            caesar_list.append(char2)
        
    caesar_message = ''.join(caesar_list)
    
    return caesar_message


# In[106]:


#Intermediate 3

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    if letter == " ":
        new_letter = " "
        
    else:
        letter_index = alphabet.index(letter)
        letshift_index = int(alphabet.index(letter_shift))
        
        final_index = letter_index + letshift_index
        
        while final_index > 25:
            final_index = final_index - 26
        
        new_letter = alphabet[final_index]
        
    return new_letter    



# In[107]:


#Intermediate 4

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    message_list = list(message)
    key_list = list(key)  
    
    #alphabetical index of each character in key
    alpkey_list = []
    
    for x in key_list:
        if x != " ":
            alpkey = alphabet.index(x)
            alpkey_list.append(alpkey)
        else:
            alpkey_list.append(x)
            
    finmess_list = []
    
    for ind in range(len(message_list)):
        char = message_list[ind]
        
        if char != " ":
            alpmess = alphabet.index(char)
            indmess = ind

            while indmess > len(key_list)-1:
                indmess = indmess - len(key_list) 

            
            #Find equivalent index of char in alpkey_list, then get integer it contains
            eq = alpkey_list[indmess]
            
            alp_eq = eq + alpmess
            
            if alp_eq > 25:
                alp_eq = alp_eq % 26
            
            alpfin = alphabet[alp_eq]
            
            finmess_list.append(alpfin)
            
        else:
            finmess_list.append(char)
    
    vigenere_message = ''.join(finmess_list)
            
    return vigenere_message




# In[108]:


#Intermediate 5

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    scy_list = []
    
    while len(message) % shift != 0:
        message = message+"_"
        
    for i in range(len(message)):
        x = (i // shift) + (len(message) // shift) * (i % shift)
        char = message[x]
        scy_list.append(char)
        
    scytale_message = ''.join(scy_list)
        
    return scytale_message



# In[109]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    decipher = ""
    
    for i in range(len(message)):
        decipher = decipher + message[(i // (len(message)//shift)) + (shift) * (i % (len(message)//shift))]
    
    return decipher


