import os
import csv
from datetime import datetime

class JobscraperPipeline:
    def __init__(self):
        self.file_path = None
        self.items = []  # Store all items in memory

    def open_spider(self, spider):
        """Called when the spider starts"""
        today_date = datetime.today().strftime('%Y-%m-%d')
        self.folder_path = os.path.join(os.getcwd(), today_date)
        os.makedirs(self.folder_path, exist_ok=True)  # Create folder if it doesn’t exist

        self.file_path = os.path.join(self.folder_path, f"{spider.name}.csv")

    def process_item(self, item, spider):
        """Called for each scraped item - store in memory"""
        self.items.append([
            item.get("company_name", ""), item.get("role", ""), item.get("location", ""),
            item.get("stipned", ""), item.get("salary", ""), item.get("duartion", ""),
            item.get("post_link", ""), item.get("posted_date", ""), item.get("start_date", ""),
            item.get("apply_by", ""), item.get("total_applicants", ""), item.get("skills", ""),
            item.get("openings", ""), item.get("website_link", ""), item.get("job_type", ""),
            item.get("responsibilities", ""), item.get("about_company", ""), item.get("activities", "")
        ])
        return item

    def close_spider(self, spider):
        """Called when the spider closes - writes all data at once (overwriting file)"""
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Ensure headers match your Scrapy Item fields exactly
            writer.writerow([
                "company_name", "role", "location", "stipned", "salary", "duartion",
                "post_link", "posted_date", "start_date", "apply_by", "total_applicants",
                "skills", "openings", "website_link", "job_type", "responsibilities",
                "about_company", "activities"
            ])
            # Write all stored items
            writer.writerows(self.items)
