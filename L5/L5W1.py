def pix_to_mm(pixels_count: int) -> float:
    return pixels_count * 33.87


if __name__ == "__main__":
    while 1:
        try:
            pix = int(input("Pixels: "))
        except ValueError:
            print("Err")
            continue
        print("mm:", pix_to_mm(pix))
