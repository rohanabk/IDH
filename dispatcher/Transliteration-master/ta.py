
from transliteration import getInstance
t = getInstance()
text = "ನಮಸ್ಕಾರ"
t_text = t.transliterate(text, "ml_IN")
print t_text #"നമസ്കാര"

