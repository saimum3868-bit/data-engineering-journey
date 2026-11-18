import my_tools

def main():
    file_path = "/home/ubuntu/de-bootcamp/ostad-de-bootcamp/module-02/data/raw_sales.txt"
    lines = my_tools.read_lines(file_path)
    

    # পেমেন্ট মেথড অনুযায়ী সংখ্যা ও টাকার ঘর (loop-এর বাইরে)
    bkash_count, bkash_total = 0, 0.0
    nagad_count, nagad_total = 0, 0.0
    card_count, card_total = 0, 0.0
    rocket_count, rocket_total = 0, 0.0
    cod_count, cod_total = 0, 0.0

    # বোনাস: তারিখের হিসাব রাখার ঘর
    d07, d08, d09, d10, d11 = 0.0, 0.0, 0.0, 0.0, 0.0

    for line in lines:
        parts = [p.strip() for p in line.split(";")]
        if len(parts) < 8:
            continue

        date = parts[1]
        amount = my_tools.clean_amount(parts[5])
        method = parts[6].lower()
        status = parts[7].lower()

        # বাতিল অর্ডার বাদ দেওয়া হচ্ছে
        if status == "cancelled":
            continue

        # পেমেন্ট মেথড অনুযায়ী যোগ করা
        if method == "bkash":
            bkash_count += 1
            bkash_total += amount
        elif method == "nagad":
            nagad_count += 1
            nagad_total += amount
        elif method == "card":
            card_count += 1
            card_total += amount
        elif method == "rocket":
            rocket_count += 1
            rocket_total += amount
        elif method == "cash on delivery":
            cod_count += 1
            cod_total += amount

        # বোনাস: তারিখ অনুযায়ী যোগ করা
        if date == "2026-10-07":
            d07 += amount
        elif date == "2026-10-08":
            d08 += amount
        elif date == "2026-10-09":
            d09 += amount
        elif date == "2026-10-10":
            d10 += amount
        elif date == "2026-10-11":
            d11 += amount

    grand_total = bkash_total + nagad_total + card_total + rocket_total + cod_total

    # সব print একসাথে শেষে
    print("payment ধরে হিসাব (বাতিল বাদে)\n")
    print(f"{'bkash':<17} {bkash_count}টা   {my_tools.taka(bkash_total)}")
    print(f"{'nagad':<17} {nagad_count}টা   {my_tools.taka(nagad_total)}")
    print(f"{'card':<17} {card_count}টা   {my_tools.taka(card_total)}")
    print(f"{'rocket':<17} {rocket_count}টা   {my_tools.taka(rocket_total)}")
    print(f"{'cash on delivery':<17} {cod_count}টা   {my_tools.taka(cod_total)}")
    print(f"\nসব মিলিয়ে: {my_tools.taka(grand_total)}")

    # বোনাস আউটপুট: সবচেয়ে বেশি বিক্রির তারিখ বের করা
    best_date = "2026-10-07"
    best_amount = d07

    if d08 > best_amount:
        best_date, best_amount = "2026-10-08", d08
    if d09 > best_amount:
        best_date, best_amount = "2026-10-09", d09
    if d10 > best_amount:
        best_date, best_amount = "2026-10-10", d10
    if d11 > best_amount:
        best_date, best_amount = "2026-10-11", d11

    print(f"\nবোনাস — সবচেয়ে বেশি বিক্রি: {best_date} ({my_tools.taka(best_amount)})")


if __name__ == "__main__":
    main()
