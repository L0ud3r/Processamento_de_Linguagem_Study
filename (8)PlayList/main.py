# playlist.py
import ply.lex as plex
from ply.lex import TOKEN
from my_utils import slurp
from pprint import PrettyPrinter  # pretty printer


class Playlist:
    tokens = ("FAIXA", "AUTOR", "TEMPO", "LIXO1", "LIXO2", "LIXO3")
    states = (
        ("faixa", "exclusive"),
        ("tempo", "exclusive"),
        ("lixo", "exclusive"),
    )
    t_ANY_ignore = ""
    t_faixa_ignore = t_tempo_ignore = "\t"

    exp_reg_complicada = r"[^\t]+"

    # faixa da musica
    @TOKEN(exp_reg_complicada)
    def t_faixa_STR(self, t):
        t.type = "FAIXA"
        t.lexer.begin("tempo")
        return t

    # lixo ao final da linha
    def t_lixo_LIXO1(self, t):
        r".*\n"
        t.lexer.begin("INITIAL")
        return t

    # tempo
    def t_tempo_TEMPO(self, t):
        r"[0-9]+:[0-9]{2}"
        (minutes, _) = t.value.split(":")
        if int(minutes) >= 3:
            self.count[self.author] = self.count.get(self.author, 0) + 1
        t.lexer.begin("lixo")
        return t

    # nome do autor/interprete
    @TOKEN(exp_reg_complicada)
    def t_STR(self, t):
        "Documentacao"
        t.type = "AUTOR"
        self.author = t.value
        t.lexer.begin("faixa")
        return t

    def t_LIXO2(self, t):
        r"\t.+\n"
        return t

    def t_LIXO3(self, t):
        r"\t+\t"
        return t

    def t_ANY_error(self, t):
        print(f"Unexpected token: {t.value[:10]}")
        exit(1)

    def __init__(self):
        self.lexer = None
        self.author = None
        self.count = {}  # empty dictionary

    @staticmethod
    def builder(**kwargs):
        obj = Playlist()
        obj.lexer = plex.lex(module=obj, **kwargs)
        return obj

    def parse(self, filename):
        contents = slurp(filename)
        self.lexer.input(contents)
        for token in iter(self.lexer.token, None):
            pass
        return self.count


playlist = Playlist.builder()
authors = playlist.parse("Playlist.txt")
pp = PrettyPrinter(indent=4, width=10)
pp.pprint(authors)
