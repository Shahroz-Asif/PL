guests = {
    "self_invited": [ "Joe", "Jacqueline", "Joseph", "Jack", "Jill", "Jane", "Jordan", "Josh", "John", "Jimmy" ],
    "parents_invited": [ "Jack", "Jake", "Jane", "John", "Joe", "Josh", "Jacqueline", "Jennifer", "Jordan", "Jill" ]
}

def count_guests():
    unique_guests = set(guests["self_invited"])
    unique_guests.update(guests["parents_invited"])
    unique_guests_count = len(unique_guests)

    return unique_guests_count

def count_attendees():
    family_count = 5
    guests_count = count_guests()

    return family_count + guests_count

guests_count = count_guests()
attendees_count = count_attendees()
print("The total number of guests are: " + str(guests_count))
print("The total number of attendees are: " + str(attendees_count))