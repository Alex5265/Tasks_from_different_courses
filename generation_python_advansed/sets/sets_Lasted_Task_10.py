# Генераторы множеств
# Необходимо с помощью генератора создать множество уникальных слов(в нижнем регистре) длиною менее 4 символов
# в приведенной строке без учета знаков препинания

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

set_sentence = {i.lower().strip('(),.;:&!') for i in sentence.split() if len(i.strip('(),.;:&!')) < 4}

print(*sorted(set_sentence))