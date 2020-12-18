import pytest

from Pages.MainPage import MainPage
from Pages.ChallengeDom import ChallengeDOM


@pytest.mark.usefixtures("init_driver")
class TestChallengeDom():


    def test_click_middle_button(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_challenging_dom()

        self.challengeDom=ChallengeDOM(self.driver)

        button_names_list=self.challengeDom.click_middlebutton_and_get_text()

        assert button_names_list[0] != button_names_list[1]


    def test_row_five_header_and_data(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_challenging_dom()

        self.challengeDom=ChallengeDOM(self.driver)

        actual_header_list=self.challengeDom.get_header_data()
        actual_row_data_list=self.challengeDom.get_row_data()

        expected_header_list=['Lorem', 'Ipsum', 'Dolor', 'Sit', 'Amet', 'Diceret', 'Action']
        expected_row_data_list=['Iuvaret4', 'Apeirian4', 'Adipisci4', 'Definiebas4', 
                                'Consequuntur4', 'Phaedrum4', 'edit delete']
        final_result = False

        for data_index in range(0,len(expected_header_list)):

            if (actual_header_list[data_index] != expected_header_list[data_index] or 
                actual_row_data_list[data_index] != expected_row_data_list[data_index]):

                final_result= False
            else:

                final_result=True
 
        assert final_result == True
    