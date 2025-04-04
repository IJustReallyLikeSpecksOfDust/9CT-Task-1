#pseudocode activity thing again

#purchasing books
isdone = False
done = 19.2

while isdone == False:
    bookprice = 0
    answer = (input("How expensive is the book? $"))
    if answer == done:
        isdone = True
    else:
        bookprice = bookprice + int(answer)


