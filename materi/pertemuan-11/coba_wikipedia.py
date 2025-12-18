import wikipedia

wikipedia.set_lang("id")

ringkasan = wikipedia.summary("black clover", sentences=5)
print(ringkasan)