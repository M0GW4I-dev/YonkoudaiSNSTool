import req
import random
import itertools
def main():
    g = itertools.combinations_with_replacement(["藍子ちゃん","藍子","...","好き","大好き","愛してる","高森...","あ、い、こ","♡","好き好き","結婚しよ"],10)
    for i in g:
        req.tweet("donikiBot","dbrk666","".join(i))
        
if __name__=='__main__':
    main()
