# To Revtext() function and Remove all Special Characters
def RevText(text):
    s = text.split()
    for i in range(len(s)):
        if s[i][0] == 'i' or s[i][0] == 'I':
            s[i] = s[i][::-1]
    text = ' '.join(s)
    return text
with open("Story.txt",'r') as f:
    text = f.read()
    text_update = ''
    for i in text:
        if i >= 'a' and i<= 'z' or i >= 'A' and i <= 'Z' or i ==  ' ':
            text_update += i
        else:
            continue
    text = RevText(text_update)
    with open('write.txt','w') as f1:
        f1.write(text)
    print("Written Successfully !!")
            
