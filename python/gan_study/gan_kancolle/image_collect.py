from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "urakaze_eng"})
crawler.crawl(keyword="urakaze", max_num=999)