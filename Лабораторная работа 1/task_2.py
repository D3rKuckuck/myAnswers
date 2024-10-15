#yuPIT/4oXScdiUb4qTdbULlw+hDW1HnbKSPvqxTaHfyINNTOzgSLLwaVQ9365tKjrxN5Z7NO76cfdgERXi+djkXOBwo9+ORjSCHF1G3H+Y2e/Wb3Uf0y4SMfxBTpCo+qcNO5WlGAbhql2ew5BISU2I4Amgvs9OdTslnZiBwT9dSD3v0=
def CountSpace(disk,book):
    booksize=book["pages"]*book["strings"]*book["symbols"]*book["bytes"]/1024**2
    print("book size ", booksize, "for space ", disk,"\n")
    count=disk//booksize
    return count

#Right our data
disk=1.44 #Changin MB in byte
book={"pages": 100,
      "strings": 50,
      "symbols": 25,
      "bytes": 4}
#Finding count of books
count=CountSpace(disk,book)
print(count, "books we can place")
