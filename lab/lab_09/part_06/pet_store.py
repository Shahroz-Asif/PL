dog_product = 83
cat_product = 101
fish_product = 22
other_product = 34

dog_cat_product = 31
dog_fish_product = 8
cat_fish_product = 10

dog_cat_fish_product = 6

dog_only_product = dog_product - dog_cat_product - dog_fish_product - dog_cat_fish_product
cat_only_product = cat_product - dog_cat_product - cat_fish_product - dog_cat_fish_product
fish_only_product = fish_product - dog_fish_product - cat_fish_product - dog_cat_fish_product

dog_cat_only_product = dog_cat_product - dog_cat_fish_product
dog_fish_only_product = dog_fish_product - dog_cat_fish_product
cat_fish_only_product = cat_fish_product - dog_cat_fish_product

dog_or_fish_product = dog_only_product + fish_only_product + dog_fish_only_product

total_purchases = dog_only_product + cat_only_product + fish_only_product + dog_cat_only_product + dog_fish_only_product + cat_fish_only_product + dog_cat_fish_product

print("The amount of dog-only product purchases are: " + str(dog_only_product))
print("The amount of cat-only product purchases are: " + str(cat_only_product))
print("The amount of dog product or fish product purchases are: " + str(dog_or_fish_product))
print("The amount of total purchases are: " + str(total_purchases))