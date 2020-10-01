
from api_handler import ApiHandler
from urls import donald, chuck


while True: 
    print("Choose a quote from either Chuck Norris or Donald Trump \nChuck Norris = 1 \nDonald Trump = 2")
    choice = input("->")
    if choice == "1":        
        random_chuck_quote = ApiHandler(chuck)
        print(random_chuck_quote.getQuote())
    elif choice == "2":
        donald_quote = ApiHandler(donald)
        print(donald_quote.getQuote())
    else:
        print("please choose 1 or 2")










