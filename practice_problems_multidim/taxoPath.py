from cmput274 import *

def taxoPath(tree, cl):
    '''
    taxoPath returns a. LList of all of the classifications of cl within the taxoTree tt

    tt      - TaxoTree
    cl      - a Str
    returns - A LList of Str
    '''
    if tree == ():
        return empty()
    if tree[0] == cl:
        return LL(cl)
    children = tree[1:]
    findThis = lambda t: taxoPath(t, cl)
    possiblePaths = map(findThis, children)
    filteredPaths = filter(lambda p: not isEmpty(p), possiblePaths)
    if isEmpty(filteredPaths):
        return empty()
    return cons(tree[0], first(filteredPaths))

def main():
    taxo_tree = ("Chordata",
            ("Mammalia",
                ("Primates",
                    ("Hominidae",
                        ("Homo sapiens",),
                        ("Pan troglodytes",)
                    )
                ),
                ("Carnivora",
                    ("Felidae",
                        ("Panthera leo",),
                        ("Panthera tigris",)
                    )
                )
            ),
            ("Aves",
                ("Accipitriformes",
                    ("Cathartidae",),
                    ("Sagittariidae",)
                )
            )
       )
    print(taxoPath(taxo_tree, "Homo sapiens"))

if __name__ == "__main__":
    main()