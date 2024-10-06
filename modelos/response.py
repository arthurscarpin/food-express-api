from fastapi import status

responses = {
    400: {'description': 'Erro de validação'},
    422: {'description': 'Entidade não processável'},
    500: {'description': 'Erro interno do servidor'}
}