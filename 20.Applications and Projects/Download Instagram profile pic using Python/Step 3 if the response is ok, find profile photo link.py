if response.ok:
	html=response.text

	bs_html=bs(html, features="lxml")
	bs_html=bs_html.text
	index=bs_html.find('profile_pic_url_hd')+21

	remaining_text=bs_html[index:]
	remaining_text_index=remaining_text.find('requested_by_viewer')-3
	string_url=remaining_text[:remaining_text_index]

	print(string_url, "\n \n downloading..........")
