from pytube import YouTube

link = 'https://www.youtube.com/watch?v=wjTn_EkgQRg&index=1&list=PLgJ7b1NurjD2oN5ZXbKbPjuI04d_S0V1K'
src = YouTube(link)

# prints all avaliable captions in various languages.
print('Captions Available: ', src.captions)
print()

# Getting only English captions by specifying 'en' as parameter
en_caption = src.captions.get_by_language_code('en')
print(en_caption.xml_captions)

# Instead of Captions in XML format we are converting it to string format.
en_caption_convert_to_srt = (en_caption.generate_srt_captions())
print(en_caption_convert_to_srt)
