import docx
document = docx.Document("testdoc1.docx")

pgs = filter(lambda x: x.text.strip()!= '', document.paragraphs)

s_id = next(i for i in range(len(pgs)) if pgs[i].text == 'Summary')

c_style = pgs[s_id + 1].style.name
for i in range(s_id +1, len(pgs)):
    if pgs[i].style.name == c_style:
        print(pgs[i].text)
