dishes = {
    "preference": [ "Nihari", "Karahi", "Qorma" ],
    "cooked": [ "Bryani", "Qorma", "Palao", "Achari Gosht", "Nihari" ]
}

common_dishes = [ dish for dish in dishes["preference"] if dish in dishes["cooked"] ]
print("My preferred dishes to be cooked by next week are: " + ", ".join(common_dishes))