from apps import formDAO

df = formDAO.get_all()

df = df.fillna('')
df.city = df.city.map(lambda state_id: formDAO.states[state_id] if state_id else '')
df.gender = df.gender.map(lambda gender_id: formDAO.genders[gender_id] if gender_id else '')

def get_languages(row):
    language_ids = row.languages.split('|')
    languages = []
    for id in language_ids:
        languages.append(formDAO.languages[id])
    row.languages = ", ".join(languages)
    return row

df.apply(get_languages, axis='columns')

df.columns = df.columns.map(lambda name : name.capitalize())

print(df.head())