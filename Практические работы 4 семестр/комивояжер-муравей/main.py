from salesman import Salesman

def main():
    s = Salesman(Salesman.getTestDistance())
    r = s.findShortest(render=True, animate=True)
    print(r)

if __name__=="__main__":
    main()

