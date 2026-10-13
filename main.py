import sys
from ongaku.core.app import App

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    sys.exit(main())

# todo próximos passos

# done colocar sistema de temas 
# done escolher a paleta dos outros temas, implementar mais duas cores (ficou faltando)
# implementar detecção de tempo ouvido pra estatísticas como listen_time ou play_count

# todo depois:

# conseguir mostrar arte do álbum junto com o nome da música
# terminar sistema de álbuns, playlists e genres
# permitir colocar tags em músicas, como #dahora
# ? talvez reescrever metadata da música se conveniente?
# implementar análise do bunseki (em paralelo, usar asyncio ou threading)





