#!/usr/bin/python3
import os

def updateStyle(c_path, c_file, colors):
    # 
    if not (os.path.isdir(c_path) and os.path.isfile(c_file)):
        print("Caminho(s) não existe(m)")
        return -1

    theme_file = open(c_file, "r")
    new_theme = theme_file.read()
    for i, cor in enumerate(colors):
        new_theme = new_theme.replace("{color" + str(i) + "}", cor)
    theme_file.close()
    # escreve no local do openbox
    theme_file = open( c_path + c_file, "w")
    theme_file.write(new_theme)
    theme_file.close()


def main():
    # Get environment variables
    home = os.getenv('HOME')
    eww_path = f"{home}/.config/eww/Bar/"
    eww_file = "eww.scss"
    openbox_path = f"{home}/.themes/CustomPixels/openbox-3/"
    openbox_file = "themerc"
    wal_path = f"{home}/.cache/wal/colors"
    
    # pega as cores geradas pelo pywal
    colors = []
    colors_file = open(wal_path, "r")
    for line in colors_file:
        colors.append(line.replace("\n", "").upper())
    colors_file.close()

    updateStyle(openbox_path, openbox_file, colors)
    os.system("openbox --reconfigure")
    updateStyle(eww_path, eww_file, colors)

    # abre o arquivo de tema do openbox e substitui as cores e as deixa em new_theme
    # e finalmente atualiza o openbox



if __name__ == "__main__":
    main()