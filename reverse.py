def reverse(testo):

    def reverso(word: object) -> object:
        return word[::-1]

    nuovo = ""
    nuovo += reverso(testo)

    f = lambda x: x.strip().title()

    return f(nuovo)


print(reverse("This is a string"))
