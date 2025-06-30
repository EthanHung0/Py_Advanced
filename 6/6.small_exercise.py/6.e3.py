from Classes import CreditCard,PayPal,CryptoWallet

tlist = [CreditCard(),PayPal(),CryptoWallet()]

print(tlist[0].pay(50)) #Invalid
for i in tlist:
    i.authenticate()
    print(i.pay(30))