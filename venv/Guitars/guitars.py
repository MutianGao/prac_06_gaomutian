from Guitars.guitar import Guitar
def main():
    print("My guitars!")
    guitars = []
    name = input("Name:")
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    guitars.append(Guitar(name, year, cost))
    print(f'{name} ({year}) : $ {cost} added.')
    while name != 0:
        name = input("Name:")
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitars.append(Guitar(name, year, cost))
        print(f'{name}({year}):$ {cost}added.')
    print("These are my guitars:")
    print(guitars)
main()
