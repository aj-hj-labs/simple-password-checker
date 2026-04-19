InpPassword = input("Input Password: ")
if len(InpPassword) < 6:
    print("weak")
elif len(InpPassword) >= 6 and len(InpPassword) <= 10:
    print("medium")
elif len(InpPassword) > 10:
    print("strong")
