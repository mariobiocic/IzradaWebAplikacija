import socket, time

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print (e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000000).decode('latin-1')
    print (response)
    return response

def get_all_links(response):
    list_links = []
    beg = 0
    while True:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return list_links  
            break
        end_str = response.find('"', beg_str + 6)      
        link = response[beg_str + 6:end_str]
        if link not in list_links:
            list_links.append(link)
        beg = end_str + 1
        

def posjeceni(s, ip, links):
    lista_posjecenih = []
    count = 0
    for link in links:
        if count >= 50:
            break
        response = get_source(s, ip, link)
        odg_links = get_all_links(response)
        if odg_links:
            if link not in lista_posjecenih:
                lista_posjecenih.append(link)
                count += 1
            for odg_link in odg_links:
                if odg_link not in lista_posjecenih:
                    lista_posjecenih.append(odg_link)
                    count += 1
    return lista_posjecenih         

ip='crawler-test.com'
port = 80
page = '/'
s = connect_to_server(ip, port)
print (s)
response = get_source(s, ip, page)
links=get_all_links(response)
print(links)

posjecene_stranice = posjeceni(s, ip, links)
print(posjecene_stranice)

broj_posj_stranica=len(posjecene_stranice)
print("broj je: ",broj_posj_stranica)