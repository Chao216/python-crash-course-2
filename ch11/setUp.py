import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):#创建一个调查对象和一组答案

        question = "what countries you have been to?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["Russia", "Finland", "Italy", "Grace", "Austria", "Hungary", "Poland"]

        def test_store_one_res(self):
            self.my_survey.store_response(self.responses[0]) # 使用store 存取第一个res
            self.assertIn(self.responses[0], self.my_survey.responses)

        def test_store_many_res(self):
            for res in self.responses:
                self.my_survey.store_response(res)

            for res in self.responses:
                self.assertIn(res, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()

