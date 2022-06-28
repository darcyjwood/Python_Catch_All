

elif command == 5:
            ItemPriceList = []
            for item in cart:
                ItemPrice = ItemPriceInv[item][0]
                ItemNum = cart[item]
                ItemPriceList.extend([ItemPrice]*ItemNum)
            print(ItemPriceList)