N = int(input('Введите целое число N<=27: '))

for i in range(100, 1000):
    if sum(map(int, str(i))) == N:
        print(i)