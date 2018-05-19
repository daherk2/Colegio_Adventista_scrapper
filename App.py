
import urllib2 as lib2

BASEURL = ".educacaoadventista.org.br/equipe"

cidades = ['lorena', 'taubate', 'saojosedoscampos', 'jacarei']

for i in range(0, len(cidades)):
    cid = cidades[i]
    #print 'http://'+cid+BASEURL
    url = 'http://'+cid+BASEURL
    pagina = lib2.urlopen(url).readlines()
    test = 'http://images.educacaoadventista.org.br/cache//!sttc-imgs/siteescola/sites/sp/'+cid+'/team/'
    for linha in pagina:
        if test in linha and 'default.jpg' not in linha:
            print linha.split('src="')[1].split('/117/117')[0]+'/250/250'