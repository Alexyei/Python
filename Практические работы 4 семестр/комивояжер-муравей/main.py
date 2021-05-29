from salesman import Salesman

def main():
    # s = Salesman(Salesman.getTestSimpleDistance(),pathScale=5)
    s = Salesman(Salesman.getTestDistance())
    r = s.findShortest(render=True, animate=True)
    print("Муравьиный алгоритм: ")
    print(f"Минимальная дистанция: {r[0]:.2f}; Маршрут: {r[1]}")
    r1 = s.findShortestAll()
    print("Полный перебор: ")
    print(f"Минимальная дистанция: {r1[0]:.2f}; Маршруты: {r1[1]}")
    s.draw(r1[1])

if __name__=="__main__":
    main()

