# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JardiscraperPipeline:
    def process_item(self, item, spider):

        adaptater = ItemAdapter(item)

        field_names = adaptater.field_names()
        for field_name in field_names:
            if field_name == "src":
                value = adaptater.get(field_name)
                adaptater[field_name] = value.split("-")[-1]


        #convert string to number
        # nbr_rater_string = adaptater.get("nbr_rater")
        # adaptater["nbr_rater"] = int(nbr_rater_string)



        return item
