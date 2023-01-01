import random

cities = [ "Karachi", "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala", "Hyderabad", "Peshawar", "Islamabad", "Quetta", "Sargodha", "Sialkot", "Bahawalpur", "Sukkur", "Kandhkot", "Sheikhupura", "Mardan", "Gujrat", "Larkana", "Kasur", "Rahim" "Yar" "Khan", "Sahiwal", "Okara", "Wah" "Cantonment", "Dera" "Ghazi" "Khan", "Mingora", "Mirpur" "Khas", "Chiniot", "Nawabshah", "Kamoke", "Burewala", "Jhelum", "Sadiqabad", "Khanewal", "Hafizabad", "Kohat", "Jacobabad", "Shikarpur", "Muzaffargarh", "Khanpur", "Gojra", "Bahawalnagar", "Abbottabad", "Muridke", "Pakpattan", "Khuzdar", "Jaranwala", "Chishtian", "Daska", "Mandi" "Bahauddin", "Ahmadpur" "East", "Kamalia", "Tando" "Adam", "Khairpur", "Dera" "Ismail" "Khan", "Vehari", "Nowshera", "Dadu", "Wazirabad", "Khushab", "Charsada", "Swabi", "Chakwal", "Mianwali", "Tando" "Allahyar", "Kot" "Adu", "Farooka", "Chichawatni", "Vehari", "Mansehra"  ]

print("List of Pakistani cities before shuffle:")
print(", ".join(cities), end="\n\n")

random.shuffle(cities)

print("List of Pakistani cities after shuffle: ")
print(", ".join(cities))
