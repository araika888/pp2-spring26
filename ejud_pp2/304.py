class stringhandler:
    def __init__(self):
        self.text=""
    def alph(self):
        self.text=input()
    def upp(self):
        print(self.text.upper())

handler=stringhandler()
handler.alph()
handler.upp()