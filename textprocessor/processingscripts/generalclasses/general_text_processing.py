from textblob import TextBlob
from textblob.blob import Sentence

class GeneralTextProcessing:

    def npn_percentage_calculator(self, polarity):

        return_result = []

        #check if the number is negative or positive
        if polarity < 0:
            #convert the number to positive
            polarity = -(polarity)

        #zero value polarity returns negative result so if zero then no percentage calculation
        if polarity != 0:
            polarity_percentage = (polarity * 100)
        else:
            polarity_percentage = 50

        #converting to integer
        polarity_percentage = int(polarity_percentage)

        #check if negative or positive
        #range 45 to 55 is calculated a neutral point here
        if polarity_percentage > 0 and polarity_percentage < 45:
            negative_percentage = 100 - polarity_percentage
            neutral_percentage = 55 - polarity_percentage
            positive_percentage = 100 - negative_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        elif polarity_percentage >= 45 and polarity_percentage <= 55:

            #if maximun negative density
            if polarity_percentage < 49:
                negative_percentage = 50 - polarity_percentage
                neutral_percentage = polarity_percentage
                positive_percentage = 0
            else:
                negative_percentage = 0
                neutral_percentage = polarity_percentage
                positive_percentage = 56 - polarity_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        else:
            negative_percentage = polarity_percentage - 45
            positive_percentage = 100 - negative_percentage
            neutral_percentage = 100 - polarity_percentage

            return_result.append(negative_percentage)
            return_result.append(positive_percentage)
            return_result.append(neutral_percentage)

        return return_result

    def npn_percentage_statement(self, polarity):
        percentage_list = self.npn_percentage_calculator(polarity)

        #find the index number of the maximum value in the list
        max_value = percentage_list.index(max(percentage_list))

        #Negative on index 0, Positive on index 1 and Neutral on index 2
        if max_value == 0:
            return 'Negativity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Possible Positivity: ' + str(percentage_list[1]) + '%'
        elif max_value == 1:
            return 'Possible Negativity: ' + str(percentage_list[0]) + '%, Possible Neutrality: ' + str(percentage_list[2]) + '%, Positivity: ' + str(percentage_list[1]) + '%'
        else:
            return 'Possible Negativity: ' + str(percentage_list[0]) + '%, Neutrality: ' + str(percentage_list[2]) + '%, Possible Positivity: ' + str(percentage_list[1]) + '%'
