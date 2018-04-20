import req
import itertools

def main():
    sel = itertools.combinations_with_replacement(["恵...","恵好き","恵愛してる","結婚しよ","大好き","好き好き","結婚しよう","僕が幸せにするよ","本当に好き","..."],9)
    for i in sel:
        req.tweet("enuwai","test1010","".join(i))

if __name__=='__main__':
    main()
