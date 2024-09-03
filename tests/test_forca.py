import pytest
import os
from python_text_games.forca import (
    inicializa_letras_acertadas,
    marca_chute_correto,
    desenha_forca,
    imprime_mensagem_vencedor,
    imprime_mensagem_perdedor,
    carrega_palavra_secreta,
)
from unittest.mock import patch, mock_open


def test_inicializa_letras_acertadas():
    palavra = "BANANA"
    resultado_esperado = ["_", "_", "_", "_", "_", "_"]
    assert inicializa_letras_acertadas(palavra) == resultado_esperado

    # Teste com palavra vazia
    palavra_vazia = ""
    assert inicializa_letras_acertadas(palavra_vazia) == []


def test_marca_chute_correto():
    palavra_secreta = "BANANA"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    chute = "A"

    marca_chute_correto(chute, letras_acertadas, palavra_secreta)

    resultado_esperado = ["_", "A", "_", "A", "_", "A"]
    assert letras_acertadas == resultado_esperado

    # Teste com chute incorreto
    chute_incorreto = "Z"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    marca_chute_correto(chute_incorreto, letras_acertadas, palavra_secreta)
    assert letras_acertadas == ["_", "_", "_", "_", "_", "_"]


def test_desenha_forca(capfd):
    desenha_forca(3)
    out, err = capfd.readouterr()

    assert " |      (_)   " in out
    assert " |      \\|    " in out
    assert " |            " in out

    # Teste com erro máximo (7)
    desenha_forca(7)
    out, err = capfd.readouterr()
    assert " |      / \\   " in out


@patch("python_text_games.games_util.imprime_taca")
def test_imprime_mensagem_vencedor(mock_imprime_taca, capfd):
    imprime_mensagem_vencedor()
    out, err = capfd.readouterr()

    assert "Parabéns, você ganhou!" in out
    mock_imprime_taca.assert_called_once()


@patch("python_text_games.games_util.imprime_caveira")
def test_imprime_mensagem_perdedor(mock_imprime_caveira, capfd):
    palavra_secreta = "ABACAXI"
    imprime_mensagem_perdedor(palavra_secreta)
    out, err = capfd.readouterr()

    assert "Puxa, você foi enforcado!" in out
    assert "A palavra era ABACAXI" in out
    mock_imprime_caveira.assert_called_once()


@patch("builtins.open", new_callable=mock_open, read_data="banana\nmorango\nlaranja")
@patch("random.randrange", return_value=0)
def test_carrega_palavra_secreta(mock_randrange, mock_open_file):
    palavra_secreta = carrega_palavra_secreta()

    assert palavra_secreta == "BANANA"

    # Construindo o caminho absoluto esperado
    caminho_esperado = os.path.join(
        os.path.dirname(__file__), "..", "python_text_games", "db", "frutas.txt"
    )
    mock_open_file.assert_called_once_with(os.path.abspath(caminho_esperado), "r")
