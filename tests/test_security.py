from app.security import gerar_hash, verificar_senha


def test_verificar_senha_correta():
    senha = "senhacerta"

    senha_hash = gerar_hash(senha)

    resultado = verificar_senha(
        senha,
        senha_hash
    )

    assert resultado is True


def test_verificar_senha_incorreta():
    senha = "senhacerta"

    senha_hash = gerar_hash(senha)

    resultado = verificar_senha(
        "senhaerrada",
        senha_hash
    )

    assert resultado is False