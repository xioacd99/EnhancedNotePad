from MyQR import myqr


def UrlMake2dbgMap(url_file, bgpic, result_pic):
    fo = open(url_file, "r")
    url = fo.read()

    myqr.run(words=url,
             picture=bgpic,
             colorized=True,    # True：彩色，False：黑白
             save_name=result_pic)


UrlMake2dbgMap("./url.txt", "./001.png", "./result.png")
