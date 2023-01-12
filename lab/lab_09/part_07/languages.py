overall_students = 110

english = 25
spanish = 10
french = 11

english_spanish = 20
french_spanish = 9
english_french = 17

english_french_spanish = 13

one_of_three = english + spanish + french
two_of_three = english_spanish + french_spanish + english_french

language_students = one_of_three + two_of_three + english_french_spanish
non_language_students = overall_students - language_students

print("Students who speak English and Spanish, but not French: " + str(english_spanish))
print("Students who speak none of English, Spanish, and French: " + str(non_language_students))
print("Students who speak French, but neither English nor Spanish: " + str(french))
print("Students who speak only one of French, English or Spanish: " + str(one_of_three))
print("Students who speak exactly two of English, Spanish, or French: " + str(english_spanish))
print("Students who do speak a language: " + str(language_students))