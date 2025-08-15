def main():

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        try:
            m_str, d_str, y_str = date_str.split("/")
            m, d, y = int(m_str), int(d_str), int(y_str)
            if 1 <= m <= 12 and 1 <= d <= 31:
                break 
        except ValueError:
            try:
                month_name, d_str, y_str = date_str.split(" ")

                if not d_str.endswith(","):
                    continue

                d_str = d_str.replace(",", "") 
                d, y = int(d_str), int(y_str)

                m = months.index(month_name) + 1

                if 1 <= d <= 31:
                    break 
            except (ValueError, KeyError):
                pass

    print(f"{y}-{m:02}-{d:02}")


if __name__ == "__main__":
    main()
