alphabets=["a","b",'c',"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def cipher(original_text,shift_amount,endode_or_decode):
    cipher=""
    if endode_or_decode=="decode":
                shift_amount*=-1
    for letter in original_text:
        if letter not in alphabets:
            cipher+=letter
        else:
                shift_position=alphabets.index(letter)+shift_amount
                shift_position%=len(alphabets)
                cipher+=alphabets[shift_position]
    print(f"here  is your output text {cipher}")
should_continue=True
while should_continue:
    direction=input("Type encode for encryption, Type decode for decryption:\n").lower()
    shift=int(input("Enter shift amount:\n"))
    word=input("Enter the text to be change:\n").lower()
    cipher(word,shift,direction)
    repeat=input("Type yes for repeat again or no:\n").lower()
    if repeat=="no":
        should_continue=False
        print("OVER")
