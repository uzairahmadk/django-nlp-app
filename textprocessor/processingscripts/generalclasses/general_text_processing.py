from textblob import TextBlob
from textblob.blob import Sentence
from textprocessor.processingscripts.generalclasses.calculation_scripts import MathemeticsCalculation

class GeneralTextProcessing:

    math_class = MathemeticsCalculation()

    def npn_percentage_statement(self, polarity):
        percentage_list = self.math_class.percentage_calculator(polarity)

        #find the index number of the maximum value in the list
        max_value = percentage_list.index(max(percentage_list))

        #Negative on index 0, Positive on index 1 and Neutral on index 2
        if max_value == 0:
            return 'Negativity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Possible Positivity: ' + str(percentage_list[1]) + '%'
        elif max_value == 1:
            return 'Possible Negativity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Positivity: ' + str(percentage_list[1]) + '%'
        else:
            return 'Possible Negativity: ' + str(percentage_list[0]) + '%, Neutrality: ' + str(percentage_list[2]) + '%, Possible Positivity: ' + str(percentage_list[1]) + '%'

    def npn_overall_statement(self, polarity):
        percentage_list = self.math_class.percentage_calculator(polarity)

        #find the index number of the maximum value in the list
        max_value = percentage_list.index(max(percentage_list))

        #Negative on index 0, Positive on index 1 and Neutral on index 2
        if max_value == 0:
            return 'Negative'
        elif max_value == 1:
            return 'Positive'
        else:
            return 'Neutral'

    def so_percentage_statement(self, subjectivity):
        percentage_list = self.math_class.percentage_calculator(subjectivity)

        #find the index number of the maximum value in the list
        max_value = percentage_list.index(max(percentage_list))

        #Objective on index 0, Subjective on index 1 and Neutral on index 2
        if max_value == 0:
            return 'Objectivity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Possible Subjectivity: ' + str(percentage_list[1]) + '%'
        elif max_value == 1:
            return 'Possible Objectivity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Subjectivity: ' + str(percentage_list[1]) + '%'
        else:
            return 'Possible Objectivity: ' + str(percentage_list[0]) + '%, Neutrality: ' + str(percentage_list[2]) + '%, Possible Subjectivity: ' + str(percentage_list[1]) + '%'

    def so_overall_statement(self, subjectivity):
        percentage_list = self.math_class.percentage_calculator(subjectivity)

        #find the index number of the maximum value in the list
        max_value = percentage_list.index(max(percentage_list))

        #Negative on index 0, Positive on index 1 and Neutral on index 2
        if max_value == 0:
            return 'Objective'
        elif max_value == 1:
            return 'Subjective'
        else:
            return 'Neutral'
