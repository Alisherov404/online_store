def callback_data_generator(text):
    res = text.replace(" & ", "_")
    res = res.replace(" ", "_").lower()
    return res.replace("-", "_")
