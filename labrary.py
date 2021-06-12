
def fos ():
    from platform import system as si
    ba = {'Windows':'\\','Linux':r'/'}
    b = ba[si()]
    return b