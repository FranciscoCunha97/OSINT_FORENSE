import requests
from bs4 import BeautifulSoup
import datetime


def Mes_Numero(ola):
  if str(ola) == "janeiro":
    return 1
  elif str(ola) == "fevereiro":
    return 2
  elif str(ola) == "março":
    return 3
  elif str(ola) == "abril":
    return 4
  elif str(ola) == "maio":
    return 5
  elif str(ola) == "junho":
    return 6
  elif str(ola) == "julho":
    return 7
  elif str(ola) == "agosto":
    return 8
  elif str(ola) == "setembro":
    return 9
  elif str(ola) == "outubro":
    return 10
  elif str(ola) == "novembro":
    return 11
  else:
    return 12


def record_PESQUISAR():

  input1 = input("O que procura no Record: ")

  URL = "https://www.record.pt/pesquisa/?q=" + input1
  page = requests.get(URL)

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
  #0 -> 03 Novembro 2022, hora
  #1 -> 03-11-2022 / hora


def bola_PRINCIPAL():

  URL1 = "https://www.abola.pt"
  page = requests.get(URL1)
  Noticias = []

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  bola_elements1 = results.find_all("div", class_="info")
  aux = ""
  for bola_element in bola_elements1:

    titulo_bola = bola_element.find('span',
                                    {'class': "titulo ellipsis-2-line"})
    hora_bola = bola_element.find('span', {'class': "data-hora"})

    if str(titulo_bola) != "None" and str(hora_bola) != "None":
      if aux != titulo_bola.text and hora_bola.text != "":
        print(titulo_bola.text)
        print(hora_bola.text)
        aux = titulo_bola.text

  #1 -> 03.11.2022 / hora
  #0 -> hora ou data


def bola_PESQUISAR():
  input2 = input("O que procura na Bola: ")

  URL1 = "https://www.abola.pt/Pesquisa/" + input2
  page = requests.get(URL1)

  #print(page.text)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  print(results)
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


def Publico_PESQUISAR():
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

      publico_news = [titulo_noticia.strip(), link12, date.text]
      Todas_noticias_publico.append(publico_news)

  pl = 0

  for a in Todas_noticias_publico:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def Publico_PRINCIPAL():
  URL1 = "https://www.publico.pt/"
  page = requests.get(URL1)
  Todas_Noticias_Publico = []
  #print(page.text) card__header

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  Publico_todas = results.find_all("h2", class_="article__title")
  print(Publico_todas)

  for publico_element in Publico_todas:
    link_publico = publico_element.find('a')
    titulo_publico = (link_publico.text)
    link12 = link_publico.get('href')

    if "PÚBLICO" not in titulo_publico:

      p = [titulo_publico.strip(), "https://www.publico.pt/" + link12, ""]
      Todas_Noticias_Publico.append(p)

  pl = 0

  for a in Todas_Noticias_Publico:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def Correio_da_Manha_PRINCIPAL():
  URL1 = "https://www.cmjornal.pt/"
  page = requests.get(URL1)
  Todas_Noticias_Correio = []
  #print(page.text) card__header

  #f = open("Publico_Pag_Principal", "x")
  #f.write(page.text)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  Correio_todas = results.find_all("div", class_="text_container")

  Noti = []

  for correio_element in Correio_todas:
    correio_publico = correio_element.find('h4', {'class': "seccao"})
    titulo_publico = correio_element.find('a', {'class': "eventAnalytics"})

    noticia = ""
    link = ""
    #print(titulo_publico)

    if str(titulo_publico) != "None":
      if str(titulo_publico.text) != "Editoriais" and str(
          titulo_publico.text) != "CM Interativo" and str(
            titulo_publico.text) != "Gráficos Interativos" and str(
              titulo_publico.text) != "Apartamento" and str(
                titulo_publico.text) != "Escritório" and str(
                  titulo_publico.text) != "Quinta" and str(
                    titulo_publico.text) != "Um Podcast":

        r = str(titulo_publico.text)
        noticia = r

        if len(r.split()) == 1:
          titulo1_publico = correio_element.find(
            'a', {'class': "newsTitle eventAnalytics"})
          if str(titulo1_publico) != "None":
            noticia = r
        else:
          if "htpp" not in titulo_publico.get('href'):
            link = "https://www.cmjornal.pt/" + titulo_publico.get('href')

    a = [noticia, link]
    if noticia != "" and link != "":
      Noti.append(a)

  pl = 0

  for a in Noti:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def record_PRINCIPAL():
  URL = "https://www.record.pt/"
  pagex = requests.get(URL)

  soup = BeautifulSoup(pagex.content, "html.parser")
  results = soup.find()
  job_elements = results.find_all("div", class_="noticia_box")

  Todas_noticias_atuais = []

  for job_element in job_elements:

    company1 = job_element.find('a', {'class': 'eventAnalytics'})
    if str(company1) != "None":
      URL_req = "https://www.record.pt/" + company1.get('href')
      page_req = requests.get(URL_req)

      soup_req = BeautifulSoup(page_req.content, "html.parser")
      results_req = soup_req.find()
      job_req = results_req.find_all("div", class_="article_titles")

      for job in job_req:

        companye1 = job.find('span', {'class': 'article_date'})

        titulo = job.find('h1', {'class': ''})
        #print(titulo.text)
        if str(companye1) != "None":
          if len(companye1.text) < 6:
            now = datetime.datetime.now()
            aux = str(now.day) + '.' + str(now.month) + "." + str(
              now.year) + " - " + companye1.text
            #print(aux)
          else:
            aux = companye1.text
            auxiliar = aux.split()
            frase = auxiliar[0] + "." + str(Mes_Numero(
              auxiliar[1])) + "." + auxiliar[2] + " - " + auxiliar[4]
            #print(frase)
            aux = frase
          a = [
            titulo.text, aux, "https://www.record.pt/" + company1.get('href')
          ]
        Todas_noticias_atuais.append(a)

  pl1 = 0

  for a in Todas_noticias_atuais:
    print(str(pl1) + "-> ")
    print(a)
    print("\n\n")
    pl1 = pl1 + 1


def Expresso_PRICIPAL():
  URL = "https://expresso.pt/"
  pagex = requests.get(URL)

  soup = BeautifulSoup(pagex.content, "html.parser")
  results = soup.find()
  job_elements = results.find_all("div", class_="text-details")

  Todas_noticias_expresso = []

  for job_element in job_elements:

    company1 = job_element.find('h2', {'class': 'title'})
    #print(company1.text)
    link = company1.find('a')
    link_1 = link.get('href')

    data = job_element.find('div',
                            {'class': 'elements-wrapper date-and-author'})

    if "http" not in link_1:
      link_1 = "https://expresso.pt/" + link_1

    if str(data) != "None":
      data1 = data.find('p', {'class': 'time-stamp'})

      data2 = data1.text.strip()
    else:
      data2 = "No info about data or hour"

    a = [company1.text, link_1, data2]
    Todas_noticias_expresso.append(a)
    #print("\n\n")

  pl = 0
  for a in Todas_noticias_expresso:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def Correio_PESQUISAR():
  input2 = input("O que procura no Correio da Manha: ")

  URL1 = "https://www.cmjornal.pt/pesquisa/?q=" + input2
  page = requests.get(URL1)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  correio_elements = results.find_all("div", class_="text_container")

  Todas_noticias_correio = []

  for correio_element in correio_elements:
    title_news = correio_element.find("a", class_="eventAnalytics")
    link = ""
    if "http" in title_news.get('href'):
      link = title_news.get('href')
    else:
      link = "https://www.cmjornal.pt/" + title_news.get('href')

    a = [title_news.text.strip(), link]
    Todas_noticias_correio.append(a)

  pl = 0

  for a in Todas_noticias_correio:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def EXPRESSO_PESQUISAR():
  input2 = input("O que procura no Expresso: ")

  URL1 = "https://expresso.pt/pesquisa?q=" + input2
  page = requests.get(URL1)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  correio_elements = results.find_all("div", class_="textDetails")
  #print(correio_elements)

  Todas_noticias_expresso = []

  for correio_element in correio_elements:
    title_news = correio_element.find("h2", class_="title")

    if str(title_news) != "None":
      titulo = title_news.text
      aa = title_news.find("a")
      link = aa.get('href')
      if "http" not in link:
        link = "https://expresso.pt" + link

      title_news1 = correio_element.find("div", class_="inlineDateAndAuthor")
      if str(title_news1) != "None":
        data_news = title_news1.find(
          "p", class_="timeStamp js-relative-time publishedDate")

        aa = [titulo, link, data_news.text]
        Todas_noticias_expresso.append(aa)

  pl = 0

  for a in Todas_noticias_expresso:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def DN_PRINCIPAL():
  URL = "https://www.dn.pt/"
  pagex = requests.get(URL)

  soup = BeautifulSoup(pagex.content, "html.parser")
  results = soup.find()
  job_elements = results.find_all("a", class_="t-am-text")

  Diario = []

  for job_element in job_elements:

    #print(job_element)

    texto = job_element.find('h2', {'class': 't-am-title'})
    link_1 = job_element.get('href')
    if "http" not in link_1:
      link_1 = "https://www.dn.pt/" + link_1
    #print(texto.text)

    #print(link_1)
    a = [texto.text, link_1]
    Diario.append(a)

  pl = 0
  for ab in Diario:
    print(str(pl) + "-> ")
    print(ab)
    print("\n\n")
    pl = pl + 1


def SIC_Noticias():
  

  URL = "https://sicnoticias.pt/"
  page = requests.get(URL)

  soup = BeautifulSoup(page.content,"html.parser")
  results = soup.find()
  results1 = soup.find()
  job_elements = results.find_all("div", class_="relative-container")

  Todas_noticias_sic = []

  for job_element in job_elements:
    texto = job_element.find('h2', {'class': 'title AT-icon-element-target'})
    if str(texto) != "None":
      if "SIC" not in (texto.text) :
        texto1 = texto.find('a')
        link_1 = texto1.get('href')
        data = job_element.find('p', {'class': 'time-stamp js-relative-time publishedDate'})
        #print(data)
        if str(data) != "None":
          data1 = data.text
        else:
          data1 = "None"
  
  
        a = [texto.text,"https://sicnoticias.pt" + str(link_1),data1]
        Todas_noticias_sic.append(a)
    
  pl1 = 0
  
  for a in Todas_noticias_sic:
    print(str(pl1) + "-> ")
    print(a)
    print("\n\n")
    pl1 = pl1 + 1


def SIC_Noticias_Pesquisar():
  input2 = input("O que procura na Sic Noticias: ")

  URL1 = "https://sicnoticias.pt/pesquisa?q=" + input2
  page = requests.get(URL1)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find()
  correio_elements = results.find_all("div", class_="text-details")

  Todas_noticias_correio = []

  for correio_element in correio_elements:
    title_news = correio_element.find("h2", class_="title AT-icon-element-target")
    #data = correio_element.find("div", class_="inline-article-data")
    link = ""

    if str(title_news) != "None":
      if "SIC" not in (title_news.text) and "O Dia Seguinte" not in (title_news.text) and "Sem Título" not in (title_news.text):
        texto1 = title_news.find('a')
        link_1 = texto1.get('href')
        link_11=""
        if "http" in link_1:
          link_11 = link_1
        else:
          link_11 = "https://sicnoticias.pt/" + link_1

        data = correio_element.find('p', {'class': 'time-stamp js-relative-time publishedDate'})
        #print(data)
        if str(data) != "None":
          data1 = data.text
        else:
          data1 = "None"

        a = [title_news.text.strip(), link_11,data1]
        Todas_noticias_correio.append(a)

  pl = 0

  for a in Todas_noticias_correio:
    print(str(pl) + "-> ")
    print(a)
    print("\n\n")
    pl = pl + 1


def main():
  SIC_Noticias_Pesquisar()


if __name__ == "__main__":
  main()
