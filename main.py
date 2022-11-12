import requests
from bs4 import BeautifulSoup
import datetime


def Mes_Numero(ola):
  if str(ola) == "Janeiro":
    return 1
  elif str(ola) == "Fevereiro":
    return 2
  elif str(ola) == "Março":
    return 3
  elif str(ola) == "Abril":
    return 4
  elif str(ola) == "Maio":
    return 5
  elif str(ola) == "Junho":
    return 6
  elif str(ola) == "Julho":
    return 7
  elif str(ola) == "Agosto":
    return 8
  elif str(ola) == "Setembro":
    return 9
  elif str(ola) == "Outubro":
    return 10
  elif str(ola) == "Novembro":
    return 11
  else:
    return 12


def record():
  input1 = input("O que procura no Record: ")

  URL = "https://www.record.pt/pesquisa/?q=" + input1
  page = requests.get(URL)

  #print(page.text)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  job_elements = results.find_all("div", class_="noticia_box")
  job_elements1 = results.find_all("img", class_="img-fluid")

  noticia = []
  link = []

  for job_element in job_elements:

    title_element = job_element.find("h1", class_="eventAnalytics")
    company1 = job_element.find('a', {'class': 'eventAnalytics'})
    #print(company1.get('href'))  #LINKS
    link.append("https://www.record.pt/" + company1.get('href'))
    #print(company1.text)
    noticia.append(company1.text)

  Todas_noticias = []
  p = 0

  for job_elementa in job_elements1:

    a = job_elementa.get('src')
    if ("record" in a):

      x = a.split("$")
      data = x[1].split("_")
      dia = data[2] + "-" + data[1] + "-" + data[0]
      hora = data[3] + ":" + data[4] + ":" + data[5]

      b = [noticia[p], link[p], dia, hora]
      Todas_noticias.append(b)

      p = p + 1

  pl1 = 0

  for a in Todas_noticias:
    print(str(pl1) + "-> ")
    print(a)
    print("\n\n")
    pl1 = pl1 + 1


def bola():
  input2 = input("O que procura na Bola: ")

  URL1 = "https://www.abola.pt/Pesquisa/" + input2
  page = requests.get(URL1)

  #print(page.text)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  bola_elements = results.find_all("div", class_="media mt-15")

  id1 = 0
  Todas_noticias_bola = []

  for bola_element in bola_elements:

    #print("=====")
    title_news = bola_element.find("h4", class_="media-heading")
    #print(title_news.text)
    ola1 = ""
    ola1 = "body_NoticiasPesquisa_rptNoticiasTodas_lblHora_" + str(id1)

    hora_bola = bola_element.find('span', {'id': ola1})

    dia_bola = bola_element.find('span', {'class': 'data-vermelho data-hora'})

    if dia_bola == None:
      now = datetime.datetime.now()
      aux = str(now.day) + '.' + str(now.month) + "." + str(now.year)
    else:
      aux = dia_bola.text

    ola = "body_NoticiasPesquisa_rptNoticiasTodas_hplImg_" + str(id1)
    link = ""

    link_bola = bola_element.find('a', {'id': ola})
    if "https://" not in link_bola.get('href'):
      link = "https://www.abola.pt/" + link_bola.get('href')
    else:
      link = link_bola.get('href')
    id1 = id1 + 1

    bola = [title_news.text[1:], link, aux, hora_bola.text]
    Todas_noticias_bola.append(bola)

  pl = 0

  for a in Todas_noticias_bola:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def Publico():
  input2 = input("O que procura no Publico: ")

  URL1 = "https://www.publico.pt/pesquisa?query=" + input2
  page = requests.get(URL1)

  #print(page.text)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  publico_elements = results.find_all("div", class_="media-object-section")
  #print(publico_elements)

  Todas_noticias_publico = []

  for bola_element in publico_elements:

    asx = bola_element.find("h4", class_="headline")

    if ("PÚBLICO" not in asx.text):

      link_bola = bola_element.find('a')
      link12 = link_bola.get('href')
      #print(link)

      URL3 = link12
      page3 = requests.get(URL3)

      #print(page.text)

      soup3 = BeautifulSoup(page3.content, "html.parser")
      results3 = soup3.find()

      t = results3.find("h1", class_="headline story__headline")
      titulo_noticia = t.text.replace("  ", "")
      #print(titulo_noticia)

      date = results3.find("time", class_="dateline")
      #print(date.text)

      if "\r\c" in titulo_noticia:
        print("ola")

      publico_news = [titulo_noticia, link12, date.text]
      Todas_noticias_publico.append(publico_news)

  pl = 0

  for a in Todas_noticias_publico:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def main():
  Publico()


if __name__ == "__main__":
  main()
