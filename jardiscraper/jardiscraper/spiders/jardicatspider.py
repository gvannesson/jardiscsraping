import scrapy
from jardiscraper.spider_functions import get_random_user_agent
import time, random as rd

class BricospiderSpider(scrapy.Spider):
    name = "jardicatspider"

    start_urls = ["https://www.jardiland.com"]

    def parse(self, response):
        print("############################salut#####################""")
        categories = response.css("a.ens-main-navigation-items__link.ds-ens-anchor.ds-ens-anchor--link.ens-main-navigation-items__link")
        for categorie in categories:
            url_du_moment="https://www.jardiland.com"+categorie.attrib['href']
            titre_du_moment=categorie.css('.ens-main-navigation-items__link-label  ::text').get()
            print(url_du_moment)
            print("")
            if "promotions" in url_du_moment or "conseils-idees" in url_du_moment\
                or "animalerie"in url_du_moment or "plante"in url_du_moment or "jardinage"in url_du_moment\
                or "amenagement-exterieur"in url_du_moment or "maison" in url_du_moment:
                print(f"categorie eliminée    {url_du_moment}")
                continue

            print(url_du_moment)
            # time.sleep(rd.uniform(1, 3))

            yield response.follow(
                url=url_du_moment,
                callback=self.parse_subcategorie,
                meta={'cat_parente': self.start_urls[0],'titre_du_moment':titre_du_moment, "ma_cat_actuelle": url_du_moment}
            )


    def check_categorie(self, response):
        return response.css('a.ens-product-list-categories__item')
    

    def parse_subcategorie(self, response):
        print("############################hello#####################""")
        sub_categories = response.css('a.ens-product-list-categories__item')
        print(sub_categories)
        classe_parente = response.meta['cat_parente']
        for sub_categorie in sub_categories:
            print(f"------------------{sub_categorie}")
            url_du_moment="https://www.jardiland.com"+sub_categorie.attrib['href']
            print(f"------------------{url_du_moment}")
            title_du_moment = sub_categorie.css("::text").get()
            print(f"#############{title_du_moment}")
            print(f'~~~~~~~~~~~~~~{response.follow(url=url_du_moment,callback=self.check_categorie)}')
                
            print(f"le titre de la sous categorie qui vient d etre yieldé {title_du_moment}")

            yield response.follow(
                url=url_du_moment,
                callback=self.parse_subcategorie,
                meta={'cat_parente': classe_parente,'titre_du_moment':title_du_moment, "ma_cat_actuelle": url_du_moment}
            )

        yield{
            "titre_categorie":response.meta['titre_du_moment'],
            "url_categorie":response.meta['ma_cat_actuelle'],
            'is_page_list':False if sub_categories else True
            }

