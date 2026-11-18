def clean_amount(text):
    """৳ আর কমা সরিয়ে সংখ্যায় ফেরত দিন।"""
    cleaned = text.replace("৳", "").replace(",", "").strip()
    return float(cleaned)


def taka(amount):
    """1240.5  →  "৳1240.50" """
    return f"৳{amount:.2f}"


def read_lines(path):
    """ফাইল পড়ে লাইনগুলোর list ফেরত দিন।"""
    with open(path, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            stripped = line.strip()
            if stripped:
                lines.append(stripped)
        return lines


if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))  # 1240.5
    print(taka(1240.5))                   # ৳1240.50
