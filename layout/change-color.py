import xml.etree.ElementTree as ET


def change_svg_color(input_file, output_file, new_color):
    # پارس کردن فایل SVG
    tree = ET.parse(input_file)
    root = tree.getroot()


    ns = {'svg': 'http://www.w3.org/2000/svg'}


    for elem in root.findall(".//*[@fill]", ns):
        elem.set('fill', new_color)


    for elem in root.findall(".//*[@stroke]", ns):
        elem.set('stroke', new_color)


    tree.write(output_file)



change_svg_color('img/file-brackets-curly.svg', 'img/file-brackets-curly(W).svg', '#FFFFFF')