import requests
from bs4 import BeautifulSoup


proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}


def create_list(m_divs):
    lst = []
    for strong_tag in m_divs:
        lst.append(strong_tag.text)

    return lst


def remove_extra_content(revised_lst):

    revised_lst2 = []

    error_list = ['Posted by', 'at', 'Language: text', '•', 'Views:']

    for j in error_list:
        for index, i in enumerate(revised_lst):
            if j in i:
                w = i.replace(j, "")
                revised_lst[index] = w

    for x in revised_lst:
        p = x.split('UTC', 1)[0] + 'UTC'
        revised_lst2.append(p)

    return revised_lst2


def create_multiple_lists():

    r = requests.get("http://nzxj65x32vh2fkhk.onion/all", proxies=proxies)

    soup = BeautifulSoup(r.text, "html.parser")

    mydivs = soup.findAll("div", class_="pre-info pre-footer")

    mydivs_titles = soup.findAll("div", class_="col-sm-5")

    mydivs_content = soup.findAll("div", class_="text")

    my_list = create_list(mydivs)

    new_list = remove_extra_content(my_list)

    # create the list of authors
    my_authors = [i.split()[0] for i in new_list]

    # create the list of dates
    my_dates = [x.split("  ")[1:][0] for x in new_list]

    # create the list of titles
    my_titles = create_list(mydivs_titles)

    # create the list of all content
    my_content = create_list(mydivs_content)

    # strip trailing spaces in content
    my_content = filter(lambda x: x.strip(), my_content)

    return my_authors, my_dates, my_titles, my_content
