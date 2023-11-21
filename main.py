import cx_Oracle

from GUI.gui import GUI

if __name__ == "__main__":
    cx_Oracle.init_oracle_client(lib_dir=r"c:\Users\Yanny\Downloads\instant_client.v.21.12")
    gui = GUI()
    gui.createMainWindow()