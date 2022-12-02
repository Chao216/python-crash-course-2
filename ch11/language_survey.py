from survey import AnonymousSurvey

question = "what languages do you speak?"

my_survey = AnonymousSurvey(question)

my_survey.show_question()
my_survey.store_response("English")
my_survey.store_response("German")
my_survey.store_response("Japanese")
my_survey.store_response("Spanisch")

my_survey.show_responses()
