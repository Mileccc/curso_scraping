from multiprocessing import Pool
from requests import get


def bajar_datos(url):
    return get(url).text


# URLs a procesar
urls = [
    f"http://numbersapi.com/{number}" for number in [1, 2, 3, 4, 5, 6, 7, 8]]
# print(urls)

# Procesamiento en paralelo con multiprocessing.Pool
if __name__ == "__main__":
    with Pool(8) as p:
        resultados = p.map(bajar_datos, urls)

    for resultado in resultados:
        print(resultado)

    # with Pool(5) as p:
    #     print(p.map(bajar_datos, urls))
