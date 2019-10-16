import lingkaran

def main ():
    #luas lingkaran
    r = 5

    luas = lingkaran.luaslingkaran(r)

    print("LUAS LINGKARAN")
    print("jari-jari\t: ", r)
    print("luas\t: ", luas)

    #keliling lingkaran
    r = 6

    keliling = lingkaran.kelilinglingkaran(r)

    print("\nKELILING LINGKARAN")
    print("jari-jari\t: ", r)
    print("keliling\t: ", keliling)

    #volume lingkaran
    r = 10

    volume = lingkaran.volumelingkaran(r)

    print("\nVOLUME LINGKARAN")
    print("jari-jari\t: ", r)
    print("volume\t: ", volume)


if __name__ == "__main__":
    main()