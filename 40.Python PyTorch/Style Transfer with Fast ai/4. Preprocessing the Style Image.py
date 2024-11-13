def get_style_im(url):
    download_url(url, 'style.jpg')
    fn = 'style.jpg'
    dset = Datasets(fn, tfms=[PILImage.create])
    dl = dset.dataloaders(after_item=[ToTensor()], after_batch=[IntToFloatTensor(), Normalize.from_stats(*imagenet_stats)], bs=1)
    return dl.one_batch()[0]
