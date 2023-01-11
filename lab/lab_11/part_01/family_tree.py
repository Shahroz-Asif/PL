family = {
    "brother": "Joe",
    "sister": "Jane",
    "mother": "Jill",
    "father": "Jack"
}

print("Family tree: ", family, end="\n\n")

family["maternal grandfather"] = "Joseph"
family["materal grandmother"] = "Jennifer"
family["paternal grandfather"] = "James"
family["paternal grandmother"] = "Jacqueline"

print("Updated family tree: ", family)