class Circle:

    PI = 3.1415

    def ensyu(r):
        m = int(r * 2 * Circle.PI * 1000)
        m = m / 1000
        return m

    def menseki(r):
        m = int(r * r * Circle.PI * 1000)
        m = m / 1000
        return m

    def print(r) -> None:
        ensyu = Circle.ensyu(r)
        menseki = Circle.menseki(r)

        print("円周の長さは{}です。".format(ensyu))
        print("円周の面積は{}です。".format(menseki))


a = int(input("半径を整数値で入力："))

Circle.print(a)