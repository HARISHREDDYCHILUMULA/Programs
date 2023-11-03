def anagram(a,b):
    if len(a)!=len(b):
        print('Different size')
        return
    a1=sorted(a)
    b1=sorted(b)
    if a1==b1:
        print("Anagram")
    else:
        print("Not an Anagram")
anagram(input('Enter 1: '),input('Enter 2:'))
