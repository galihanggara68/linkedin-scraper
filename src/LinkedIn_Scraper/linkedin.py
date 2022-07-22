class LinkedInScraper:
    def __init__(self, driver, finder, cookie_path):
        self.driver = driver
        self.finder = finder
        self._load_cookie(cookie_path)
        
    def _load_cookie(self, path):
        with open(path, 'r') as cookiesfile:
            self.cookies = json.load(cookiesfile)
            
    def _apply_cookie(self):
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        
    def exec_scraper(self, username):
        self.finder.load_mapping("json_scheme_ld.json")
        curr_mapping = self.finder.get_mapping()
        curr_mapping["search"]["text"] = f"'{username}'"
        self.finder.set_mapping(curr_mapping)
        
        self.driver.get("https://www.linkedin.com")
        self.driver.maximize_window()
        self._apply_cookie()
        self.driver.refresh()
        self.finder.by_json_scheme()
        
    def get_data(self):
        return self.finder.get_mapped_data()