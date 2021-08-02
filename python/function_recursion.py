# recursion: fonction appel soit meme
# ---------------------------------------
x = "wwoooorrrldd"
# je veux elliminer les caracteres repetés et retourner le mot sans repetition des caracteres


def cleanword(word):
    if len(word) == 1:
        return word

    print(f"print start function  {word}")

    if word[0] == word[1]:  # wwoooorrrldd retourne le mot "world"
        print(f"print before condition  {word}")
        return cleanword(word[1:])
    print(f"print before return  {word}")
    return word[0]+cleanword(word[1:])

    # stach[word]

    # je veux retourner le mot sans repetition des caracteres
print(cleanword("wwoooorrrldd"))

# print before condition  wwoooorrrldd
# print before return  woooorrrldd
# print before condition  oooorrrldd
# print before condition  ooorrrldd
# print before condition  oorrrldd
# print before return  orrrldd
# print before condition  rrrldd
# print before condition  rrldd
# print before return  rldd
# print before return  ldd
# print before condition  dd
# world
