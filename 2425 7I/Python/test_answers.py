def get_days_with_max_attendees(attendees: list[list[str]]) -> str:
    rep = ""
    daily_attendance = [0, 0, 0, 0, 0]

    for day in range(len(daily_attendance)):
        for attendee in attendees:
            if attendee[day] == "Y":
                daily_attendance[day] += 1

    max_attendance = max(daily_attendance)

    for day in range(len(daily_attendance)):
        if daily_attendance[day] == max_attendance:
            rep += str(day + 1)

    return ",".join(rep)


def get_total_spiciness(peppers: list[str]) -> int:
    total_spiciness = 0

    for pepper in peppers:
        if pepper == "Poblano":
            total_spiciness += 1500
        if pepper == "Mirasol":
            total_spiciness += 6000
        if pepper == "Serrano":
            total_spiciness += 15500
        if pepper == "Cayenne":
            total_spiciness += 40000
        if pepper == "Thai":
            total_spiciness += 75000
        if pepper == "Habanero":
            total_spiciness += 125000

    return total_spiciness


def get_leftover_cupcakes(num_reg: int, num_small: int) -> int:
    class_size = 28
    cc_per_reg = 8
    cc_per_small = 3
    total_cupcakes = cc_per_reg * num_reg + cc_per_small * num_small
    leftover_cupcakes = total_cupcakes - class_size
    return leftover_cupcakes


def get_dusa_size(dusa_size: int, yobis: list[int]) -> int:
    for yobi in yobis:
        if dusa_size > yobi:
            dusa_size += yobi
        else:
            return dusa_size

    return dusa_size


# print(get_dusa_size(5, [3, 2, 9, 20, 22, 14]))
# print(get_dusa_size(10, [10, 3, 5, 13]))


# scores = [70, 62, 58, 73]
# print(get_bronze_count(scores))

# scores = [75, 70, 60, 70, 70, 60, 75, 70]
# print(get_bronze_count(scores))


# calendar = [
#     ["Y", "Y", ".", "Y", "."],
#     [".", ".", ".", "Y", "."],
#     [".", "Y", "Y", "Y", "."],
# ]

# print(get_days_with_max_attendees(calendar))

# calendar = [
#     ["Y", "Y", ".", ".", "Y"],
#     [".", "Y", "Y", ".", "Y"],
#     [".", "Y", ".", "Y", "."],
#     [".", "Y", "Y", ".", "Y"],
#     ["Y", ".", ".", ".", "Y"],
# ]

# print(get_days_with_max_attendees(calendar))
