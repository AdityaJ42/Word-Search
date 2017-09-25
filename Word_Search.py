import os

search_in=input('Enter the path to search in: ')
word=input('Enter the word to search for: ')
find_word=word.lower()
os.chdir(search_in)
file_list=os.listdir(search_in)
for name in file_list:
    fo=open(name,'r')
    line=0
    flag=0
    content=fo.read()
    a=content.lower()
    a1=a.split()
    print ('In the file ',name)
    for words in a1:
        words=words.lower()
        word=''
        for ch in words:
            if(ch not in '!#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
                word+=ch
        if(find_word==word):
            flag+=1
    if(flag==0):
        print ('Word not found.')
    else:
        print('Word occurence: ',flag)
    print ()
    input()

