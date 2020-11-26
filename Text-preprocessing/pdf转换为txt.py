for filename in filename_list:
    #重构文件路径
    file_dir = '../data'
    file_path = os.path.join(file_dir,filename)
    try:
        outF = open(filename[:-4]+'.txt', "w", encoding = 'utf-8')
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                outF.write(text)       
        outF.close()
        print("converted: " + filename)
    except:
        print("cannot read: " + filename)
