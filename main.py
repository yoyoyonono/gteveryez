import googletrans as gt


translator = gt.Translator()

input_text = "Congratulations to @Kento Nishi!!! He has been named as one of the top 300 scholars in the 81st Regeneron Science Talent Search—the nation's oldest and most prestigious science and mathematics competition for high school seniors."
original_language = translator.detect(input_text).lang

for langcode in (gt.LANGCODES.values()):
    input_text = translator.translate(input_text, langcode).text
    print(langcode + '\t' + input_text, '\t' + translator.translate(input_text, original_language).text, sep='\n', end='\n\n')

