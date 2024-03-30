import iknowpy

engine = iknowpy.iKnowEngine()

# show supported languages
print(engine.get_languages_set())

# index some text
text = 'This is a test of the Python interface to the iKnow engine.'
engine.index(text, 'en')

# print the raw results
print(engine.m_index)

# or make it a little nicer
for s in engine.m_index['sentences']:
    for e in s['entities']:
        print('<'+e['type']+'>'+e['index']+'</'+e['type']+'>', end=' ')
    print('\n')