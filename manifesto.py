import time

manifesto = ["Technology is considered the new language of our time and is an important factor in shaping our art.",
              "Negligence and ignorance towards more traditional mediums are condemned,"
              "Deconstructing the conventional uses of the Internet to provide a more fun approach and subverting the expectations of user experiences and the associations within our current and future technologies",
              "Deconstructing the use of film and images in the context of computational arts",
              "Challenges the rules of the contemporary art space through provocative and invading art pieces",
              "Technology should be seen as an extension of our body and space and should be observed from an open mind"]

print("ARTIST MANIFESTO - RIZQ YAZED")

time.sleep(3)

for x in range(0, len(manifesto)):
    print(x,". ", manifesto[x])
    time.sleep(2)