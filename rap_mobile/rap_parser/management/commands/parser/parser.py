from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

from rap_parser.management.commands.parser.settings import (
    link_to_site,
    next_page_xpath,
    for_links_selector,
    with_link_selector,
    link_attribute,
    title_selector,
    rating_selector,
    rating_attribute,
    track_list_selector,
    link_to_download_selector,
    link_to_download_attribute,
)
from api.models import Album


class WebParser:
    """control parser and specification"""
    def __init__(self):
        self.__browser = webdriver.Firefox(options=self.__set_options())

    @staticmethod
    def __set_options():
        """return headless options for web_parser driver"""
        options = Options()
        options.add_argument("--headless")

        return options

    def start_parse(self, count=None):
        """open site and start parsing"""
        self.__open_site()

        for _step in range(count):
            links = self.__get_links()

            self.__save_info_about_albums(links)

            self.__next_page()
            print(_step)

    def __next_page(self):
        """open next page for parsing"""
        self.__browser.find_element_by_xpath(next_page_xpath).click()

    def __open_site(self):
        """open site for parsing"""
        self.__browser.get(link_to_site)

    def __get_links(self):
        """return links to albums"""
        elements_for_links = self.__browser.find_elements_by_css_selector(
            for_links_selector
        )

        elements_with_links = []
        for element_for_link in elements_for_links:
            try:
                element_with_link = element_for_link.find_element_by_css_selector(
                    with_link_selector
                )
                elements_with_links.append(element_with_link)
            except NoSuchElementException:
                continue

        links = []
        for element_with_link in elements_with_links:
            link = element_with_link.get_attribute(link_attribute)
            links.append(link)

        return links

    def __save_info_about_albums(self, links):
        """save info about all albums"""
        self.__browser.execute_script("window.open('');")
        self.__browser.switch_to.window(self.__browser.window_handles[1])

        for link in links:
            self.__save_info_about_album(link)

        self.__browser.close()
        self.__browser.switch_to.window(self.__browser.window_handles[0])

    def __save_info_about_album(self, link):
        """save info about one definite album"""
        self.__browser.get(link)

        try:
            album = Album.objects.get(link_to_album=link)
        except Album.DoesNotExist:
            album = Album(link_to_album=link)
            album.title = self.__browser.find_element_by_css_selector(title_selector).text
            album.rating = self.__browser.find_element_by_css_selector(
                rating_selector
            ).get_attribute(rating_attribute)
            album.track_list = self.__browser.find_element_by_css_selector(
                track_list_selector
            ).text
            album.link_to_download = self.__browser.find_element_by_css_selector(
                link_to_download_selector
            ).get_attribute(link_to_download_attribute)

            album.save()

    def stop_parse(self):
        """stop parsing and close browser"""
        self.__browser.quit()
